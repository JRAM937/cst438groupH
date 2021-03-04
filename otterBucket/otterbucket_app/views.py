from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# index is the name used in urls.py to call this function
def index(request):
    return HttpResponse("<h1>This is were you would put a view file</h1><a href='/list'>to list</a>")

def list(request):
    return HttpResponse("<a href = '/'>Back to index</a><h1>this is a list</h1>")