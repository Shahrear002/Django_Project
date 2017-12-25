from django.db import models
from django.forms import ModelForm

class patient_info(models.Model):
	name = models.CharField(max_length=50)
	username = models.CharField(max_length=15, primary_key=True)
	password = models.CharField(max_length=20)
	address = models.TextField()
	contactnumber = models.CharField(max_length=14)

	def __str__(self):
		return self.username

class doctor_info(models.Model):
	name = models.CharField(max_length=50)
	username = models.CharField(max_length=15, primary_key=True)
	password = models.CharField(max_length=20)
	Chamber_address = models.TextField()
	Speciality = models.CharField(max_length=30)
	Degree = models.CharField(max_length=100)

			
