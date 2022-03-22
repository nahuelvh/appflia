from django.shortcuts import render
from django.http import HttpResponse
from appflia.models import Familia
from django.template import loader

def familiares(request)
    familia = Familia.objects.get(id = 1)
    return print(familia)
