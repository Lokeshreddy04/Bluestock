from rest_framework import serializers
from .models import DimCompany

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