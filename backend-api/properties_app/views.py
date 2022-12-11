from urllib import response
from django.shortcuts import render
from rest_framework import generics,permissions, viewsets
from . import serializers
from django.http import HttpResponse, Http404
from . import models

# Create your views here.


class RoomList(generics.ListCreateAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomListSerializer

    def get_queryset(self):
        category = self.request.GET.get('category')
        category = models.CampusCategory.objects.get(id=category)
        return models.Room.objects.filter(category=category)


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


class PaymentView(generics.CreateAPIView):
    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer


class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentDetailSerializer
