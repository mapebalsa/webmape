from django.http import HttpResponse
from django.shortcuts import render
from .models  import Category
from .models  import Product

def index(request):
	lista_categorias  = Category.objects.order_by('-id')[:5]
	context_dict = {'categorias': lista_categorias }


#	return HttpResponse("alojaja")
	return render(request, 'mape_1/index.html', context_dict)	

def category(request):
 context_dict = {} 
 lista_categorias  = Category.objects.order_by('-id')[:5]
 lista_productos  = Product.objects.order_by('-id')[:5]
 context_dict ['categorias'] = lista_categorias 
 
 context_dict ['productos'] = lista_productos 
 tablas = Category.objects.get(name="Tablas")
 context_dict ['productos_tablas'] = Product.objects.filter(category=tablas)
 
 varillas = Category.objects.get(name="Varillas")
 context_dict ['productos_varillas'] = Product.objects.filter(category=varillas)

 
 return render(request, 'mape_1/productos.html', context_dict)	
 
# def category(request):
	# context_dict = {} 
	# try:
		# lista_category = Product.objects.order_by('-id')
		# context_dict['category_name'] = category.name
#		context_dict['category_name_slug'] = category.slug

		# productos = Page.objects.filter(category = category)
		# context_dict['pages'] = page
		# context_dict['category'] = category

#		return HttpResponse("alojaja")u
	# except Category.DoesNotExist:
		# pass

	# return render(request, 'mape_1/productos.html', context_dict)
	
