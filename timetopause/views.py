from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from .forms import CommentForm

class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'timetopause/post_list.html'
    paginate_by = 4

def base(request):
    return render(request, 'timetopause/base.html')

#def about(request):
#    return render(request, 'about/about.html')

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
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    comment_form = CommentForm()

    return render(
        request, 
        "timetopause/post_detail.html",
        {
            "post":post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            },
)