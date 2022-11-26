from django.contrib import admin
from .models import CampusCategory,Book, Room, Customer
# Register your models here.
admin.site.register(Room)
admin.site.register(CampusCategory)
admin.site.register(Customer)
admin.site.register(Book)



