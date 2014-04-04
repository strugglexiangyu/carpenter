# -*- coding:utf8 -*-
from annoying.decorators import render_to,ajax_request
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib import messages
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.auth.models import User
from apps.business.models.business import Customer,Business,UserCustomer,UserBusiness
from contrib.shortcuts import json_response
import re


@csrf_exempt
@render_to("business/index.html")
def index(request):
	business = Business.objects.all()
	customer = Customer.objects.all().order_by("name")
	businessID = request.REQUEST.get("current_business",'')
	if not businessID:
		businessID = business[0].id
	user = request.user
	businessName = Business.objects.get(id=businessID)
	customerData = []
	try:
		busi = UserBusiness.objects.get(userId=user.id,businessId=businessID)

		customers = UserCustomer.objects.filter(business_id=busi.id)
		
		
		for c in customers:
			customerInfo = Customer.objects.get(id=c.customerId)
			customerData.append({"id":c.id,"name":customerInfo.name,"code":customerInfo.code,"users":user,"businessname":businessName.name,"businesscode":businessName.code
			})

	except Exception, e:
		busi = []
		customerData = {}
	#print customerData
	return {"data":business,"customer":customer,"tableList":customerData,"businessID":businessID}
	
@csrf_exempt
@render_to("business/index.html")
def create(request):
	businessID = request.REQUEST.get("business","")
	customer = request.REQUEST.get("customer","")
	if businessID == "":
		return json_response({"status":0,"mess":"NONE"})
	if customer == "":
		return json_response({"status":0,"mess":"NONE"})
	customerID = customer.split(",")
	user = request.user
	try:
		is_exist = UserBusiness.objects.get(businessId=businessID,userId=user.id)
		for i in customerID:
			try :
				is_exist_customer = UserCustomer.objects.get(business_id=is_exist.id,customerId=i)
			except Exception, e:
				print e
				customer = UserCustomer()
				customer.customerId = i
				customer.business_id = is_exist.id
				customer.save()
		return json_response({"status":1})
	except Exception, e:
		print e
		userbusiness = UserBusiness()
		userbusiness.businessId = businessID
		userbusiness.userId = user.id
		userbusiness.save()
		userbusinessid = userbusiness.id
		for i in customerID:
			customer = UserCustomer()
			customer.customerId = i
			customer.business_id = userbusinessid
			customer.save()
		return json_response({"status":1})
	return json_response({"status":2})

@csrf_exempt
@render_to("business/index.html")
def delete(request):
	delete = request.REQUEST.get("delete","")
	de = delete.split(",")
	 
	for d in de:
	  
		customer = UserCustomer.objects.filter(id=d)[0].delete()
		 
	return json_response({"a":111})