from django.contrib import admin
from .models import Order, OrderItem

class OrderItemAdmin(admin.TabularInline):
	model = OrderItem
	fieldsets = [
	('Product',{'fields':['product'],}),
	('Quantity',{'fields':['quantity'],}),
	('Price',{'fields':['price'],}),
	]
	readonly_fields = ['product','quantity','price']
	can_delete= False # disappear the delete check box in the backend page
	max_num = 0 # remove the "Add another Order Item", that is bult-in function of the django backend
	template = 'admin/order/tabular.html' # tabular.html control the behaviour of the order item section on the order records

@admin.register(Order)  # use @adnmin to  register the order model
class OrderAdmin(admin.ModelAdmin):
	list_display = ['id','billingName','emailAddress','created']
	list_display_links = ('id','billingName')
	search_fields = ['id','billingName','emailAddress']
	readonly_fields = ['id','token','total','emailAddress','created','billingName','billingAddress1','billingCity',
					'billingPostcode','billingCountry','shippingName','shippingAddress1','shippingCity','shippingPostcode','shippingCountry']
	fieldsets = [
	('ORDER INFORMATION',{'fields': ['id','token','total','created']}),
	('BILLING INFORMATION', {'fields': ['billingName','billingAddress1','billingCity','billingPostcode','billingCountry','emailAddress']}),
	('SHIPPING INFORMATION', {'fields': ['shippingName','shippingAddress1','shippingCity','shippingPostcode','shippingCountry']}),
	]

    # to see the order items in order records, need to add the order item admin as part of the order admin class

	inlines = [
		OrderItemAdmin,
	]

    # isable the delete button as the order can just be deleted in the backend

	def has_delete_permission(self, request, obj=None):
		return False

    # order can not be added in the backend
	def has_add_permission(self, request):
		return False

