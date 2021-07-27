from django.db import models

class Customer(models.Model):
	name = models.CharField(max_length=30)
	email =models.CharField(max_length=50)
	contact = models.CharField(max_length=10)

	class Meta:
		db_table ='customer'


class Product(models.Model):
	productname = models.CharField(max_length=30)
	price = models.CharField(max_length=10)
	Description = models.TextField()
	Company = models.CharField(max_length=30)

	class Meta:
		db_table ='product'


