from __future__ import unicode_literals
from django.conf import settings
from django.db import models

# Create your models here.
class resource(models.Model):
	title = models.CharField(max_length = 255)
	description = models.TextField()
	timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)
	updated = models.DateTimeField(auto_now = True, auto_now_add = False)
	RESOURCE_TYPE = (
	    ('L', 'Lectures'),
	    ('Q', 'Quizzes'),
	    ('T', 'Tutorials'),
	    ('E', 'Endsem'),
	)
	resource_type = models.CharField(max_length=30,
                  choices=RESOURCE_TYPE,
                  default="L")
	course_name = models.ForeignKey(
		'course', 
		on_delete=models.CASCADE,
	)
	upload = models.FileField(upload_to = '%s/media/' %settings.BASE_DIR)

	def __unicode__(self):
		return self.title

class course(models.Model):
	course_name = models.CharField(max_length = 255)
	course_description = models.TextField()
	course_id = models.IntegerField()

	def __unicode__(self):
		return self.course_name