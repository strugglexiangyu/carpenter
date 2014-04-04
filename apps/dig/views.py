# -*- coding:utf8 -*-
from annoying.decorators import render_to,ajax_request
 
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from apps.dig.models import Dns
from django.http import HttpResponseRedirect
from contrib.shortcuts import json_response
import json
@csrf_exempt
@render_to("test.html")
def get(request):
	return {}



@csrf_exempt
def save(request):
	if request.method == "POST":
 		data = request.REQUEST.get("postdata","")
		result = json.loads(data)
		dns =  Dns()
		dns.code = result['code']
		dns.channel = result['channel']
		dns.alarmtime = result['alarmtime']
		dns.customer = result['customer']
		dns.name = result['name']
		dns.alarmtype = result['alarmtype']
		try:
			dns.save()
		except Exception, e:
			raise e

	return   json_response({'status':'ok'})

