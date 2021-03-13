from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import BucketItem,BucketList,User

# Create your views here.
# index is the name used in urls.py to call this function
def index(request):
    return HttpResponse("<h1>This is were you would put a view file</h1><a href='/list'>to list</a>")

def genBucketList(request):
    for i in range(10):
        b = BucketItem(title=i, text="text")
        b.save()
    return redirect('/list')

def list(request):
    bucketItems = BucketItem.objects.all()
    context = {'bucketItems': bucketItems}
    return render(request, 'otterbucket_app/display_list.html', context)

# TODO: Check if admin.
def adminMain(request):
    items = BucketItem.objects.all()
    context = {'items': items}
    return render(request, 'otterbucket_app/adminMain.html', context)

# TODO: Implement search
def search(request):
    return render(request, 'otterbucket_app/search')
