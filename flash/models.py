from django.db import models

class List(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()
	URL = models.CharField(max_length=100)
	published = models.DateTimeField(auto_now_add=True, db_index=True)
