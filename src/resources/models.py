from __future__ import unicode_literals
from django.conf import settings
from django.db import models

# Create your models here.
class resource(models.Model):
	title = models.CharField(max_length = 255)
	description = models.TextField()
	timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)
	updated = models.DateTimeField(auto_now = True, auto_now_add = False)
	upload = models.FileField(upload_to = '%s/media/' %settings.BASE_DIR)

	def __unicode__(self):
		return self.title