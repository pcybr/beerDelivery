from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(max_length = 16)
	password = forms.CharField(max_length = 16)