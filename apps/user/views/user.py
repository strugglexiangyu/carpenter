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
from contrib.shortcuts import json_response
from django.contrib.auth import authenticate,login
import re


@csrf_exempt
@render_to("user/index.html")
def index(request):
	if request.method == "POST":
		password = request.REQUEST.get('password','')
		repassword = request.REQUEST.get('repassword','')
		email = request.REQUEST.get('email','')
		if not password:
			return {"error":"重复密码不能为空"}
		if not email:
			return {"error":"邮箱不能为空"}
		if repassword != password:
			return {"error":"两次密码输入不一致"}
		isMatch = bool(re.match(r"^[a-zA-Z](([a-zA-Z0-9]*\.[a-zA-Z0-9]*)|[a-zA-Z0-9]*)[a-zA-Z]@([a-z0-9A-Z]+\.)+[a-zA-Z]{2,}$", email,re.VERBOSE))
		if isMatch is None:
			return {"error":"邮箱格式不正确"}
		user = User()
		user.username = email
		user.set_password(password)
		try:
			user.save()
			userlogin = authenticate(username=email,password=password)
			if userlogin is not None:
				login(request,userlogin)
				return HttpResponseRedirect(reverse('chart:chart_index'))
		except Exception, e:
			return {"error":"用户名已存在"}
		return HttpResponseRedirect(reverse('user:user_index'))
	return {}
