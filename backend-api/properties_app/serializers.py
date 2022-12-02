from rest_framework import serializers
from . import models

class RoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = ['id','category', 'floortype', 'roomType','persons', 'apartmentName', 'address', 'apartmentPrice','apartmentImage','room1','room2','room3']

    def __init__(self, *args, **kwargs):
        super(RoomListSerializer, self).__init__(*args, **kwargs)
    
class RoomDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = ['id','category','description','persons', 'floortype', 'roomType', 'apartmentName', 'address', 'apartmentPrice','apartmentImage','room1','room2','room3']


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
        

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ['id','customer', 'date_booked']

    def __init__(self, *args, **kwargs):
        super(BookSerializer, self).__init__(*args, **kwargs)


class BookingDetailSerializer(serializers.ModelSerializer):
     class Meta:
         model = models.Bookings
         fields = ['id','room', 'booking', 'status']

     def __init__(self, *args, **kwargs):
          super(BookingDetailSerializer, self).__init__(*args, **kwargs)
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CampusCategory
        fields = ['id','campusname', 'campuslocation','campuslogo']


    def __init__(self, *args, **kwargs):
        super(CategorySerializer, self).__init__(*args, **kwargs)


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CampusCategory
        fields = ['id','campusname', 'campuslocation', 'campuslogo']

    def __init__(self, *args, **kwargs):
         super(CategoryDetailSerializer, self).__init__(*args, **kwargs)
