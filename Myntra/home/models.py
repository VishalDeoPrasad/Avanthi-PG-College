from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='products/')  # ✅ Pillow required

    def __str__(self):
        return self.name
