from django import forms
# from . import getAllStoresList


class LoginForm(forms.Form):
	username = forms.CharField(max_length = 16)
	password = forms.CharField(max_length = 16)

class SignUpForm(forms.Form):
	username = forms.CharField(max_length = 16)
	password = forms.CharField(max_length = 16)
	name = forms.CharField(max_length = 90)
	age = forms.IntegerField(min_value = 21)

class SearchForm(forms.Form):
	query = forms.CharField(max_length = 100)

class TripForm(forms.Form):
	#allStores = getAllStoresList()
	def __init__(self,*args,**kwargs):
		self._errors = None
		self.is_bound = None
		self.fields = ('store')
		self.allStores = kwargs.pop("allStores")
		super(TripForm,self).__init__(*args,**kwargs)
		self.fields['store'] = forms.ChoiceField(choices = self.allStores)

class TripCreate(forms.Form):

	def __init__(self,*args,**kwargs):
		store = "Blank"
		if 'store' in kwargs:
			store = kwargs.pop("store")
		self._errors = None
		self.is_bound = None
		self.fields = ('store')
		super(TripCreate,self).__init__(*args,**kwargs)
		self.fields['store'] = store

class OrderForm(forms.Form):
	def __init__(self, *args, **kwargs):
		self._errors = None
		self.is_bound = None
		self.fields = ('beer')
		self.allBeers = kwargs.pop("allBeers")
		self.allTrips = kwargs.pop('allTrips')
		super(OrderForm, self).__init__(*args, **kwargs)
		self.fields['beer'] = forms.ChoiceField(choices = self.allBeers)
		self.fields['trip'] = forms.ChoiceField(choices = self.allTrips)

class OrderCreate(forms.Form):
	def __init__(self, *args, **kwargs):
		beer = "Blank"
		if 'beer' in kwargs:
			beer = kwargs.pop("beer")
		if 'trip' in kwargs:
			trip = kwargs.pop("trip")
		self._errors = None
		self.is_bound = None
		self.fields = ('beer')
		super(OrderCreate, self).__init__(*args, **kwargs)
		self.fields['beer'] = beer
		self.fields['trip'] = trip
    
