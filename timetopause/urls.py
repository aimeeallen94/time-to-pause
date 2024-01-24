from . import views
from django.urls import path, include

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('base/', views.base, name='base'),
    path('PostList/', views.PostList.as_view(), name='post_list'),
]