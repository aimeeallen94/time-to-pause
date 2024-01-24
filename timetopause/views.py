from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
    paginate_by = 4

def base(request):
    return render(request, '../templates/base.html')

def about(request):
    return render(request, '../templates/about.html')

def blog(request):
    return render(request, '../templates/blog.html')

def home(request):
    return render(request, '../templates/home.html')