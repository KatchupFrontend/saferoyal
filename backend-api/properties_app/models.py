from django.db import models
from django.contrib.auth.models import User

# Create your models here.


#Customer model
class Customer(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    fullname  = models.CharField(max_length=200)
    phone = models.PositiveBigIntegerField()
    email = models.EmailField(max_length=200, unique=True)
    def __str__(self):
        return self.user.username


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


    def __str__(self):
        return self.campusname

# #Floor Category
# class FloorCategory(models.Model):
#     floortype = models.CharField(max_length=10)


#Room model
class Room(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(CampusCategory, on_delete=models.SET_NULL, null=True)
    floortype = models.CharField(choices=(('1st', 'First'), ('2nd','Second'),('3rd', 'Third'), ('4th','Fourth'), ('5th', 'Fifth')), max_length=10)
    roomType = models.CharField(choices=( ('HOSTEL', "hostel"),
            ('HOMESTEL', "homestel"),
            ), max_length=10)
    
    apartmentName = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    apartmentPrice = models.DecimalField(max_digits=10, decimal_places=2)
    persons = models.CharField(choices=(('1 in 1', 'one in one'),( '2 in 1','Two in one'),( '3 in 1','Three in one'),( '4 in 1','Four in one')),max_length=100)
    description = models.TextField()
    apartmentImage = models.ImageField(upload_to='properties/images/')
    room1 = models.ImageField(upload_to='properties/images/')
    room2 = models.ImageField(upload_to='properties/images/')
    room3 = models.ImageField(upload_to='properties/images/')

    def __str__(self):
        return self.apartmentName




#Payment model
# class Payment(models.Model):
#     amount = models.CharField(max_length=20)
#     ref = models.CharField(max_length=20)
#     email = models.ForeignKey(max_length=20)
#     verified = models.BooleanField(default=False)
#     date_created = models.DateTimeField(auto_now_add=True)
#     phone = models.CharField(max_length=20)




#Booking model
class Book(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_booked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.fullname


# Booked Rooms
class Bookings(models.Model):
     booking = models.ForeignKey(Book, on_delete=models.CASCADE)
     room = models.ForeignKey(Room, on_delete=models.CASCADE)
     status = models.BooleanField( default=True )
     def __str__(self):
         return self.booking





   


