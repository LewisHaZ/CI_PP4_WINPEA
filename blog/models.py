# 3rd Party Imports
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Posted'))


class Post(models.Model):
    """
    A class for setting up the fields for the post
    model and each field type/key.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    post_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    created_date = models.DateTimeField(blank=True)
    updated_date = models.DateTimeField()
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
   
    class Meta:
        """
        A class to order the comments by
        the date they were created.
        """
        ordering = ['-created_date']

    def __str__(self):
        """
        Returns self
        """
        return self.title


class Comment(models.Model):
    """
    A class for the comment model, this will take
    various fields and values both from the user
    and by the user.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'

