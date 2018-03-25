# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
import urllib.request
import urllib.parse
import json
import requests

from django.views.decorators.csrf import csrf_exempt


def index(request,pk=None):
	'''
	View Function for home page of site
	'''
	# req = urllib.request.Request('http://models-api:8000/api/v1/person/1')
	# response = urllib.request.urlopen(req, timeout=5).read().decode('utf-8')
	# data = json.loads(response)
	# return JsonResponse(data)

	return render(request,'index.html',context={},)

def getPerson(request,pk = None):
	'''
	View Function for individual person
	'''
	endpoint = "http://models-api:8000/api/v1/person/" + str(pk)
	req = urllib.request.Request(endpoint)
	response = urllib.request.urlopen(req).read().decode('utf-8')
	data = json.loads(response)
	return JsonResponse(data)

def getOrder(request,pk = None):
	'''
	View Function for individual order
	'''
	endpoint = "http://models-api:8000/api/v1/order/" + str(pk)
	req = urllib.request.Request(endpoint)
	response = urllib.request.urlopen(req).read().decode('utf-8')
	data = json.loads(response)
	return JsonResponse(data)

def getBeer(request,pk = None):
	'''
	View Function for individual beer
	'''
	endpoint = "http://models-api:8000/api/v1/beer/" + str(pk)
	req = urllib.request.Request(endpoint)
	response = urllib.request.urlopen(req).read().decode('utf-8')
	data = json.loads(response)
	return JsonResponse(data)

def getTrip(request,pk = None):
	'''
	View Function for individual trip
	'''
	endpoint = "http://models-api:8000/api/v1/trip/" + str(pk)
	req = urllib.request.Request(endpoint)
	response = urllib.request.urlopen(req).read().decode('utf-8')
	data = json.loads(response)
	return JsonResponse(data)

def getStore(request,pk = None):
	'''
	View Function for individual store
	'''
	endpoint = "http://models-api:8000/api/v1/store/" + str(pk)
	req = urllib.request.Request(endpoint)
	response = urllib.request.urlopen(req).read().decode('utf-8')
	data = json.loads(response)
	return JsonResponse(data)


def getAllPeople(request, pk = None):
	endpoint = "http://models-api:8000/api/v1/person/all"
	req = urllib.request.Request(endpoint)
	response = urllib.request.urlopen(req).read().decode('utf-8')
	data = json.loads(response)
	new_list = data
	return JsonResponse(new_list, safe = False)


def getAllBeers(request, pk = None):
	endpoint = "http://models-api:8000/api/v1/beer/all"
	req = urllib.request.Request(endpoint)
	response = urllib.request.urlopen(req).read().decode('utf-8')
	data = json.loads(response)
	new_list = data
	return JsonResponse(new_list, safe = False)

def getAllStores(request, pk = None):
	endpoint = "http://models-api:8000/api/v1/store/all"
	req = urllib.request.Request(endpoint)
	response = urllib.request.urlopen(req).read().decode('utf-8')
	data = json.loads(response)
	new_list = data
	return JsonResponse(new_list, safe = False)

def getAllOrders(request, pk = None):
	endpoint = "http://models-api:8000/api/v1/order/all"
	req = urllib.request.Request(endpoint)
	response = urllib.request.urlopen(req).read().decode('utf-8')
	data = json.loads(response)
	new_list = data
	return JsonResponse(new_list, safe = False)

def getAllTrips(request, pk = None):
	endpoint = "http://models-api:8000/api/v1/trip/all"
	req = urllib.request.Request(endpoint)
	response = urllib.request.urlopen(req).read().decode('utf-8')
	data = json.loads(response)
	new_list = data
	return JsonResponse(new_list, safe = False)


@csrf_exempt
def login(request,pk = None):
	if request.method == "POST":
		try:
			data = request.POST.copy()
			endpoint = "http://models-api:8000/api/v1/login"
			req = requests.post(endpoint,data=data)
			message = str((req.content).decode())
			ret = json.loads(message)
			return JsonResponse(ret)
		except:
			return JsonResponse({'status':401, 'message': req})