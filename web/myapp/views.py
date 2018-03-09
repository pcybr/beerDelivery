# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
import urllib.request
import json

def index(request):
	req = urllib.request.Request('http://exp-api:8000/index/')
	response = urllib.request.urlopen(req).read().decode('utf-8')
	data = json.loads(response)
	# string = "HERE--- " + req
	return JsonResponse(data)

def getPerson(index,pk = None):
	endpoint = "http://exp-api:8000/person/" + str(pk)
	req = urllib.request.Request(endpoint)
	response = urllib.request.urlopen(req).read().decode('utf-8')
	data = json.loads(response)
	return JsonResponse(data)
