from django.contrib import admin

# Register your models here.
from .models import Category, Product
# Register your models here.
# admin.site.register(Category)
# admin.site.register(Product)

class CategoryAdmin(admin.ModelAdmin):
   list_display=['id' ,'name', 'slug','description']
   prepopulated_fields = {'slug': ('name',)}
   Ordering=['name']
   list_display_links = ('id','name')
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
   list_display=['id' ,'name', 'slug','stock']
   prepopulated_fields ={'slug':('name',)}
   list_editable = ['stock',]

admin.site.register(Product,ProductAdmin)