from django.urls import path

from .views import (
    company_scores,
    dashboard,
    company_detail,
    top_companies,
    search_company
)

urlpatterns = [

    path('', dashboard, name='dashboard'),

    path(
        'scores/',
        company_scores,
        name='company_scores'
    ),

    path(
        'company/<str:symbol>/',
        company_detail,
        name='company_detail'
    ),
    path(
    'top-companies/',
    top_companies,
    name='top_companies'
),
    path(
    'search/',
    search_company,
    name='search_company'
),
]