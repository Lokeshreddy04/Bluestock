from rest_framework import generics

from .models import DimCompany, FactForecasts, FactPeers
from .serializers import CompanySerializer, ForecastSerializer, HealthScoreSerializer



class CompanyListView(generics.ListAPIView):
    queryset = DimCompany.objects.all()
    serializer_class = CompanySerializer


class CompanyDetailView(generics.RetrieveAPIView):
    queryset = DimCompany.objects.all()
    serializer_class = CompanySerializer
    lookup_field = "symbol"


from rest_framework import generics

from .models import FactProfitLoss
from .serializers import ProfitLossSerializer


class ProfitLossView(generics.ListAPIView):
    serializer_class = ProfitLossSerializer

    def get_queryset(self):
        symbol = self.kwargs["symbol"]
        return (
            FactProfitLoss.objects
            .filter(symbol=symbol)
            .order_by("year")
        )
    
from .models import FactBalanceSheet
from .serializers import BalanceSheetSerializer

class BalanceSheetView(generics.ListAPIView):
    serializer_class = BalanceSheetSerializer

    def get_queryset(self):
        symbol = self.kwargs["symbol"]

        return (
            FactBalanceSheet.objects
            .filter(symbol=symbol)
            .order_by("year")
        )

from .models import FactCashFlow
from .serializers import CashFlowSerializer


class CashFlowView(generics.ListAPIView):
    serializer_class = CashFlowSerializer

    def get_queryset(self):
        symbol = self.kwargs["symbol"]

        return (
            FactCashFlow.objects
            .filter(symbol=symbol)
            .order_by("year")
        )


from rest_framework import generics
from .models import FactMlScores
# from .serializers import HealthScoreSerializer


class HealthScoreView(generics.RetrieveAPIView):
    serializer_class = HealthScoreSerializer

    def get_object(self):
        symbol = self.kwargs["symbol"]

        return (
            FactMlScores.objects
            .filter(symbol=symbol)
            .first()
        )
    

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import (
    DimCompany,
    FactProfitLoss,
    FactBalanceSheet,
    FactCashFlow,
    FactMlScores
)

from .serializers import (
    CompanySerializer,
    ProfitLossSerializer,
    BalanceSheetSerializer,
    CashFlowSerializer,
    HealthScoreSerializer
)

class CompanyDashboardView(APIView):

    def get(self, request, symbol):

        company = DimCompany.objects.get(symbol=symbol)

        health_score = (
            FactMlScores.objects
            .filter(symbol=symbol)
            .first()
        )

        profit_loss = (
            FactProfitLoss.objects
            .filter(symbol=symbol)
            .order_by("year")
        )

        balance_sheet = (
            FactBalanceSheet.objects
            .filter(symbol=symbol)
            .order_by("year")
        )

        cash_flow = (
            FactCashFlow.objects
            .filter(symbol=symbol)
            .order_by("year")
        )

        data = {
            "company": CompanySerializer(company).data,

            "health_score":
                HealthScoreSerializer(
                    health_score
                ).data,

            "profit_loss":
                ProfitLossSerializer(
                    profit_loss,
                    many=True
                ).data,

            "balance_sheet":
                BalanceSheetSerializer(
                    balance_sheet,
                    many=True
                ).data,

            "cash_flow":
                CashFlowSerializer(
                    cash_flow,
                    many=True
                ).data,
        }

        return Response(data)
    

from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response

class CompanySearchView(APIView):

    def get(self, request):

        query = request.GET.get("q", "")

        companies = (
            DimCompany.objects
            .filter(
                Q(symbol__icontains=query) |
                Q(company_name__icontains=query)
            )[:10]
        )

        data = [
            {
                "symbol": c.symbol,
                "company_name": c.company_name
            }
            for c in companies
        ]

        return Response(data)
    


class PeerView(APIView):

    def get(self, request, symbol):

        peer = FactPeers.objects.filter(
            company=symbol
        ).first()

        if not peer:
            return Response(
                {"error": "Company not found"},
                status=404
            )

        data = {
            "company": peer.company,
            "peers": [
                peer.peer_1,
                peer.peer_2,
                peer.peer_3,
                peer.peer_4,
                peer.peer_5,
            ]
        }

        return Response(data)
    

class ForecastView(APIView):

    def get(self, request, symbol):

        forecast = (
            FactForecasts.objects
            .filter(symbol=symbol)
            .first()
        )

        if not forecast:
            return Response(
                {"error": "Forecast not found"},
                status=404
            )

        return Response(
            ForecastSerializer(
                forecast
            ).data
        )
    

from rest_framework.views import APIView
from rest_framework.response import Response

class SectorListView(APIView):

    def get(self, request):

        sectors = (
            DimCompany.objects
            .values_list(
                "sector_name",
                flat=True
            )
            .distinct()
            .order_by("sector_name")
        )

        return Response(list(sectors))
    

class SectorDetailView(APIView):

    def get(self, request, sector_name):

        companies = DimCompany.objects.filter(
            sector_name=sector_name
        )

        company_symbols = list(
            companies.values_list(
                "symbol",
                flat=True
            )
        )

        company_count = len(company_symbols)

        profit_data = FactProfitLoss.objects.filter(
            symbol__in=company_symbols
        )

        health_data = FactMlScores.objects.filter(
            symbol__in=company_symbols
        )

        avg_revenue = (
            sum(
                p.sales or 0
                for p in profit_data
            )
            / len(profit_data)
        ) if profit_data else 0

        avg_profit = (
            sum(
                p.net_profit or 0
                for p in profit_data
            )
            / len(profit_data)
        ) if profit_data else 0

        avg_health = (
            sum(
                h.health_score or 0
                for h in health_data
            )
            / len(health_data)
        ) if health_data else 0

        top_companies = [
            {
                "symbol": c.symbol,
                "company_name": c.company_name
            }
            for c in companies[:10]
        ]

        return Response({
            "sector": sector_name,
            "company_count": company_count,
            "avg_revenue": round(avg_revenue, 2),
            "avg_profit": round(avg_profit, 2),
            "avg_health_score": round(avg_health, 2),
            "top_companies": top_companies
        })
    

class CompanyDashboardView(APIView):

    def get(self, request, symbol):

        company = DimCompany.objects.filter(
            symbol=symbol
        ).first()

        health = FactMlScores.objects.filter(
            symbol=symbol
        ).first()

        forecast = FactForecasts.objects.filter(
            symbol=symbol
        ).first()

        peers = FactPeers.objects.filter(
            company=symbol
        ).first()

        profit_loss = FactProfitLoss.objects.filter(
            symbol=symbol
        )

        balance_sheet = FactBalanceSheet.objects.filter(
            symbol=symbol
        )

        cash_flow = FactCashFlow.objects.filter(
            symbol=symbol
        )

        return Response({
            "company": {
                "symbol": company.symbol,
                "company_name": company.company_name,
                "sector_name": company.sector_name
            },

            "health_score": {
                "score": health.health_score,
                "label": health.health_label
            } if health else None,

            "forecast": {
                "forecast_sales":
                forecast.forecast_sales
            } if forecast else None,

            "peers": [
                peers.peer_1,
                peers.peer_2,
                peers.peer_3,
                peers.peer_4,
                peers.peer_5
            ] if peers else [],

            "profit_loss":
                ProfitLossSerializer(
                    profit_loss,
                    many=True
                ).data,

            "balance_sheet":
                BalanceSheetSerializer(
                    balance_sheet,
                    many=True
                ).data,

            "cash_flow":
                CashFlowSerializer(
                    cash_flow,
                    many=True
                ).data
        })