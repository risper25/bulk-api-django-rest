from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50,unique=False)
    image=models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.name



class ProductVariant(models.Model):
    sku=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=100,decimal_places=2)
    details=models.TextField(max_length=200)
    product=models.ForeignKey(Product,related_name='variants',on_delete=models.CASCADE)
    def __str__(self):
        return self.name
