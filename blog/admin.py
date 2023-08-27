# 3rd Party Imports
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Internal
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    A class for the Post Admin that will
    be able to control content on the
    Blog page
    """

    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
    list_filter = ('status', 'created_date')
    list_display = ('title', 'slug', 'status', 'created_date')
    search_fields = ['title', 'content']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    A class for the Comment Admin that will
    be able to control content on the
    Blog page
    """

    list_filter = ('approved', 'created_date')
    list_display = ('name', 'body', 'post', 'created_date', 'approved')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):

        queryset.update(approved=True)
