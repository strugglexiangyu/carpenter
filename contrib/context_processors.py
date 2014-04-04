# -*- coding:utf8 -*-

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
import logging
def current_user(request):
    user = request.user
    try:
        is_super = user.is_superuser
        is_saff = user.is_staff
    except Exception,e:
        logging.error(e)
        is_super = False
        is_saff = False
    return {'current_user': request.user,'is_super':is_super,'is_saff':is_saff}

def is_super_permission(redirect_url='error.html', login_url='/'):
    def wrapper(f):
        def decorate(*arg):
            request = arg[0]
            if not request.user.is_superuser:
                return render_to_response(redirect_url,{'message':u'对不起您权限不够'})
            else:
                return f(arg[0])
        return decorate
    return wrapper

def authority_required(redirect_url='/', login_url='/'):
    """
    Decorator for views that checks whether a user has a service permission
    enabled, redirecting to the redirect page if necessary.
    """
    def wrapper(f):
        def decorate(*arg):
            request = arg[0]
            if not request.user.id:
            	return HttpResponseRedirect(redirect_url)
            else:
            	return f(arg[0])
        return decorate
    return wrapper