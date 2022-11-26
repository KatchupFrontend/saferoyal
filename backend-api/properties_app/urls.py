from django.urls import path
from .import views


urlpatterns = [
    path('rooms/', views.RoomList.as_view()),
    path('room/<int:pk>/', views.RoomDetail.as_view()),

    path('categories/', views.CategoryList.as_view()),
    path('category/<int:pk>/', views.CategoryDetail.as_view()),
    
    path('customers/', views.CustomerList.as_view()),
     path('customer/<int:pk>/', views.CustomerDetail.as_view()),
     path('bookings/', views.BookList.as_view()),
    path('booking/<int:pk>/', views.BookingDetail.as_view()),

    # path('booking/<int:pk>/', views.BookingDetail.as_view()),


]

