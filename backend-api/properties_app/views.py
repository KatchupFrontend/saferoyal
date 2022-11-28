from django.shortcuts import render
from rest_framework import generics,permissions
from . import serializers
from . import models
# Create your views here.

class RoomList(generics.ListCreateAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomListSerializer

    def get_queryset(self):
        qs=super().get_queryset()
        category=self.request.GET['category']
        category=models.CampusCategory.objects.get(id=category)
        qs=qs.filter(category=category)
        return qs
    
    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     category=self.request.GET['category']
    #     category=models.CampusCategory.objects.get(id=category)
    #     qs=qs.filter(category=category)
    #     # return qs

class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomDetailSerializer
    






class CustomerList(generics.ListCreateAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerDetailSerializer

class BookList(generics.ListCreateAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer


class BookingDetail(generics.ListAPIView):
#     # queryset = models.BookedRoom.objects.all()
      serializer_class = serializers.BookingDetailSerializer

      def get_queryset(self):
         booking_id = self.kwargs['pk']
         booking = models.Bookings.objects.get(id=booking_id)
         book_items = models.Bookings.objects.filter(booking=booking)
         return book_items

class CategoryList(generics.ListCreateAPIView):
    queryset = models.CampusCategory.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CampusCategory.objects.all()
    serializer_class = serializers.CategoryDetailSerializer

