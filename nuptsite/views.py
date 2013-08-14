from django.http import HttpResponse
from django.core import serializers
from django.template import Template, Context
from django.shortcuts import render_to_response
from nuptsite.models import *


		





def jwc(request):
	result = Jwc.objects.all().order_by('time')[0:30]
	json = serializers.serialize('json', result, fields=('title','content'))
	return HttpResponse(json)


def jwc_new(request):
	if ('title' in request.GET) and ('content' in request.GET):
		title = request.GET['title']
		content = request.GET['content']

		record = Jwc(title = title, content = content)
		record.save()

		message = "ok"
	else:
		message = "faild"

	status = "{\"status\":" + message + "}"
	return  HttpResponse(status)




def news(request):
	result = News.objects.all().order_by('time')[0:30]
	json = serializers.serialize('json', result, fields=('title','content'))
	return HttpResponse(json)
	

def newspaper(request):
	result = Newspaper.objects.all().order_by('time')[0:30]
	json = serializers.serialize('json', result, fields=('title','content'))
	return HttpResponse(json)
	

def lost(request):
	result = Lost.objects.all().order_by('title')[0:30]
	json = serializers.serialize('json', result, fields=('title','content'))
	return HttpResponse(json)



def lost_new(request):
	if ('title' in request.GET):
		title = request.GET['title']
		time = int(request.GET['time'])
		record = Lost(title = title)
		record.save()
		message = "ok"
	else:
		message = "faild"

	status = "{\"status\":" + message + "}"
	return  HttpResponse(status)
	


def header(request):
	values = request.META.items()
	values.sort()
	html = []
	for k, v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
	return HttpResponse('<table> %s </table>' % '\n'.join(html))
