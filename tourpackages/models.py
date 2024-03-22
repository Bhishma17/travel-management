from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    class Meta:
        db_table="Register"

class contactus(models.Model):
    firstname = models.TextField(max_length=255)
    lastname = models.TextField(max_length=255)
    email = models.EmailField(primary_key = True)
    comments = models.TextField(max_length=255)
    class Meta:
        db_table="contactus"

class RentCar(models.Model):
    location1 = models.CharField(primary_key=True, max_length=255)
    from_date_value = models.DateField()
    to_date_value = models.DateField()

    class Meta:
        db_table = "rentcar"

