# 3rd Party Imports
from django.urls import path

# Internal
from . import views

urlpatterns = [
    path('blog/', views.PublishedPosts.as_view(), name='blog'),
]