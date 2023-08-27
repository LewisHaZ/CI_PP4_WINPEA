# 3rd Party Imports
from django.urls import path
# Internal
from contactus import views

urlpatterns = [
    path('contactus/', views.ContactMessage.as_view(), name='contactus'),
]
