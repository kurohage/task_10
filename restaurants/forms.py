from django import forms
from .models import Restaurant, Item
from django.contrib.auth.models import User

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        #fields = ['name', 'description', 'opening_time', 'closing_time', 'logo']
        # the owner is passed by django automatically and no one should be able to add restaurant objects to other users
        exclude = ['owner']

        widgets = {
        	'opening_time': forms.TimeInput(attrs={'type':'time'}),
        	'closing_time': forms.TimeInput(attrs={'type':'time'}),
        }

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price']

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email' ,'password']

        widgets={
        'password': forms.PasswordInput(),
        }

class SigninForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())