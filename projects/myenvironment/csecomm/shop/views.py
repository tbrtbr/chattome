from django.shortcuts import render, get_object_or_404,redirect #add redirect for signin
from django.http import HttpResponse
from .models import Category,Product

# for paginator
from django.core.paginator import Paginator, EmptyPage, InvalidPage

#for register user account
from django.contrib.auth.models import Group, User
from .forms import SignUpForm

#for sign in
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout


#test fumction for web page
def index(request):
	text_var = 'This is my first django app web page.'
	return HttpResponse(text_var)


#Category view

def allProdCat(request, c_slug=None):
	c_page = None # Category page
	products_list = None # product list page
	if c_slug!=None:
		c_page = get_object_or_404(Category,slug=c_slug)
		products_list = Product.objects.filter(category=c_page,available=True)
	else:
		products_list = Product.objects.all().filter(available=True)

	'''Pagination code'''
	paginator = Paginator(products_list, 6) # limited to list 6 products only
	try:
		page = int(request.GET.get('page','1')) # request to get the page no. one
	except:
		page = 1
	try:
		products = paginator.page(page) # get the page no. 1 
	except (EmptyPage,InvalidPage):
		products = paginator.page(paginator.num_pages) # this method to get the total number of pages

	return render(request,'shop/category.html',{'category':c_page,'products':products})

def ProdCatDetail(request,c_slug,product_slug):
	try:
		product = Product.objects.get(category__slug=c_slug,slug=product_slug)
	except Exception as e:
		raise e
	return render(request,'shop/product.html', {'product':product})


# for sign up view


def signupView(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			signup_user = User.objects.get(username=username)
			customer_group = Group.objects.get(name='Customer')
			customer_group.user_set.add(signup_user)
	else:
		form = SignUpForm()
	return render(request, 'accounts/signup.html', {'form':form})


def signinView(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('shop:allProdCat')
			else:
				return redirect('signup')
	else:
		form = AuthenticationForm()
	return render(request,'accounts/signin.html', {'form':form })

def signoutView(request):
	logout(request)
	return redirect('signin')