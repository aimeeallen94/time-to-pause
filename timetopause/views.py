from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 4

def get_base_html(request):
    return render(request, '../templates/base.html')

#def get_about_html(request):
#    return render(request, '../templates/about.html')