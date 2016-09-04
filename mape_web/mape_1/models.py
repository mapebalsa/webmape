from django.template.defaultfilters import slugify
#from __future__ import unicode_literals
from django.db import models
from decimal import Decimal


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):  #For Python 2, use __str__ on Python 3
       self.slug = slugify(self.name)
       super(Category, self).save(*args,**kwargs)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, help_text='Unique value for product page URL, created from name.')
    brand = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9,decimal_places=2, default=Decimal(0))
    old_price = models.DecimalField(max_digits=9,decimal_places=2, blank=True, default=Decimal(0))
    #image = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/images/products/main')
    thumbnail = models.ImageField(upload_to='static/images/products/thumbnails')
    image_caption = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    description = models.TextField()
    #meta_keywords = models.CharField(max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag')
    #meta_description = models.CharField(max_length=255, help_text='Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #categories = models.ManyToManyField(Category)
    category = models.ForeignKey(Category)
    #category = models.ForeignKey(Category, default= Category.objects.get_or_create(name="sin_categoria"))
    def __unicode__(self):      #For Python 2, use __str__ on Python 3
            return self.name    



