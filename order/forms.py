from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
  country = forms.CharField(max_length=255,
    widget=forms.TextInput(attrs={'class' : 'form-control', 'id' : 'last', 'aria-describedby' : 'last' }))
  firstname = forms.CharField(max_length=255,
    widget=forms.TextInput(attrs={'class' : 'form-control', 'id' : 'name', 'aria-describedby' : 'last', 'placeholder' : '""' }))
  lastname = forms.CharField(max_length=255,
    widget=forms.TextInput(attrs={'class' : 'form-control', 'id' : 'last', 'aria-describedby' : 'last' }))
  company = forms.CharField(max_length=255,
    widget=forms.TextInput(attrs={'class' : 'form-control', 'id' : 'last', 'aria-describedby' : 'last' }))
  address = forms.CharField(max_length=255,
    widget=forms.TextInput(attrs={'class' : 'form-control', 'id' : 'address', 'aria-describedby' : 'last' }))
  city = forms.CharField(max_length=255,
    widget=forms.TextInput(attrs={'class' : 'form-control', 'id' : 'last', 'aria-describedby' : 'last' }))
  email = forms.EmailField(max_length=255,
    widget=forms.TextInput(attrs={'class' : 'form-control', 'id' : 'email', 'aria-describedby' : 'email' }))
  phone = forms.CharField(max_length=255,
    widget=forms.TextInput(attrs={'class' : 'form-control', 'id' : 'phone', 'aria-describedby' : 'phone' }))
  country = forms.CharField(max_length=255,
    widget=forms.TextInput(attrs={'class' : 'form-control', 'id' : 'last', 'aria-describedby' : 'last' }))
  firstname = forms.CharField(max_length=255,
    widget=forms.TextInput(attrs={'class' : 'form-control', 'id' : 'name2', 'aria-describedby' : 'name2', 'placeholder' : '""' }))
  lastname = forms.CharField(max_length=255,
    widget=forms.TextInput(attrs={'class' : 'form-control', 'id' : 'last2', 'aria-describedby' : 'last2' }))
  company = forms.CharField(max_length=255,
    widget=forms.TextInput(attrs={'class' : 'form-control', 'id' : 'company', 'aria-describedby' : 'company' }))
  address = forms.CharField(max_length=255,
    widget=forms.TextInput(attrs={'class' : 'form-control', 'id' : 'address', 'aria-describedby' : 'last' }))
  city = forms.CharField(max_length=255,
    widget=forms.TextInput(attrs={'class' : 'form-control', 'id' : 'city', 'aria-describedby' : 'city' }))
  class Meta:
    model = Order
    fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']