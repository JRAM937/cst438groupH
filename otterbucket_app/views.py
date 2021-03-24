from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect

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

    if checkUser == True:
        validUser = User.objects.get(username = typedUser)
        if validUser.password == typedPass:
            request.session['username'] = typedUser
            print("Login Success!")
            return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'otterbucket_app/login-failed.html')
      
# TODO: Implement random_item
def randomItem(request):
    return render(request, 'otterbucket_app/random-item.html')

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
    bucketIds = BucketList.objects.filter(user = user)
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
    print(itemId)
    return HttpResponseRedirect(reverse('itemPage',args=[itemId]))
