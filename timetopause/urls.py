from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('base/', views.base, name='base'),
    path('post_list/', views.PostList.as_view(), name='post_list'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]