from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm

class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'timetopause/post_list.html'
    paginate_by = 4

def base(request):
    return render(request, 'timetopause/base.html')

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
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

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

def edit_comment(request, slug, comment_id):
    if request.method == 'POST':

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, message.ERROR, 'Error updating comment!')

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def delete_comment(request, slug, comment_id):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)

        if comment.author == request.user:
            comment.delete()
            messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
        else:
            messages.add_message(request, message.ERROR, 'You can only delete a comment you wrote.')

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))