from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('blog/', views.blog, name='blog'),
    path('post_list/', views.PostList.as_view(), name='post_list'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.edit_comment, name='edit_comment'),
]