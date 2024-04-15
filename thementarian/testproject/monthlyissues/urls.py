from django.urls import path
from . import views

urlpatterns = [
    path('monthly_issues/', views.monthly_issues, name='MonthlyIssues'),
    path('monthly_issues/<slug:slug>', views.monthly_issue, name="Monthlyissue"),

] 