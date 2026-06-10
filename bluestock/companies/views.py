from rest_framework import generics

from .models import DimCompany
from .serializers import CompanySerializer, HealthScoreSerializer


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