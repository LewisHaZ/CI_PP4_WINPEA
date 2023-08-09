# Imports 
# 3rd Party
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('home.urls'), name='home_urls'),
    path('', include('item_catalogue.urls'), name='catalogue_urls'),
]
