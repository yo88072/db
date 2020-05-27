from django.db import models

class student(models.Model):
	no = models.CharField(max_length=50)
	companyid = models.CharField(max_length=50)
	num = models.CharField(max_length=50)
	jobname = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	company = models.CharField(max_length=50)
	cash = models.CharField(max_length=50)
	
	def __str__(self):
		return self.no
