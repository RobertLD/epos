from django.db import models  
from django.contrib.auth.models import User

class Restaurant(models.Model):          
    name = models.CharField(max_length=50)          
    address = models.CharField(max_length=80)          
    phoneNumber = models.CharField(max_length=10)      

    def __str__(self): 
        return "%s the place" % self.name   

class Menu(models.Model):          
    restaurant = models.OneToOneField(Restaurant,on_delete=models.CASCADE,primary_key=True)

class Section(models.Model):
    name = models.CharField(max_length=50)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

class Product(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    image = models.FileField(upload_to='img')
    price = models.IntegerField(default = 0)

    def __str__(self):
	    return self.name

class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'customer', null=True, blank=True)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
		
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 
