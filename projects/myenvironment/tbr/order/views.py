from django.shortcuts import render, get_object_or_404
from .models import Order

# for order history course 24
from .models import OrderItem
from django.contrib.auth.decorators import login_required


def thanks(request, order_id):
	if order_id:
		customer_order = get_object_or_404(Order, id=order_id)
	return render(request, 'thanks.html', {'customer_order': customer_order})


# for order history course 24
# auth. decorators help to check the user is login or not. since the order list web page is a private page 
@login_required()
def orderHistory(request):
 	if request.user.is_authenticated:
 		email = str(request.user.email)
 		order_details = Order.objects.filter(emailAddress=email)
   
 # return the request, order list and the dictionary in this case is order details  
 	return render(request, 'order/orders_list.html', {'order_details':order_details})

 # for order detail course 24
@login_required()
def viewOrder(request, order_id):
	if request.user.is_authenticated:
		email = str(request.user.email)
		order = Order.objects.get(id=order_id, emailAddress=email)
		order_items = OrderItem.objects.filter(order=order)
	return render(request, 'order/order_detail.html', {'order':order, 'order_items':order_items})
