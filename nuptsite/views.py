# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.core import serializers
from django.utils import simplejson
from nuptsite.models import *

KEY = 'llpzqxh' # 不知道以后还记不记得。。


def save(type , request):
	try:
		key = request.GET['key']
		title = request.GET['title']
		time = request.GET['time']
		content = request.GET['content']
		url = request.GET['url']

		if key != KEY:
			raise Except()

		record = type(title = title, content = content, time = time, url = url)
		record.save()
		message = "ok"
	except:
		message = "faild"
	status = "{\"status\":" + message + "}"
	return  HttpResponse(status)



class QuerySetEncoder( simplejson.JSONEncoder ):
    """
    Encoding QuerySet into JSON format.
    """
    def default( self, object ):
        try:
            return serializers.serialize( "python", object, ensure_ascii = False )
        except:
            return simplejson.JSONEncoder.default( self, object )




def json_encode(list):
	s = ''' {"array" : [ '''
	for i in list:
		s = s + '{' + "\"title\"" + ':' + '"' + i.title + '",' 
		s = s + "\"content\"" + ':' + '"' + i.content + '",' 
		s = s + "\"url\"" + ':' + '"' + i.url + '"},'
	s = s[:-1] 
	s = s + ']}'
	return s



	 
def jwc(request):
	result = Jwc.objects.all().order_by('time')[0:30]
	return HttpResponse(json_encode(result))

def news(request):
	result = News.objects.all().order_by('time')[0:30]
	return HttpResponse(json_encode(result))


def newspaper(request):
	result = Newspaper.objects.all().order_by('time')[0:30]
	return HttpResponse(json_encode(result))

	
def lost(request):
	result = Lost.objects.all().order_by('time')[0:30]
	return HttpResponse(json_encode(result))


def jwc_new(request):
	return save(Jwc, request)

def news_new(request):
	return save(News, request)


def newspaper_new(request):
	return save(Newspaper, request)

def lost_new(request):
	return save(Lost, request)

