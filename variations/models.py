from django.db import models

class Variation(models.Model):
	
	def __unicode__(self):
		return self.name
	
	name = models.CharField(max_length=200)
	rating = models.IntegerField('rating')
	description = models.CharField(max_length=5000)
    

