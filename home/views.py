from django import http
from django.http.response import HttpResponseServerError
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
  return HttpResponse("{success: true}")

