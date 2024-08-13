from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("sokhum sana \n u r at the pols index")
