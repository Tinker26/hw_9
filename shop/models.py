from django.db import models

# Create your models here.
class Krasofkalar(models.Model):

    name = models.CharField(max_length=300, db_index=True)
    image = models.CharField(max_length=400)
    price = models.IntegerField()
    old_price = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    class Meta:
        ordering = ['pk']
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name