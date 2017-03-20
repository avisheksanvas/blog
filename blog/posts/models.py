from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse 
from django.db import models

# Create your models here.

#def upload_location(instance,filename):
#	return "%s/%s" %(instance.id,filename)

class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL , default=1)
	title = models.CharField(max_length=200)
	content = models.TextField()
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	image = models.ImageField(
		#upload_to=upload_location,
		null=True,blank=True,
		width_field="width_field",
		height_field="height_field")
	draft = models.BooleanField(default=False)
	publish = models.DateTimeField(auto_now=False,auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	
	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("posts_detail" , kwargs={"id" : self.id } )
	def get_update_url(self):
		return reverse("posts_update", kwargs={"id" : self.id } )