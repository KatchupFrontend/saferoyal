from django.db import models
from django.contrib.auth.models import User

# Create your models here.


#Customer model
class Customer(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    name  = models.CharField(max_length=200, null=True)
    phone = models.PositiveBigIntegerField()
    email = models.EmailField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name


# class Property(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     address = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     zipcode = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     bedrooms = models.IntegerField()
#     bathrooms = models.IntegerField()
#     guests = models.IntegerField()
#     check_in = models.TimeField()
#     check_out = models.TimeField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

    

#CampusCategory
class CampusCategory(models.Model):
    campusname = models.CharField(max_length=100)
    campuslocation = models.CharField(max_length=50)
    campuslogo = models.ImageField(upload_to='properties/images/')

#Floor Category
class FloorCategory(models.Model):
    floortype = models.CharField(max_length=10)


#Room model
class Room(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(CampusCategory, on_delete=models.SET_NULL, null=True)
    roomFloor = models.ForeignKey(FloorCategory, on_delete=models.SET_NULL,null=True)
    roomType = models.CharField(choices=( ('HOSTEL', "hostel"),
            ('HOMESTEL', "homestel"),
            ), max_length=1)
    apartmentName = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    apartmentPrice = models.DecimalField(max_digits=10, decimal_places=2)
    persons = models.CharField(max_length=10)
    description = models.TextField()
    apartmentImage = models.ImageField(upload_to='properties/images/')
    room1 = models.ImageField(upload_to='properties/images/')
    room2 = models.ImageField(upload_to='properties/images/')
    room3 = models.ImageField(upload_to='properties/images/')

    def __str__(self):
        return self.apartmentName




#Payment model
class Payment(models.Model):
    amount = models.CharField(max_length=20)
    ref = models.CharField(max_length=20)
    email = models.ForeignKey(Customer,max_length=20)
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=20)




#Booking model
class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    status = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.room.apartmentName




   


