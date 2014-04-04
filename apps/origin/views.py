# -*- coding:utf8 -*-
from annoying.decorators import render_to,ajax_request
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import HttpResponseRedirect
from contrib.shortcuts import json_response
 
import simplejson as json

from django.contrib.auth.models import User
 
from apps.helper.help  import *
import time

@render_to('origin/index.html')
def index(request):
	if not request.GET:
		return {}

	start = request.REQUEST.get('start','')
	end = request.REQUEST.get('end','')
	channelid = request.REQUEST.get('channel_id','')

	if channelid =='':
		return {'message':'channel为空','start':start,'end':end,'channelid':channelid}
	if  start =='':
		return {'message':'开始时间为空','start':start,'end':end,'channelid':channelid}
	if end =="":
		return {'message':'结束时间为空','start':start,'end':end,'channelid':channelid}

	StartTime = time.mktime(time.strptime(start,'%Y-%m-%d %H:%M'))
	x = time.localtime(StartTime)
	start_time =  time.strftime('%Y%m%d%H%M',x)
	#endtime
	EndTime = time.mktime(time.strptime(end,'%Y-%m-%d %H:%M'))
	x = time.localtime(StartTime)
	end_time =  time.strftime('%Y%m%d%H%M',x)
	if StartTime > EndTime :
		return  {'message':'开始时间必须小于结束时间'}
	data = get_origin(start_time,end_time,channelid)

	return {'data':map(toint,data),'start':start,'end':end,'channelid':channelid}