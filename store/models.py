from django.db import models

# Create your models here.


class Category(models.Model):
    
    name = models.CharField(max_length=250, db_index=True)

    slug = models.SlugField(max_length=250, unique=True)

    
    class Meta:
        
        verbose_name_plural = 'categories'
    
    
    def __str__(self):
        
        return self.name


class Brand(models.Model):
    
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name



class Product(models.Model):

    name = models.CharField(max_length=250)

    brand = models.ForeignKey('Brand', 
            on_delete=models.CASCADE, 
            null=True, 
            default='nobrand'
    )

    description = models.TextField(blank=True)

    slug = models.SlugField(max_length=250, unique=True)

    price = models.DecimalField(max_digits=5, decimal_places=2)

    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name