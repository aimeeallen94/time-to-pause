from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'timetopause/post_list.html'
    paginate_by = 4

def base(request):
    return render(request, 'timetopause/base.html')

def about(request):
    return render(request, 'timetopause/about.html')

def blog(request):
    return render(request, 'timetopause/post_list.html')

def home(request):
    return render(request, 'timetopause/home.html')