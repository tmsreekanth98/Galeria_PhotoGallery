from django.db import models

# Create your models here.

class Photo(models.Model):
	title = models.CharField(max_length=200)
	url = models.CharField(max_length=2000)
	is_favorite = models.BooleanField(default=False)
	file_format = models.CharField(max_length=20)
	date_added = models.DateField(auto_now_add=True)
	username = models.CharField(max_length=100,default='1')
	is_public = models.BooleanField(default=False)
	original_uploader = models.CharField(max_length=100,default='1')

	def __str__(self):
		return self.title+" ("+self.file_format+")"