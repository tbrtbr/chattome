from .models import Category
def menu_links(request):
	links = Category.objects.all() # get all the categories
	return dict(links=links) # dict = dictionary