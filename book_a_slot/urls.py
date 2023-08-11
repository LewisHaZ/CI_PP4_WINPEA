# Imports
# 3rd Party
from django.urls import path

# Internal
from book_a_slot import views

urlpatterns = [
    path('visit_store/', views.Reservations.as_view(), name='visit_store'),
    path('slot_confirmed/', views.Confirmed.as_view(), name='slot_confirmed'),
    path('booking_list/', views.BookingList.as_view(), name='booking_list'),
    path('edit_booking/<int:pk>/', views.EditBooking.as_view(
    ), name='edit_booking'),
]
