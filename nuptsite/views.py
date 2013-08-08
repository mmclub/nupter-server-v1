from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render_to_response
from nuptsite.models import Students


		

def index(request):
	if ('value' in request.GET) and ('type' in request.GET):
		search_type = request.GET['type']
		search_value = request.GET['value']
		if search_type == 'name':
			students = Students.objects.filter(name__contains = search_value)
		elif search_type == 'number':
			students = Students.objects.filter(number__contains = search_value)
		elif search_type == 'college':
			students = Students.objects.filter(college__contains = search_value)
		elif search_type == 'major':
			students = Students.objects.filter(major__contains = search_value)
		else:
			students = Students.objects.filter(classes__contains = search_value)
		message = "you search type : " + search_type + ' value : ' + search_value

	else:
		message = "No value"
	return render_to_response("index.html", locals())

def header(request):
	values = request.META.items()
	values.sort()
	html = []
	for k, v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
	return HttpResponse('<table> %s </table>' % '\n'.join(html))
