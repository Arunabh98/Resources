from django import forms

from .models import resource

class resourceForm(forms.ModelForm):
	class Meta(object):
		model = resource
		fields = [
			"title",
			"description",
			"course_name",
			"resource_type",
			"upload",
		]
	upload = forms.FileField(
			label = 'Select a file',
			help_text = 'max. 5 megabytes',
		)
