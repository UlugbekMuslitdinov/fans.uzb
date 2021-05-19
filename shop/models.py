import os
from django.db import models
from django.db.models import indexes
from django.urls import reverse
import datetime
from django.utils import timezone
# Create your models here.

def get_upload_path(instance, filename):
    #  задаем название файла названием slug`а продукта
    filename = instance.slug + '.' + filename.split('.')[1]  
    return os.path.join('images/', filename)


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover = models.CharField(max_length=500, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['slug'], name='slug_index'),
        ]
        ordering = ('name',)
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:category_detail', args=[self.slug])


class Measurement(models.Model):
    name = models.CharField(max_length=50, db_index=True) 

    def __str__(self) -> str:
        return self.name   
    
    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'




class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products', 
        on_delete=models.CASCADE
        )
    measurement = models.ForeignKey(Measurement, related_name='measurement', null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.CharField(max_length=500, null=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        indexes = [
            models.Index(fields=['id'], name='id_index'),
        ]
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
    
    def was_added_recently(self):
        return self.created_at >= (timezone.now() - datetime.timedelta(days=7))
    
class Banner:
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to=get_upload_path)

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'


    def __str__(self):
        return self.name
