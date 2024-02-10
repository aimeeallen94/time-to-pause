from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    This class lays out how the post form will be
    laid out in the admin panel as well as what field
    types they will be.
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    This class lays out how the comment form
    will appear in the admin panel as well as
    what field type each of them will be.
    """

    list_display = ('post', 'author', 'content', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['author', 'content']
    action = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
