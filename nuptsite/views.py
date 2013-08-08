from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render_to_response

def index(request):
	if 'value' in request.GET:
		message = "you search " + request.GET['value']
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
