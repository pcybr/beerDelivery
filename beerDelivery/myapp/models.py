from django.db import models
from django.urls import reverse

# Create your models here.

class Person(models.Model):
	person_id = models.AutoField(primary_key=True);
	name = models.CharField(max_length = 90);
	age = models.PositiveIntegerField();
	username = models.CharField(max_length = 16, default="Username")
	password = models.CharField(max_length = 254, default="Password")

	def __str__(self):
	    """
	    String for representing the Model object (in Admin site etc.)
	    """
	    return self.name
    
	def get_absolute_url(self):
		return reverse('person_get', args=[str(self.person_id)])


class Beer(models.Model):
	TOPS = (
		('Twist-Off', 'Twist-Off'),
		('Pop-Off', 'Pop-Off'),
		('Can', 'Can'),
	)
	TYPES = (
        ('IPA', 'IPA'),
        ('Light', 'Light'),
        ('Lager', 'Lager'),
        ('Ale', 'Ale'),
        ('Non-Alcoholic', 'Non-Alcoholic')
    )
	beer_id = models.AutoField(primary_key=True);
	size = models.PositiveIntegerField();
	name = models.CharField(max_length = 100);
	price = models.PositiveIntegerField();
	beer_type = models.CharField(verbose_name = 'Beer Type', choices = TYPES, max_length = 30);
	bottle_type = models.CharField(verbose_name = 'Bottle Type', choices = TOPS, max_length = 30);

	def __str__(self):
	    """
	    String for representing the Model object (in Admin site etc.)
	    """
	    return self.name

	def get_absolute_url(self):
		return reverse('beer_get', args=[str(self.beer_id)])


class Store(models.Model):
	store_id = models.AutoField(primary_key=True)
	inventory = models.ManyToManyField(Beer, blank = True);
	# inventory = models.CharField(max_length = 100,default = "None")
	location = models.CharField(max_length = 100)
	name = models.CharField(max_length = 100)

	def __str__(self):
	    """
	    String for representing the Model object (in Admin site etc.)
	    """
	    return self.name

	def get_absolute_url(self):
		return reverse('store_get', args=[str(self.store_id)])


class Order(models.Model):
	order_id = models.AutoField(primary_key=True);
	buyer = models.ForeignKey(Person);
	item = models.ForeignKey(Beer);
	order_trip = models.ForeignKey('Trip')

	def __str__(self):
	    """
	    String for representing the Model object (in Admin site etc.)
	    """
	    return str(self.order_id)

	def get_absolute_url(self):
		return reverse('order_get', args=[str(self.order_id)])

 
class Trip(models.Model):
	trip_id = models.AutoField(primary_key=True);
	runner = models.ForeignKey(Person, related_name = 'runner_person');
	store = models.ForeignKey(Store, default=1);
	time_created = models.DateTimeField(auto_now_add = True);
	active = models.BooleanField();
	# orders = models.ManyToManyField(Order, default = None, blank = True);

	def __str__(self):
	    """
	    String for representing the Model object (in Admin site etc.)
	    """
	    return str(self.trip_id)

	def get_absolute_url(self):
		return reverse('trip_get', args=[str(self.trip_id)])


class Authenticator(models.Model):
	user_id = models.PositiveIntegerField()
	auth = models.CharField(primary_key=True,max_length=254)
	date_created = models.DateTimeField(auto_now_add = True)
	name = models.CharField(max_length=16,default="")

class Recommendation(models.Model):
	item_id = models.PositiveIntegerField()
	recommended_trips = models.CharField(max_length=256)
	