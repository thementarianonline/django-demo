from django.urls import path
from . import views
from django.urls import include


urlpatterns = [
    path('posts/', views.posts, name='posts'),
    path('posts/<slug:slug>/', views.post, name="post"),
    path('summernote/', include('django_summernote.urls')),
]  