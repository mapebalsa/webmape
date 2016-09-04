import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mape_web.settings')

import django
django.setup()

from mape_1.models import Category, Page, Product
from django.template.defaultfilters import slugify



def populate():
    madera_cat = add_cat('Varillas')

    add_product(cat=madera_cat,
         name= "Varilla_10x10x100",
         price= 50.00)
    add_product(cat=madera_cat,
         name= "Varilla_20x10x100",
         price= 60.00)    

    add_product(cat=madera_cat,
         name= "Varilla_30x10x100",
         price= 70.00)

    add_product(cat=madera_cat,
         name= "Varilla_40x10x100",
         price= 80.00)            
        
    madera_cat = add_cat('Tablas')

    add_product(cat=madera_cat,
        name="Tabla_12x120x1",
        price= 150.03)
    
    add_product(cat=madera_cat,
        name="Tabla_22x120x1",
        price= 250.03)
    
    add_product(cat=madera_cat,
        name="Tabla_32x120x1",
        price= 350.03)
        
  
    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Product.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_product(cat, name, price, quantity=14):
    p = Product.objects.get_or_create(category=cat, name=name)[0]
    p.price=price
    p.quantity=quantity
    p.slug = slugify(name)
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.slug = slugify(name)

    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()
