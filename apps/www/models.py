from django.db import models

class News(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField(max_length=300)
	visible = models.BooleanField(default=True)
	
	def __unicode__(self):
		post = (self.title)
		return post 