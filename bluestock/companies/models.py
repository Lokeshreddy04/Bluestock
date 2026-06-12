# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DimCompany(models.Model):
    symbol = models.TextField(primary_key=True)
    company_name = models.TextField()

    class Meta:
        managed = False
        db_table = "dim_company"


class DimHealthLabel(models.Model):
    label_id = models.AutoField(primary_key=True)
    label_name = models.CharField(max_length=20, blank=True, null=True)
    min_score = models.IntegerField(blank=True, null=True)
    max_score = models.IntegerField(blank=True, null=True)
    color_hex = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dim_health_label'


class DimCompany(models.Model):
    symbol = models.TextField(primary_key=True)

    company_name = models.TextField(
        blank=True,
        null=True
    )

    sector_name = models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = "dim_company"


class DimYear(models.Model):
    year_id = models.AutoField(primary_key=True)
    year_label = models.CharField(max_length=20, blank=True, null=True)
    fiscal_year = models.IntegerField(blank=True, null=True)
    quarter = models.CharField(max_length=10, blank=True, null=True)
    is_ttm = models.BooleanField(blank=True, null=True)
    is_half_year = models.BooleanField(blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dim_year'


class FactAnalysis(models.Model):
    symbol = models.TextField(blank=True, null=True)
    period_label = models.TextField(blank=True, null=True)
    sales_growth_pct = models.FloatField(blank=True, null=True)
    profit_growth_pct = models.FloatField(blank=True, null=True)
    stock_cagr_pct = models.FloatField(blank=True, null=True)
    roe_pct = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fact_analysis'


class FactBalanceSheet(models.Model):
    symbol = models.TextField(primary_key=True)
    year = models.TextField(blank=True, null=True)
    equity_capital = models.FloatField(blank=True, null=True)
    reserves = models.BigIntegerField(blank=True, null=True)
    borrowings = models.BigIntegerField(blank=True, null=True)
    total_assets = models.BigIntegerField(blank=True, null=True)
    debt_to_equity = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fact_balance_sheet'


class FactBalanceSheets(models.Model):
    pk = models.CompositePrimaryKey('symbol', 'year')
    symbol = models.CharField(max_length=20)
    year = models.TextField()
    equity_capital = models.FloatField(blank=True, null=True)
    reserves = models.FloatField(blank=True, null=True)
    borrowings = models.FloatField(blank=True, null=True)
    total_assets = models.FloatField(blank=True, null=True)
    debt_to_equity = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fact_balance_sheets'


class FactCashFlow(models.Model):
    symbol = models.TextField(primary_key=True)
    year = models.TextField(blank=True, null=True)
    operating_activity = models.FloatField(blank=True, null=True)
    investing_activity = models.FloatField(blank=True, null=True)
    financing_activity = models.FloatField(blank=True, null=True)
    net_cash_flow = models.FloatField(blank=True, null=True)
    free_cash_flow = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fact_cash_flow'


class FactMlScores(models.Model):
    symbol = models.TextField(primary_key=True)
    health_score = models.FloatField(blank=True, null=True)
    health_label = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fact_ml_scores'


class FactProfitLoss(models.Model):
    id = models.BigIntegerField(primary_key=True)
    symbol = models.TextField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    sales = models.BigIntegerField(blank=True, null=True)
    expenses = models.BigIntegerField(blank=True, null=True)
    operating_profit = models.FloatField(blank=True, null=True)
    opm_percentage = models.FloatField(blank=True, null=True)
    other_income = models.BigIntegerField(blank=True, null=True)
    interest = models.BigIntegerField(blank=True, null=True)
    depreciation = models.BigIntegerField(blank=True, null=True)
    profit_before_tax = models.BigIntegerField(blank=True, null=True)
    tax_percentage = models.FloatField(blank=True, null=True)
    net_profit = models.BigIntegerField(blank=True, null=True)
    eps = models.FloatField(blank=True, null=True)
    dividend_payout = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fact_profit_loss'


class FactProsCons(models.Model):
    symbol = models.CharField(max_length=20, blank=True, null=True)
    is_pro = models.BooleanField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=20, blank=True, null=True)
    confidence = models.FloatField(blank=True, null=True)
    generated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fact_pros_cons'


class FactPeers(models.Model):
    company = models.TextField(primary_key=True)

    peer_1 = models.TextField(blank=True, null=True)
    peer_2 = models.TextField(blank=True, null=True)
    peer_3 = models.TextField(blank=True, null=True)
    peer_4 = models.TextField(blank=True, null=True)
    peer_5 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "fact_peers"



class FactForecasts(models.Model):
    symbol = models.CharField(
        max_length=20,
        primary_key=True
    )

    forecast_sales = models.FloatField(
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = "fact_forecasts"