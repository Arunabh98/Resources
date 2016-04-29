from django.contrib import admin

# Register your models here.
from .models import resource, course

class ResourceAdmin(admin.ModelAdmin):
	list_display = ["title","updated", "timestamp"]
	list_display_links = ["updated", "title"]
	list_filter = ["updated", "timestamp"]
	search_fields = ["title", "description"]
	class Meta:
		model = resource

class CourseAdmin(admin.ModelAdmin):
	list_display = ["course_name","course_id"]
	list_display_links = ["course_name"]
	search_fields = ["course_name", "course_id", "course_description"]
	class Meta:
		model = course
	
		
admin.site.register(resource, ResourceAdmin)
admin.site.register(course, CourseAdmin)