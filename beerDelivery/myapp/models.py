from django.db import models
from django.urls import reverse

# Create your models here.

class Person(models.Model):
	person_id = models.AutoField(primary_key=True);
	name = models.CharField(max_length = 90);
	age = models.PositiveIntegerField();

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
	#inventory = models.ManyToManyField(Beer);
	inventory = models.CharField(max_length = 100)
	location = models.CharField(max_length = 100)
	name = modelsCharField(max_length = 100)

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
	store = models.ForeignKey(Store);
	time_created = models.DateTimeField(auto_now_add = True);
	active = models.BooleanField();
	orders = models.ManyToManyField(Order);

	def __str__(self):
	    """
	    String for representing the Model object (in Admin site etc.)
	    """
	    return str(self.trip_id)

	def get_absolute_url(self):
		return reverse('trip_get', args=[str(self.trip_id)])





