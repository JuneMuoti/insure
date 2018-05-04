from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='profiles')
    birth_date = models.DateField()
    phone_number = PhoneNumberField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.phone_number

class Product(models.Model):
    dependants = models.CharField(max_length=30)
    package = models.CharField(max_length=30)
    limit = models.IntegerField()
    hospital = models.CharField(max_length=30)
    created = models.DateField(auto_now_add=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.premium