from .models import Category

# to show categrories in the website

def menu_links(request):
	links = Category.objects.all() # get all the categories
	return dict(links=links) # dict = dictionary