from django.shortcuts import render
from .models import MonthlyIssues, Page
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def monthly_issues(request):
    monthlyissue = MonthlyIssues.objects.all().order_by('-date').values()
    template = loader.get_template('monthly_issues.html')
    context = {
        'monthlyissue': monthlyissue,
    }
    return HttpResponse(template.render(context, request))

def monthly_issue(request, slug):
  myissue = MonthlyIssues.objects.get(slug=slug)
  pages = Page.objects.filter(monthlyissue=myissue)
  template = loader.get_template('monthly_issue.html')
  context = {
    'myissue': myissue,
    'pages': pages,
  }
  return HttpResponse(template.render(context, request))