from django import forms
from cred.models import Customer,Product

class CustomerFrom(forms.ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'

class ProductFrom(forms.ModelForm):
	class Meta:
		model = Product
		fields = '__all__'		