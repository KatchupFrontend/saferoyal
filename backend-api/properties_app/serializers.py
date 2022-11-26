from rest_framework import serializers
from . import models

class RoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(RoomListSerializer, self).__init__(*args, **kwargs)
    
class RoomDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = ['id','category', 'floortype', 'roomType', 'apartmentName', 'address', 'apartmentPrice']

    def __init__(self, *args, **kwargs):
         super(RoomDetailSerializer, self).__init__(*args, **kwargs)
        

 
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ['id','user', 'phone', 'fullname', 'email']

    def __init__(self, *args, **kwargs):
         super(CustomerSerializer, self).__init__(*args, **kwargs)
        

class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ['id','user', 'phone', 'fullname', 'email']

    def __init__(self, *args, **kwargs):
         super(CustomerDetailSerializer, self).__init__(*args, **kwargs)
        
