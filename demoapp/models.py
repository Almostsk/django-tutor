from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    price = models.IntegerField()
    
class Person(models.Model): 
    person_name = models.CharField(max_length=20) 
    email = models.EmailField() 
    phone = models.CharField(max_length=20) 
    
class Reservation(models.Model):
    name = models.CharField(max_length=100, blank=True)
    contact = models.CharField('Phone number', max_length=100)
    time = models.TimeField()
    count = models.IntegerField()
    notes = models.CharField(max_length=300, blank=True)
    
    def __str__(self):
        return self.name