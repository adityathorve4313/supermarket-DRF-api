from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=True, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='market', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    item_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Category = models.ForeignKey(Category, to_field='name', on_delete=models.CASCADE)
    
    