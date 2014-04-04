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
from apps.business.models.business import Customer,Business,UserCustomer,UserBusiness

@render_to('index.html')
def index(request):
    user = request.user
    try:
        business = UserBusiness.objects.filter(userId=user.id)
        firstbu = business[0].businessId
    except:
        return   {'chartdata': [],'business':[] ,'customer':[] }
    for bu in business:
        bus = Business.objects.get(id=bu.businessId)
        bu.name = bus.name
        
 

    businessid = request.REQUEST.get('current_business',firstbu)
    page = request.REQUEST.get('page',0)
    
    customer =  UserCustomer.objects.filter(business_id=businessid)

    nowbusiness = Business.objects.get(id=businessid)
    customer_codess = []
    customer_codes = []
    for custom in customer:
        tomer = Customer.objects.get(id=custom.customerId)
        customer_codess.append({'code':int(tomer.code),'name':str(tomer.name)})

 
    if len(customer_codess) > page :
        if (len(customer_codess) - page )>1:

            customer_codes = customer_codess[page:2]
        else:
            customer_codes = customer_codess[page:1]
    else:
        return {'chartdata': [],'business':business  }
    
    chartData = []
    for customer in customer_codes:
  
        #channels = get_customer_Channel(customer['code'],nowbusiness.code)
        channels = get_customer_Channel(customer['code'],1)
        
        cs = []
        if len(channels) == 0:
            chartData.append({'customer':str(customer['name']),'outdata':[]} )

            continue

        for channel in channels:
        	cs.append(channel['channelCode'])
        outdata = get_data_by_Channel(cs,4)
        chartData.append({'customer':str(customer['name']),'outdata':map(toint,outdata)} )
     
     
    return {'chartdata': chartData,'business':business ,'customer':customer_codess[2:] }

@csrf_exempt
def pubuliu(request):

    customer =   request.REQUEST.get('customer','')

    customer_codes =  customer.split(',')
    
    chartData = []
    for customer in customer_codes:
        #channels = get_customer_Channel(customer['code'],nowbusiness.code)
        channels = get_customer_Channel(customer.split('-')[0],1)
        cs = []
        if len(channels) == 0:
            continue

        for channel in channels:
            cs.append(channel['channelCode'])
        outdata = get_data_by_Channel(cs,4)
        chartData.append({'customer':str(customer.split('-')[1]),'outdata':map(toint,outdata)} )
     
    return json_response({'chart_data':chartData})
    #return {'chartdata': chartData,'business':business ,'count':len(customer_codes) }

 
 
