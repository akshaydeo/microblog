from django.db import models

class Post(models.Model):
	id 			= models.AutoField(primary_key = True)
	content 	= models.TextField(null = False)
	timestamp	= models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return content