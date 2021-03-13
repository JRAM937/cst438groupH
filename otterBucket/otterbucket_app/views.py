from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import BucketItem,BucketList,User

# Create your views here.
# index is the name used in urls.py to call this function
def index(request):
    return render(request, 'otterbucket_app/mainPage.html')

def genBucketList(request):
    for i in range(10):
        b = BucketItem(title=i, text="text")
        b.save()
    return redirect('/list')

def list(request):
    bucketItems = BucketItem.objects.all()
    context = {'bucketItems': bucketItems}
    return render(request, 'otterbucket_app/display_list.html',context)

def login(request):
    users = User.objects.all()
    context = {'users' : users}
    return render(request, 'otterbucket_app/login.html', context)

def register(request):
    users = User.objects.all()
    context = {'users' : users}
    return render(request, 'otterbucket_app/register.html', context)