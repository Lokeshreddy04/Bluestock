from rest_framework import serializers
from .models import DimCompany, FactPeers

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = DimCompany
        fields = "__all__"


from rest_framework import serializers
from .models import FactProfitLoss


class ProfitLossSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactProfitLoss
        fields = "__all__"


from .models import FactBalanceSheet

class BalanceSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactBalanceSheet
        fields = "__all__"


from .models import FactCashFlow

class CashFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactCashFlow
        fields = "__all__"


from .models import FactMlScores

class HealthScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactMlScores
        fields = "__all__"


class PeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactPeers
        fields = "__all__"


from .models import FactForecasts

class ForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactForecasts
        fields = "__all__"


class CompanyDashboardSerializer(serializers.Serializer):
    company = serializers.DictField()
    health_score = serializers.DictField()
    forecast = serializers.DictField()
    peers = serializers.ListField()
    profit_loss = serializers.ListField()
    balance_sheet = serializers.ListField()
    cash_flow = serializers.ListField()