from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers

from .models import BucketItem,BucketList,User

# Create your views here.
# index is the name used in urls.py to call this function
def index(request):
    return render(request, 'otterbucket_app/main-page.html')

def genBucketList(request):
    b = BucketItem(title="Mothman", text="The superhero-movie passion-project, now on DVD!")
    b.save()
    b = BucketItem(title="Mothman 2", text="The sequel that raised the standards for action films everywhere. Own it on DVD!")
    b.save()
    b = BucketItem(title="Mothman 3", text="The cashgrab sequel made after a corporate buyout of the brand. This is a license to the corporate streaming service it's exclusive to.")
    b.save()
    b = BucketItem(title="A Rock", text="The perfect paperweight. Doesn't talk back or ask for higher pay when you use it. Unlike Greg.")
    b.save()
    b = BucketItem(title="Rubber Duck", text="A loyal companion for your long, lonely programming nights. He won't judge you. Unless you don't comment your code anywhere.")
    b.save()
    b = BucketItem(title="Shrek 2", text="A VHS copy of the cinematic masterpiece.")
    b.save()
    b = BucketItem(title="Greg", text="Our incredible intern. We will pay you to take him. *An amazing offer!*")
    b.save()
    b = BucketItem(title="VHS Player", text="Perfect for playing Shrek 2")
    b.save()
    b = BucketItem(title="Nokia 5185i Cellphone", text="Indestructable. *License to carry not included.*")
    b.save()
    b = BucketItem(title="Signed Vinyl of Michael Jackson's Thriler", text="'Are you even paying me to sign this?' - Greg")
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
        return render(request, 'otterbucket_app/register-failed.html')

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
        return render(request, 'otterbucket_app/login-failed.html')
      
# TODO: Implement random_item
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

    bucketIds = BucketList.objects.filter(user = user).values_list('bucket_item')
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
