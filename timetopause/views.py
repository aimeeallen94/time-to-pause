from django.shortcuts import render, get_object_or_404
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

def post_detail(request, slug):
    """
    Displaying an individual blog post as a model
    Interpreting model from url post_detail.html in timetopause
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    return render(request, "timetopause/post_detail.html", ("post":post),)