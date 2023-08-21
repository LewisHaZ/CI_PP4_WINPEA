# 3rd Party Imports
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.core.paginator import Paginator

# Internal 
from .models import Post


class PublishedPosts(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_date')
    template_name = 'blog.html'
    paginated_by = 4

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        paginator = Paginator(Post.objects.all(), 4)
        page = request.GET.get('page')
        postings = paginator.get_page(page)

        return render(
            request, 'blog/blog.html', {'posts': posts, 'postings': postings}
        )


class PostExpand(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(
            approved=True).order_by('-created_date')

        return render(
            request, 'blog/blog_expand.html',
            {'post': post,
             'comments': comments,
             'commented': False,
             'comment_form': CommentForm()
             }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(
            approved=True).order_by('-created_date')

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request, 'blog/blog_expand.html',
            {'post': post,
             'comments': comments,
             'commented': True,
             'comment_form': CommentForm()
             }
        )
