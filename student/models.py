from django.db import models

# Create your models here.

class Contact(models.Model):
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.phone} {self.email}"

class Address(models.Model):
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street} {self.city} {self.country}"
    
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)
    Address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        f"{self.first_name} {self.last_name}"

    