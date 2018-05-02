from django.db import models
from django.contrib.auth import get_user_model


User=get_user_model()

class Package(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,db_index=True,unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'package'
        verbose_name_plural = 'packages'
    def __str__(self):
        return self.name
class Product(models.Model):
    package = models.ForeignKey(Package,related_name='products')
    hospital=models.TextField(default=True)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        def __str__(self):
            return self.name
class Profile(models.Model):


    user=models.ForeignKey(User)
    number=models.IntegerField(default=True)
    product = models.ForeignKey(Product,related_name='product',default=True)

    def __str__(self):
        return self.bio
    @classmethod
    def my_profile(cls,user_id):
        profiles=Profile.objects.get(id=user_id)

        return profiles



# Create your models here.
# class User(models.Model):
#     name=models.TextField()
#     hospital=models.TextField()
#     user=models.ForeignKey(User)
#     def __str__(self):
