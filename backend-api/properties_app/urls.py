from django.urls import path
from .import views


urlpatterns = [
    path('rooms/', views.RoomList.as_view()),
     path('room/<int:pk>/', views.RoomDetail.as_view()),

]

