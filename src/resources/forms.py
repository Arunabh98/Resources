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
		widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter Title','class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter description here', 'class': 'form-control'}),
            'resource_type': forms.Select(attrs={'class': 'form-control'}),
        	'course_name':forms.Select(attrs={'class': 'form-control'}),
        	'upload': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
	upload = forms.FileField(
			label = 'Select a file',
			help_text = 'max. 5 megabytes',
		)
