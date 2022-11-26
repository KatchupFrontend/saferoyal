from django.shortcuts import render
from rest_framework import generics,permissions
from . import serializers
from . import models
# Create your views here.

class RoomList(generics.ListCreateAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomListSerializer


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomDetailSerializer


class CustomerList(generics.ListCreateAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerListSerializer
    

