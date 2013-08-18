from django.http import HttpResponse
from django.core import serializers
from nuptsite.models import *




def save(type, request):
	try:
		title = request.GET['title']
		time = request.GET['time']
		content = request.GET['content']
		url = request.GET['url']
		record = Jwc(title = title, content = content, time = time, url = url)
		record.save()
		message = "ok"
	except:
		message = "faild"
	status = "{\"status\":" + message + "}"
	return  HttpResponse(status)




def jwc(request):
	result = Jwc.objects.all().order_by('time')[0:30]
	json = serializers.serialize('json', result, fields=('title','content', 'url'))
	return HttpResponse(json)

def news(request):
	result = News.objects.all().order_by('time')[0:30]
	json = serializers.serialize('json', result, fields=('title','content', 'url'))
	return HttpResponse(json)

def newspaper(request):
	result = Newspaper.objects.all().order_by('time')[0:30]
	json = serializers.serialize('json', result, fields=('title','content', 'url'))
	return HttpResponse(json)
	
def lost(request):
	result = Lost.objects.all().order_by('time')[0:30]
	json = serializers.serialize('json', result, fields=('title','content', 'url'))
	return HttpResponse(json)



def jwc_new(request):
	return save(Jwc, request)

def news_new(request):
	return save(Jwc, request)


def newspaper_new(request):
	return save(Jwc, request)

def lost_new(request):
	return save(Jwc, request)
