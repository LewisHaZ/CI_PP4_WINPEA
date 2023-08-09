# Imports 
# 3rd Party
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('home.urls')),
    path('', include('item_catalogue.urls')),
    path('', include('book_a_slot.urls')),
    path('accounts/', include('allauth.urls')),
]
