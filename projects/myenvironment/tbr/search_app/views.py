from django.shortcuts import render
from shop.models import Product
from django.db.models import Q  # import Q core

def searchResult(request):
	products = None #  create variable called products
	query = None  # create variables called query 
	if 'q' in request.GET: # if Q is in the request.GET, 
		query = request.GET.get('q') # a value will be assigned to the query from q, from the request.GET
  
        #Explain the search function:
        # the products variable is going to be equal to the product model- product.obejct.all() with filter 
        # either the product name or the product description, thats why we are using q 
        # it is because the first condition we are going to apply with q is that if the name contains the query, it will show a result
        # the second condition is the description contains the query, it will return a result
        
		products = Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query) | Q(brand__contains=query) | Q(SKU__contains=query))
  
    # final step, to return the request on the search.html template, and render the dictionary values, in this
    # case, the query and the products on the search.html templates
	return render(request, 'search.html', {'query':query, 'products':products})