# -*- encoding=utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import datetime

class Business(models.Model):
	name = models.CharField(max_length=128,verbose_name=u'业务名称',unique=True)
	code = models.CharField(max_length=128,verbose_name=u'业务编号',unique=True)
	def __unicode__(self):
		return u"业务名称%s" %self.name
	class Meta:
		app_label = 'business'
		verbose_name = u'业务'


class Customer(models.Model):
	name = models.CharField(max_length=128,verbose_name=u'客户名称',unique=True)
	code = models.CharField(max_length=128,verbose_name=u'客户编号',unique=True)
	def __unicode__(self):
		return u"客户名称%s" %self.name
	class Meta:
		app_label = 'business'
		verbose_name = u'客户'


class UserBusiness(models.Model):
	businessId = models.IntegerField()
	userId = models.IntegerField()
	class Meta:
		app_label = 'business'


class UserCustomer(models.Model):
	customerId = models.IntegerField()
	business = models.ForeignKey(UserBusiness)
	class Meta:
		app_label = 'business'