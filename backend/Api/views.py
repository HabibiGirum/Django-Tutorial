from django.shortcuts import render

from django.http import HttpResponse

def Home(requests):
    return HttpResponse("Hello this check Api . . .")
