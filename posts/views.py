from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Posts

def posts(request):
    myposts = Posts.objects.all().filter(status="p").order_by('-datetime').values()
    template = loader.get_template('posts.html')
    context = {
        'myposts': myposts,
    }
    return HttpResponse(template.render(context, request))

def post(request, slug):
  mypost = Posts.objects.get(slug=slug)
  template = loader.get_template('post.html')
  context = {
    'mypost': mypost,
  }
  return HttpResponse(template.render(context, request))
# Create your views here.
