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

def getOrder(request,pk = None):
	endpoint = "http://exp-api:8000/order/" + str(pk)
	req = urllib.request.Request(endpoint)
	response = urllib.request.urlopen(req).read().decode('utf-8')
	data = json.loads(response)
	buyer = data['buyer']
	item = data['item']
	return render(request,'order_detail_view.html',context={'buyer':buyer,'item':item})

def getTrip(request,pk = None):
	endpoint = "http://exp-api:8000/trip/" + str(pk)
	req = urllib.request.Request(endpoint)
	response = urllib.request.urlopen(req).read().decode('utf-8')
	data = json.loads(response)
	runner = data['runner']
	store = data['store']
	time_created = data['time']
	active = data['active']
	return render(request,'trip_detail_view.html',context={'runner':runner,'store':store,'time_created':time_created,'active':active,})
