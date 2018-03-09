# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
import urllib.request
import urllib.parse
import json

def index(request,pk=None):
	req = urllib.request.Request('http://models-api:8000/api/v1/person/1')
	response = urllib.request.urlopen(req, timeout=5).read().decode('utf-8')
	data = json.loads(response)
	return JsonResponse(data)

def getPerson(index,pk = None):
	endpoint = "http://models-api:8000/api/v1/person/" + str(pk)
	req = urllib.request.Request(endpoint)
	response = urllib.request.urlopen(req).read().decode('utf-8')
	data = json.loads(response)
	return JsonResponse(data)
