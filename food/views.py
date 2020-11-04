from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hey peeps!")

def items(request):
    return HttpResponse("Hey items!")
