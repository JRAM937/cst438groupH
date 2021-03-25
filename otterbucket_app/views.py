from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.db.models import Q

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
    users = User.objects.all()
    context = {'items': items, 'users': users}
    return render(request, 'otterbucket_app/admin-main.html', context)


def adminAddItem(request):
    return render(request, 'otterbucket_app/admin-add-item.html')


def manualAddItem(request):
    b = BucketItem(title=request.POST['title'], text=request.POST['text'])
    b.save()
    return HttpResponseRedirect(reverse('adminMain'))


def adminAddUser(request):
    return render(request, 'otterbucket_app/admin-add-user.html')


def manualAddUser(request):
    u = User(username=request.POST['username'], password=request.POST['password'])
    u.save()
    return HttpResponseRedirect(reverse('adminMain'))

def adminUpdateItem(request, itemId):
    item = BucketItem.objects.get(id=itemId)
    context = {'item': item}
    return render(request, 'otterbucket_app/admin-update-item.html', context)

def manualUpdateItem(request):
    item = BucketItem.objects.get(id=request.POST['itemId'])
    item.title = request.POST['title']
    item.text = request.POST['text']
    item.save()
    return HttpResponseRedirect(reverse('adminMain'))

def adminUpdateUser(request, userId):
    user = User.objects.get(id=userId)
    context = {'user': user}
    return render(request, 'otterbucket_app/admin-update-user.html', context)

def manualUpdateUser(request):
    user = User.objects.get(id=request.POST['userId'])
    user.username = request.POST['username']
    user.password = request.POST['password']
    user.save()
    return HttpResponseRedirect(reverse('adminMain'))

def manualDeleteItem(request):
    item = BucketItem.objects.get(id=request.POST['itemId'])
    item.delete()
    return HttpResponseRedirect(reverse('adminMain'))

def manualDeleteUser(request):
    user = User.objects.get(id=request.POST['userId'])
    user.delete()
    return HttpResponseRedirect(reverse('adminMain'))
    
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
        return render(request, 'otterbucket_app/register-failed.html')


#Log in a user
def loginUser(request):
    typedUser = request.POST['username']
    typedPass = request.POST['password']
    checkUser = User.objects.filter(username = typedUser).exists()

    if checkUser:
        validUser = User.objects.get(username = typedUser)
        if validUser.password == typedPass:
            request.session['username'] = typedUser
            print("Login Success!")
            return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'otterbucket_app/login-failed.html')

#Edit Account page
def editAccount(request):
    currUser = request.session['username']
    u = User.objects.get(username = currUser)
    context = {"userid" : u.id, "username" : u.username, "password" : u.password}
    return render(request, 'otterbucket_app/edit-account.html', context)

#log out of an account
def logout(request):
    request.session.flush()
    return render(request, 'otterbucket_app/logged-out.html')

def search(request):
    return render(request, 'otterbucket_app/search.html')

def searchResult(request):
    search = request.POST['search']
    context = {}
    query = Q(title__contains=search) | Q(text__contains=search)
    items = BucketItem.objects.filter(query)
    context['bucketItems'] = items
    return render(request, 'otterBucket_app/search.html',context)

def userList(request):
    if(request.session.get('username',None) == None):
        return HttpResponseRedirect(reverse('login'))
    username = request.session['username']
    context = {'username': username}
    user = User.objects.get(username = username)
    bucketIds = BucketList.objects.filter(user = user).values_list('bucket_item')
    bucketItems = BucketItem.objects.filter(id__in=bucketIds)
    context['bucketItems'] = bucketItems
    return render(request, 'otterbucket_app/user-list.html',context)

def itemPage(request,item_id):
    item = BucketItem.objects.filter(id=item_id)
    if(len(item) == 0):
         return HttpResponse("<a href='/' class='btn btn-danger'>Home</a><h1>Item not found</h1>")
    context = {'item' : item[0]}
    if(request.session.get('username',None) != None):
        u = User.objects.get(username = request.session.get('username'))
        context['username'] = u.username
        context['user_id'] = u.id
    return render(request, 'otterbucket_app/item.html', context)

#to do at item to bucketlist
def userAddItem(request):
    itemId = request.POST['itemId']
    
    user = User.objects.get(username=request.session['username'])
    item = BucketItem.objects.get(id=itemId)
    print(user)
    print(item)
    l = BucketList(user=user,bucket_item=item)
    print(l)
    l.save()
    return HttpResponseRedirect(reverse('itemPage',args=[itemId]))

def userRemoveItem(request):
    itemId = request.POST['itemId']
    user = User.objects.get(username=request.session['username'])
    item = BucketItem.objects.get(id=itemId)
    l = BucketList.objects.filter(user=user,bucket_item=item)
    l.delete()
    return HttpResponseRedirect(reverse('userList'))

def randomItem(request):
    if(request.session.get('Username',None) == None):
        return HttpResponseRedirect(reverse('login'))

    context = {}
    username = request.session['Username']

    user = User.objects.get(username = username)
    
    #=====================================================================
    #The following two lines of code only work if the user has a list. The 
    #third line allows for debugging should the user have no way to create
    #a list.
    #---------------------------------------------------------------------

    bucketIds = BucketList.objects.filter(user = user)
    bucketItems = BucketItem.objects.filter(id__in=bucketIds)

    #---------------------------------------------------------------------
    #Should the user have no way to create a list, comment out the
    #previous two lines of code and then uncomment the code below.
    #-------------------------------------------------------------
    #bucketItems = BucketItem.objects.all()
    #-------------------------------------------------------------
    #=====================================================================

    bucketItemJson = serializers.serialize('json', bucketItems)
    context['bucketItems'] = bucketItemJson

    return render(request, 'otterbucket_app/random-item.html', context)
