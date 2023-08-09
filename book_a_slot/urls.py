# Imports
# 3rd Party
from django.urls import path

# Internal
from book_a_slot import views

urlpatterns = [
    path('visit_store/', views.visit_store, name='visit_store'),
]