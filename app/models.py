from django.db import models

# Create your models here.
class Registration(models.Model):
    username=models.CharField(max_length=25)
    email=models.EmailField()
    password=models.CharField(max_length=25)
    confirm=models.CharField(max_length=25)
    fname=models.CharField(max_length=25)
    lname=models.CharField(max_length=25)
    gender=models.CharField(max_length=25)
    hobbies=models.CharField(max_length=25)
    country=models.CharField(max_length=25)
    address=models.TextField(max_length=125)
    class Meta:
        db_table="registration"
