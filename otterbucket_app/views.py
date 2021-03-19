from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import BucketItem,BucketList,User

# Create your views here.
# index is the name used in urls.py to call this function
def index(request):
    return render(request, 'otterbucket_app/main-page.html')

def genBucketList(request):
    for i in range(10):
        b = BucketItem(title=i, text="text")
        b.save()
    return redirect('/list')

def list(request):
    bucketItems = BucketItem.objects.all()
    context = {'bucketItems': bucketItems}
    return render(request, 'otterbucket_app/display-list.html', context)

def login(request):
    bucketItems = BucketItem.objects.all()
    context = {'bucketItems': bucketItems}
    return render(request, 'otterbucket_app/login.html', context)

def register(request):
    bucketItems = BucketItem.objects.all()
    context = {'bucketItems': bucketItems}
    return render(request, 'otterbucket_app/register.html', context)

# TODO: Check if admin.
def adminMain(request):
    items = BucketItem.objects.all()
    context = {'items': items}
    return render(request, 'otterbucket_app/admin-main.html', context)

def adminAddItem(request):
    return render(request, 'otterbucket_app/admin-add-item.html')

def manualAddItem(request):
    b = BucketItem(title=request.POST['title'], text=request.POST['text'])
    b.save()
    return HttpResponseRedirect(reverse('adminMain'))

def manualAddUser(request):
    u = User(username=request.POST['username'], password=request.POST['password'])
    u.save()
    return HttpResponseRedirect(reverse('adminMain'))

# TODO: Implement search
def search(request):
    return render(request, 'otterbucket_app/search.html')

#register a user
def registerUser(request):
    newUser = request.POST['username']
    newPass = request.POST['password']
    check = User.objects.filter(username = newUser).exists()

    if check == False:
        U = User(username = newUser, password = newPass)
        U.save()
        return HttpResponseRedirect(reverse('login'))
    else:
        return redirect('/register')

#Log in a user
def loginUser(request):
    typedUser = request.POST['username']
    typedPass = request.POST['password']
    checkUser = User.objects.filter(username = typedUser).exists()

    if checkUser == True:
        validUser = User.objects.get(username = typedUser)
        if validUser.password == typedPass:
            request.session['Username'] = typedUser
            print("Login Success!")
            return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('login'))
      
# TODO: Implement random_item
def randomItem(request):
    return render(request, 'otterbucket_app/random-item.html')
