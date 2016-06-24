from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.encoding import smart_str
from .forms import resourceForm
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
# Create your views here.
from .models import resource, course
from django.http import HttpResponseRedirect
from datetime import datetime   
from django.conf import settings


def ldap_login(request):
	context = {
		"title": "Sign In",
	}
	return render(request, "ldap_login.html", context)


def course_homepage(request):
	queryset_list = course.objects.all()
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
			Q(course_name__icontains=query) |
			Q(course_description__icontains=query)

		).distinct()
	paginator = Paginator(queryset_list, 10) # Show 25 contacts per page
	page_request_var = 'page'
	page = request.GET.get(page_request_var)
	try:
	    queryset = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    queryset = paginator.page(paginator.num_pages)
	context = {
		"object_list": queryset,
		"title": "Courses",
		"page_request_var": page_request_var
	}

	return render(request, "course_list.html", context)

def course_detail(request, id=None):
	instance = get_object_or_404(course, id = id)
	# Converting first page into JPG
	#with Image(filename="%s" %str(instance.upload)) as img:
	#     img.save(filename="%s/media/temp-%s.jpg" % (settings.BASE_DIR, instance.id))
	context = {
		"instance": instance,
	}
	return render(request, "course_detail.html", context)

def resource_create(request):
	form = resourceForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance = resource(upload=request.FILES['upload'], title=request.POST.get("title"), description = request.POST.get("description"), course_name = instance.course_name)
		instance.save()
		messages.success(request, "Successfully Created")
		#return HttpResponseRedirect("http://127.0.0.1:8000/resources/detail/%s" %str(instance.id))
		return HttpResponseRedirect(reverse('detail', kwargs={'id': instance.id}))
	
	context = {
		"form": form,
	}
	return render(request, "resource_form.html", context)	

def resource_detail(request, id=None):
	instance = get_object_or_404(resource, id = id)
	# Converting first page into JPG
	#with Image(filename="%s" %str(instance.upload)) as img:
	#     img.save(filename="%s/media/temp-%s.jpg" % (settings.BASE_DIR, instance.id))
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "resource_detail.html", context)

def resource_list(request, id=None, type=None):
	instance = get_object_or_404(course, id = id)
	queryset_list = resource.objects.filter(course_name = instance, resource_type = type).order_by("-timestamp")
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
			Q(title__icontains=query) |
			Q(description__icontains=query)

		).distinct()
	paginator = Paginator(queryset_list, 2) # Show 25 contacts per page
	page_request_var = 'page'
	page = request.GET.get(page_request_var)
	try:
	    queryset = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    queryset = paginator.page(paginator.num_pages)
	context = {
		"object_list": queryset,
		"title": "Resources",
		"page_request_var": page_request_var,
		"course": instance,
	}

	return render(request, "resource_list.html", context)

def resource_update(request, id = None):
	instance = get_object_or_404(resource, id = id)
	form = resourceForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = resource(upload=request.FILES['upload'], title=request.POST.get("title"), description=request.POST.get("description"), id=instance.id, timestamp = instance.timestamp, updated = datetime.now())
		instance.save()
		messages.success(request, "Saved")
		return HttpResponseRedirect(reverse('detail', kwargs={'id': instance.id}))
	
	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
	}
	return render(request, "resource_form.html", context)

def resource_delete(request, id = None):
	instance = get_object_or_404(resource, id = id)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("list")

def download(request, id = None):
	# Create the HttpResponse object with the appropriate PDF headers.
    instance = get_object_or_404(resource, id = id)
    fd = open(str(instance.upload))
    response = HttpResponse(fd, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="%s"'%((instance.title) + ".pdf")

    # Create the PDF object, using the response object as its "file."
    #p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    #p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    #p.showPage()
    #p.save()
    return response


