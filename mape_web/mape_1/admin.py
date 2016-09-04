from django.contrib import admin
from .models import Category, Page, Product

class CategoryAdmin(admin.ModelAdmin):
	prepopulate_fields = {'slug':('name',)}

admin.site.register(Product)
admin.site.register(Page)
admin.site.register(Category, CategoryAdmin)
# Register your models here.
