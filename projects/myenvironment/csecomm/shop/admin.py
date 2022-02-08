from django.contrib import admin

# Register your models here.

# add shop models Category and Products
from .models import Category,Product




# add shop models Category and Products
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name','slug'] # name and the slug of category
	prepopulated_fields = {'slug':('name',)} #assign the value of the name field and the slug field
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name','price','stock','available','created','updated']
	list_editable = ['price','stock','available']
	prepopulated_fields = {'slug':('name',)}
	list_per_page = 20         # means that 20 products will list out per page
admin.site.register(Product,ProductAdmin)

