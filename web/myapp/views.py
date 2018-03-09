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

def getPerson(request,pk = None):
	endpoint = "http://exp-api:8000/person/" + str(pk)
	req = urllib.request.Request(endpoint)
	response = urllib.request.urlopen(req).read().decode('utf-8')
	data = json.loads(response)
	name = data['name']
	age = data['age']
	return render(request,'person_detail_view.html',context={'name':name,'age':age})

def getBeer(request,pk = None):
	endpoint = "http://exp-api:8000/beer/" + str(pk)
	req = urllib.request.Request(endpoint)
	response = urllib.request.urlopen(req).read().decode('utf-8')
	data = json.loads(response)
	name = data['name']
	size = data['size']
	price = data['price']
	beer_type = data['beer_type']
	bottle_type = data['bottle_type']
	return render(request,'beer_detail_view.html',context={'name':name,'age':size,'price':price,'bottle_type':bottle_type,'beer_type':beer_type})

def getStore(request,pk = None):
	endpoint = "http://exp-api:8000/store/" + str(pk)
	req = urllib.request.Request(endpoint)
	response = urllib.request.urlopen(req).read().decode('utf-8')
	data = json.loads(response)
	name = data['name']
	location = data['location']
	inventory = data['inventory']
	return render(request,'store_detail_view.html',context={'name':name,'location':location,'inventory':inventory})
