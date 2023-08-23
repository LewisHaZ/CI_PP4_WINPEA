# 3rd Party
from django.urls import path
# Internal
from contactus import views

urlpatterns = [
    path('contactus/', views.Contact.as_view(), name='contactus'),
]