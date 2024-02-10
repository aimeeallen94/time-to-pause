from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm


class PostList(generic.ListView):
    """
    This class is setting the blog post list
    to be laid out in a style of 4 posts per page.
    """
    queryset = Post.objects.all()
    template_name = 'timetopause/post_list.html'
    paginate_by = 4


"""
The below three functions link up urls to display
the desired page by the user.
"""


def base(request):
    return render(request, 'timetopause/base.html')


def blog(request):
    return render(request, 'timetopause/post_list.html')


def home(request):
    return render(request, 'timetopause/home.html')


def post_detail(request, slug):
    """
    This function allowed users to place a comment below a
    blog post and to display a message to the user to
    inform them that their comment is awaiting approval.
    This message only displays to the user who has placed
    the comment. This will return the user to the blog
    post they had been on when they placed the comment.
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
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            },
    )


"""
This allows users to edit a comment that they have placed
under a blog post and to display a message confirming a
comment has been edited and alternatively displaying an
error message if there was an issue in editing a comment.
"""


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
            messages.add_message(
                request, message.ERROR, 'Error updating comment!')

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


"""
This allows users to delete a commment that they have left
under a blog post and to display a message once they have
deleted the blog post to alert the user that they have
deleted a commment.
"""


def delete_comment(request, slug, comment_id):

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(
            request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR,
            'You can only delete a comment you wrote.')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


"""
This class is used to allow users to like a blog post if
they are aunthenticated and to display a message if they
like and unlike a post. This will also redirect the user back to
the post they were on after the like a post.
"""


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.add_message(
                request, messages.ERROR, 'You have just unliked this post.')
        else:
            post.likes.add(request.user)
            messages.add_message(
                request, messages.SUCCESS, 'You have liked this post')

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
