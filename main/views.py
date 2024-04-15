from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from monthlyissues.models import MonthlyIssues
from posts.models import Posts

def main(request):
    monthlyissue = MonthlyIssues.objects.all().order_by("-date").values()
    posts = Posts.objects.all().filter(status="p").order_by("-datetime").values()
    template = loader.get_template('home.html')
    context = {
        'monthlyissue': monthlyissue,
        'posts': posts,
    }
    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template('about.html')
    context = {

    }
    return HttpResponse(template.render(context, request))
# Create your views here.