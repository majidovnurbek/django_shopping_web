from django.db import models
from django.contrib.auth.models import AbstractUser


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name


class Home_products(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name


class home_picture(models.Model):
    image = models.ImageField(upload_to='images')


class conatact_us(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email


class contact_info(models.Model):
    image = models.ImageField(upload_to='images')
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.email


class about_team(models.Model):
    image = models.ImageField(upload_to='images')
    full_name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name


class Users(AbstractUser):
    ...
