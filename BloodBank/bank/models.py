from django.db import models
from django.contrib.auth.models import User
# Create your models here.

gender_choices = (
    ('Male','Male'),
    ('Female','Female'),
)

blood_choices = (
    ('A+','A+'),
    ('B+','B+'),
    ('AB+','AB+'),
    ('O+','O+'),
    ('A-','A-'),
    ('B-','B-'),
    ('AB-','AB-'),
    ('O-','O-'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Mobile = models.DecimalField(max_digits=10, decimal_places=0)
    Gender = models.CharField(max_length=6, choices=gender_choices, default='Male')
    Dob = models.DateField()
    Blood_group = models.CharField(max_length=3, choices=blood_choices, default='A+')
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Zip_code = models.CharField(max_length=6)
    Blood_Donated = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username

class BloodStock(models.Model):
    Blood_group = models.CharField(max_length=3, choices=blood_choices, default='A+')
    Blood_Stock = models.IntegerField(default=0)
    def __str__(self):
        return self.Blood_group+"( "+str(self.Blood_Stock)+"ml )"