# -*- coding: utf-8 -*- 
import os
import sys
APP_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(APP_PATH)
from django.core.management import setup_environ
import settings
setup_environ(settings)
from django.db import IntegrityError
from apps.business.models.business import Customer
from apps.helper.help import *
f = open("customer.txt")

data = []
while  1:
	line = f.readline() 
	if not line:
		break
	if line.strip() == '':
		continue
	data.append({"name":line.strip(),"code":get_customer_code(line.strip())})
for i in data:
	if i["code"] == "":
		c = [i["name"]]
		print c,"++++++++++++++++++++++++++++++++"
		continue 
	else :
		try :
			customer = Customer()
			customer.name = i["name"]
			customer.code = i["code"]
			customer.save()
			print i['name']
		except Exception, e:
			pass 
f.close()


