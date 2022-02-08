from django.db import models
from django.urls import reverse
from django.forms import ModelForm

STATUS_CHOICES = [
    ('ACTIVE', 'active'),
    ('ARCHIVED', 'archived'),
    ('DRAFT', 'draft'),
]

class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)# it will get the url path that the visitor request in the broswer
    CatID = models.CharField(max_length=250, blank=True)  
    #SKU = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)# set upload to category
    publishedAt = models.DateTimeField(auto_now=True,verbose_name='Published At')
    pulbishedOnlyWeb = models.BooleanField(default=False, verbose_name='Published Only Web')
    updated = models.DateTimeField(auto_now=True)
    remarks = models.TextField(blank=True)

    class Meta: # define option of this model
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self): # reverse to show categories in website, course 8
        return reverse('shop:products_by_category', args=[self.slug])
    
    def __str__(self):
        return '{}'.format(self.name)

class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    SKU = models.CharField(max_length=250, blank=True)
    brand = models.CharField(max_length=250, blank=True)
    vendor = models.CharField(max_length=250, blank=True)		
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Retail Price')
    image = models.ImageField(upload_to='product', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, blank=True)
    publishedAt = models.DateTimeField(auto_now=True, verbose_name='Published At')
    pulbishedOnlyWeb = models.BooleanField(default=False, verbose_name='Published Only Web')
    customerFeedback = models.TextField(blank=True, verbose_name='Customer Feedback')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    remarks = models.TextField(blank=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_url(self):#adde in course 9, to get the product detail to show in the website
        return reverse('shop:ProdCatDetail', args=[self.category.slug, self.slug])
 
    def __str__(self):
	    return '{}'.format(self.name)
 
 
class CustomerProfile(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    nickname = models.CharField(max_length=250, blank=True)
    Interests = models.TextField(blank=True)
    #category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product', blank=True)
    #stock = models.IntegerField()
    #available = models.BooleanField(default=True)
    favouriteFashionStyle = models.TextField(blank=True, verbose_name='FashionStyle')
    favouriteFlavour = models.TextField(blank=True, verbose_name='Flavour')
    favouritBrand = models.TextField(blank=True, verbose_name='Brand')
    favouriteGameRelated = models.TextField(blank=True, verbose_name='Game related')
    favouriteMovieSerialsRelated = models.TextField(blank=True, verbose_name='Movie Serial related')
    favouriteBooksRelated = models.TextField(blank=True, verbose_name='Books related')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    remarks = models.TextField(blank=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'customer_Profile'
        verbose_name_plural = 'customer_Profiles' #showing the name at Shop at Site administration page

	#def get_url(self):
	#	return reverse('shop:ProdCatDetail', args=[self.category.slug, self.slug])
 
    def __str__(self):
	    return '{}'.format(self.name)
 
class StockPurchaseOrder(models.Model):
    name = models.CharField(max_length=250, unique=True, blank=True)
    PONumber = models.CharField(max_length=250, unique=True, verbose_name='PO Number')
    slug = models.SlugField(max_length=250, unique=True)
    productSKU = models.CharField(max_length=250, blank=True, verbose_name='Product SKU')
    qty = models.IntegerField(verbose_name='QTY')
    cost = models.DecimalField(max_digits=10, decimal_places=2) #cost per PO
    productTitle = models.CharField(max_length=250, blank=True, verbose_name='Product Title')
    POImage = models.ImageField(upload_to='product', blank=True, verbose_name='PO Image')
    PIImage = models.ImageField(upload_to='product', blank=True, verbose_name='PI Image')
    GRNImage = models.ImageField(upload_to='product', blank=True, verbose_name='Goods Received Note GRN Image')
    VendorInvoice = models.ImageField(upload_to='product', blank=True, verbose_name='Vendor Invoice')
    VendorReceipt = models.ImageField(upload_to='product', blank=True, verbose_name='Vendor Receipt')
    logisticVendor = models.CharField(max_length=250, blank=True, verbose_name='Logistic Vendor')
    logisticCost = models.CharField(max_length=250, blank=True, verbose_name='Logistic Cost')
    logisticInvoice = models.ImageField(upload_to='product', blank=True, verbose_name='Logistic Invoice')
    logisticReceipt = models.ImageField(upload_to='product', blank=True, verbose_name='Logistic Receipt')	
    confirmPO = models.BooleanField(default=False, verbose_name='Confirm PO')
    confirmPODate = models.DateTimeField(auto_now=True, verbose_name='Confirm PO Date')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    remarks = models.TextField(blank=True)
    
    class Meta:
        ordering = ('PONumber',)
        verbose_name = 'Stock Purchase Order'
        verbose_name_plural = 'Stock Purchase Orders' #showing the name at Shop at Site administration page

	#def get_url(self):
	#	return reverse('shop:ProdCatDetail', args=[self.category.slug, self.slug])
 
    def __str__(self):
	    return '{}'.format(self.name)
    
    '''
    #generate new product or update stock automatically
    def save(self, *args, **kwargs):
        # Product.objects.create()
        testObj = TestOrder(name='test27s')
        
     
        if not self._state.adding and (
            self.creator_id != self._loaded_values['creator_id']):
            raise ValueError("Updating the value of creator isn't allowed")
        testObj.save()
        super().save(*args, **kwargs)
    '''

        


class TestOrder(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, unique=True)
    # slug = models.SlugFJield(max_length=250, unique=True)
    
    class Meta:
        ordering = ('id',)
        verbose_name = 'test_Order'
        verbose_name_plural = 'test_Order' #showing the name at Shop at Site administration page

	#def get_url(self):
	#	return reverse('shop:ProdCatDetail', args=[self.category.slug, self.slug])
 
    def __str__(self):
	    return '{}'.format(self.name)