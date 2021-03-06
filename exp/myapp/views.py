# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
import urllib.request
import urllib.parse
import json
import requests
from kafka import KafkaProducer
from elasticsearch import Elasticsearch
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

def getTrip(request,pk = None,name=None):
	'''
	View Function for individual trip
	'''
	endpoint = "http://models-api:8000/api/v1/trip/" + str(pk)
	req = urllib.request.Request(endpoint)
	response = urllib.request.urlopen(req).read().decode('utf-8')
	data = json.loads(response)

	if "error" not in data:
		# end2 = "http://models-api:8000/api/v1/getMyPK"
		# req2 = urllib.request.Request(end2)
		# resp2 = urllib.request.urlopen(req2).read().decode('utf-8')
		# data2 = json.loads(response2)
		producer = KafkaProducer(bootstrap_servers='kafka:9092')
		listing = {'user_id':name, 'item_id':data['trip_id']}
		#listing = {'runner':ret['runner'],'store': ret['store'],'trip_id': ret['trip_id']}
		producer.send('recommendation_topic', json.dumps(listing).encode('utf-8'))
	return JsonResponse(data)

def getTrip2(request,pk = None):
	'''
	View Function for individual trip
	'''
	endpoint = "http://models-api:8000/api/v1/trip/" + str(pk)
	req = urllib.request.Request(endpoint)
	response = urllib.request.urlopen(req).read().decode('utf-8')
	data = json.loads(response)
	return JsonResponse(data)

def endTrip(request, pk=None,name=None):
	endpoint = "http://models-api:8000/api/v1/trip/" + str(pk) + '/' + str(name) + "/end"
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
def createTrip(request, pk = None):
	if request.method == "POST":
		try:
			data = request.POST.copy()
			endpoint = "http://models-api:8000/api/v1/createTrip"
			req = requests.post(endpoint,data=data)
			message = str((req.content).decode())
			ret = json.loads(message)
			if "error" not in ret:
				producer = KafkaProducer(bootstrap_servers='kafka:9092')
				listing = {'runner':ret['runner'],'store': ret['store'],'trip_id': ret['trip_id']}
				producer.send('trip_topic', json.dumps(listing).encode('utf-8'))
			return JsonResponse(ret) 
		except:
			return JsonResponse({'status':401, 'message': ret['error']})

@csrf_exempt
def createOrder(request, pk = None):
	if request.method == "POST":
		try: 
			data = request.POST.copy()
			endpoint = "http://models-api:8000/api/v1/createOrder"
			req = requests.post(endpoint,data=data)
			message = str((req.content).decode())
			ret = json.loads(message)
			if "error" not in ret:
				producer = KafkaProducer(bootstrap_servers='kafka:9092')
				listing = {'buyer': ret['buyer'], 'order_id': ret['order_id'], 'trip_id': ret['trip_id']}
				producer.send('order_topic', json.dumps(listing).encode('utf-8'))
			return JsonResponse(ret)
		except:
			return JsonResponse({'status':401, 'message': ret['error']})



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
			return JsonResponse({'status':401, 'message': 'Invalid Endpoint'})

@csrf_exempt
def signup(request, pk = None):
	if request.method == "POST":
		try:
			data = request.POST.copy()
			endpoint = "http://models-api:8000/api/v1/signup"
			req = requests.post(endpoint,data=data)
			message = str((req.content).decode())
			ret = json.loads(message)
			if "error" not in ret:
				producer = KafkaProducer(bootstrap_servers='kafka:9092')
				listing = {'name': ret['person_name'], 'username': ret['person_username'], 'person_id': ret['person_id']}
				producer.send('person_topic', json.dumps(listing).encode('utf-8'))
			return JsonResponse(ret)
		except:
			return JsonResponse({'status':401, 'message': 'Invalid Endpoint'})


@csrf_exempt
def logout(request):
	if request.method == "POST":
		try:
			data = request.POST.copy()
			endpoint = "http://models-api:8000/api/v1/logout"
			req = requests.post(endpoint,data=data)
			message = str((req.content).decode())
			ret = json.loads(message)
			return JsonResponse(ret)
		except:
			return JsonResponse({'status':401, 'error': 'Invalid Endpoint'})

@csrf_exempt
def checkAuth(request):
	try:
		data = request.POST.copy()
		endpoint = "http://models-api:8000/api/v1/checkAuth"
		req = requests.post(endpoint, data = data)
		message = str((req.content).decode())
		data = json.loads(message)
		return JsonResponse(data)
	except:
		return JsonResponse({'status':401, 'error': 'Invalid Endpoint'})

@csrf_exempt
def search(request):
	ret = {}
	try:
		data = request.POST.copy()
		info = data['all']
		search_type = data['search']
		es = Elasticsearch(['es'])
		if search_type == "Trip":
			search = es.search(index='listing_index_trip', body= {'query': {'query_string': {'query': info }}, 'size': 10})
		elif search_type == "Order":
			search = es.search(index='listing_index_order', body= {'query': {'query_string': {'query': info }}, 'size': 10})
		else:
			search = es.search(index='listing_index_person', body= {'query': {'query_string': {'query': info }}, 'size': 10})


		ret['status'] = 200
		output = search['hits']['hits']
		lst = []
		for value in output:
			lst.append(value['_source'])
		if len(lst) != 0:
			ret['search'] = lst
		else:
			ret['error'] = "Item not found"
		return JsonResponse(ret)

	except:
		return JsonResponse({'status':400, 'error': output})

