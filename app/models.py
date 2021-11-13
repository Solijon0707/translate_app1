from django.db import models

# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length=120)
	published = models.DateField(auto_now=True)


	def __str__(self):
		return self.name