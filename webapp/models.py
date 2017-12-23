from django.db import models
from django.forms import ModelForm

class signupp(models.Model):
		name = models.CharField(max_length=50)
		username = models.CharField(max_length=15)
		password = models.CharField(max_length=20)
		address = models.TextField()
		contactnumber = models.CharField(max_length=14)

'''class signuppf(ModelForm):
	class meta:
		model = signupp
		fields = ['name', 'username', 'password', 'address', 'contactnumber']'''
			
