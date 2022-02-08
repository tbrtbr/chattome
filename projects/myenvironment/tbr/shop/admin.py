from django.contrib import admin

# Register your models here.


# add shop models Category and Products
from .models import Category,Product,CustomerProfile,StockPurchaseOrder,TestOrder


# Modify Name of Admin Site
admin.site.site_header = 'Chat To Me Administration'


# add shop models Category and Products
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name','publishedAt'] # name and the slug of category
	prepopulated_fields = {'slug':('name',)} #assign the value of the name field and the slug field
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name','SKU','price','stock','available','created','updated']
	list_editable = ['price','stock','available']
	prepopulated_fields = {'slug':('name',)}
	list_per_page = 20         # means that 20 products will list out per page
admin.site.register(Product,ProductAdmin)

class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ['name']
	#list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20         # means that 20 products will list out per page

admin.site.register(CustomerProfile,CustomerProfileAdmin)

class StockPurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ['PONumber','productSKU','productTitle','qty','cost','confirmPO','created']
    list_editable = ['confirmPO']
    prepopulated_fields = {'slug':('PONumber',)}
    list_per_page = 20         # means that 20 products will list out per page
admin.site.register(StockPurchaseOrder,StockPurchaseOrderAdmin)

class TestOrderAdmin(admin.ModelAdmin):
    list_display = ['name']
    #list_editable = ['name']
    # prepopulated_fields = {'slug':('PO_Number',)}
    list_per_page = 20         # means that 20 products will list out per page
admin.site.register(TestOrder,TestOrderAdmin)