from django.db import models

class Project(models.Model):
	image = models.ImageField(upload_to='images/')
	summary = models.TextField(max_length = 200)
    
	def __str__(self):
		return self.summary

class Blog(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to='images/')
	description = models.TextField(max_length=400)
       
	def __str__(self):
		return self.title