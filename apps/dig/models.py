# -*- encoding=utf-8 -*-
from django.db import models

class Dns(models.Model):
	code = models.CharField(max_length=128,verbose_name=u'客户ID',unique=True)
	channel = models.CharField(max_length=128,verbose_name=u'频道名称')
	alarmtime = models.CharField(max_length=128,verbose_name=u'频道名称')
	alarmtype = models.CharField(max_length=128,verbose_name=u'告警类型')
	customer = models.CharField(max_length=128,verbose_name=u'客服人员')
	name = models.CharField(max_length=128,verbose_name=u'产品名称')
	def __unicode__(self):
		return u"产品名称%s" %self.name
	class Meta:
		app_label = 'dig'
		verbose_name = '解析异常域名”'





