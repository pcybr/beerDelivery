from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(max_length = 16)
	password = forms.CharField(max_length = 16)

class SignUpForm(forms.Form):
	username = forms.CharField(max_length = 16)
	password = forms.CharField(max_length = 16)
	name = forms.CharField(max_length = 90)
	age = forms.IntegerField(min_value = 21);


