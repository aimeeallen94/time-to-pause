from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('blog/', views.blog, name='blog'),
    path('post_list/', views.PostList.as_view(), name='post_list'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.edit_comment, name='edit_comment'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.delete_comment, name='delete_comment'),
]