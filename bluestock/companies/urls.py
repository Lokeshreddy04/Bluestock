from django.urls import path
from .views import CompanySearchView, ForecastView, PeerView, ProfitLossView, SectorDetailView, SectorListView
from .views import BalanceSheetView
from .views import CashFlowView
from .views import HealthScoreView
from .views import CompanyDashboardView

from .views import (
    CompanyListView,
    CompanyDetailView
)

urlpatterns = [
    path(
        "companies/",
        CompanyListView.as_view(),
        name="company-list"
    ),

    path(
        "companies/<str:symbol>/",
        CompanyDetailView.as_view(),
        name="company-detail"
    ),
    path(
    "profit-loss/<str:symbol>/",
    ProfitLossView.as_view(),
    name="profit-loss"
),
path(
    "balance-sheet/<str:symbol>/",
    BalanceSheetView.as_view(),
    name="balance-sheet"
),

path(
    "cash-flow/<str:symbol>/",
    CashFlowView.as_view(),
    name="cash-flow"
),
path(
    "health-score/<str:symbol>/",
    HealthScoreView.as_view(),
    name="health-score"
),
path(
    "company-dashboard/<str:symbol>/",
    CompanyDashboardView.as_view(),
    name="company-dashboard"
),
path(
    "search/",
    CompanySearchView.as_view(),
    name="company-search"
),
path(
    "peers/<str:symbol>/",
    PeerView.as_view(),
    name="peers"
),
path(
    "forecast/<str:symbol>/",
    ForecastView.as_view(),
    name="forecast"
),

path(
    "sectors/",
    SectorListView.as_view(),
    name="sector-list"
),

path(
    "sectors/<str:sector_name>/",
    SectorDetailView.as_view(),
    name="sector-detail"
),

path(
    "company-dashboard/<str:symbol>/",
    CompanyDashboardView.as_view(),
    name="company-dashboard"
),
]