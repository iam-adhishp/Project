from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='Product_images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image1 = models.ImageField(upload_to='Product_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='Product_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='Product_images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='Product_images/', blank=True, null=True)
    image5 = models.ImageField(upload_to='Product_images/', blank=True, null=True)
    image6 = models.ImageField(upload_to='Product_images/', blank=True, null=True)
    def __str__(self):
        return self.name


