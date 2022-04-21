from re import template
from django.shortcuts import render

def demoIndex(request):
    template = 'index.html'
    return render(request, template)

#render () = it takes three parameter among which two of the compulsory 
#1. request
#2. template
#3. data (must be in dict)