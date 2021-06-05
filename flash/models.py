from django.db import models

class List(models.Model):
	title = models.CharField(max_length=50)
	ganre = models.TextField()
	URL = models.CharField(max_length=100)
	published = models.DateTimeField(auto_now_add=True, db_index=True)

class Services(models.Model):
	title = models.CharField(max_length=50)
	typeservices = models.CharField(max_length=50)
	content = models.TextField()
	price = models.CharField(max_length=20)
	published = models.DateTimeField(auto_now_add=True, db_index=True)