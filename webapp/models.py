from django.db import models

class signupp(models.Model):
		name = models.CharField(max_length=50)
		username = models.CharField(max_length=15)
		passw = models.CharField(max_length=20)
		address = models.TextField()
		connum = models.CharField(max_length=14)


		
