from django.urls import path
from . import views


urlpatterns = [

    path("", views.fintech_funding, name="fintech_funding"),
    path("fintech_funding_add", views.fintech_funding_add, name="fintech_funding_add"),
    # path("expense_detail", views.expense_detail, name="expense_detail"),
    # path("summary", views.expense_summary, name="expenses-summary"),
    path("fintech_funding_edit/<int:id>", views.fintech_funding_edit, name="fintech_funding_edit"),
    path("fintech_funding_delete/<int:id>", views.fintech_funding_delete, name="fintech_funding_delete"),
    # path('expenses/search_expenses', views.search_expenses, name='search_expenses'),
    # path('expenses/summary_rest', views.expense_summary_rest,
    #      name='expenses_summary_rest'),
    # path('expenses/three_months_summary', views.last_3months_stats,
    #      name='three_months_summary'),

    # path('expenses/last_3months_expense_source_stats',
    #      views.last_3months_expense_source_stats, name="last_3months_expense_source_stats")
]
