from django.db import models

# Create your models here.

class Person(models.Model):
	person_id = models.AutoField(primary_key=True);
	name = models.CharField(max_length = 90);
	age = models.PositiveIntegerField();

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

class Store(models.Model):
	store_id = models.AutoField(primary_key=True);
	inventory = models.ManyToManyField(Beer);
	location = models.CharField(max_length = 100);
	name = models.CharField(max_length = 100);

class Order(models.Model):
	order_id = models.AutoField(primary_key=True);
	buyer = models.ForeignKey(Person);
	item = models.ForeignKey(Beer);

class Trip(models.Model):
	trip_id = models.AutoField(primary_key=True);
	runner = models.ForeignKey(Person, related_name = 'runner_person');
	buyers = models.ManyToManyField(Person);
	store = models.ForeignKey(Store);
	time_created = models.DateTimeField(auto_now_add = True);
	active = models.BooleanField();
	orders = models.ManyToManyField(Order);


