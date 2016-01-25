
# coding=utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, HttpResponseRedirect, render
from django.contrib.auth import authenticate, login, logout
from  django.utils.dateparse import parse_date
from django.contrib.auth.models import User
from django.views.generic import TemplateView,FormView
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect



def error404(request):
    return render(request,'404.html')