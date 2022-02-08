from django.db import models
from shop.models import Product

class Cart(models.Model):
	cart_id = models.CharField(max_length=250, blank=True)
	date_added = models.DateField(auto_now_add=True)
	class Meta:
		db_table = 'Cart'
		ordering = ['date_added']

	def __str__(self):
		return self.cart_id

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    SKU = models.CharField(max_length=250, blank=True) # new added, to show protail detail in cart items
    active = models.BooleanField(default=True)
    discount = models.FloatField(default=True) # input discount e.g 0.8
    discountcode = models.CharField(max_length=250, blank=True)
    giftcardnumber = models.CharField(max_length=250, blank=True, verbose_name='Gift Card Number')
    pricerule = models.DecimalField(max_digits=10, decimal_places=2, default = 0) # adjust the total price manually

    class Meta:
        db_table = 'CartItem'

    def sub_total(self): # calculate price * quantity 
        return self.product.price * self.quantity

    def __str__(self):
	    return self.product