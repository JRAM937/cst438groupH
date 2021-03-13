from django.urls import path

from . import views

urlpatterns = [
    #the empty string is the end of the URL
    #the views.index is the function in in views.py to go to
    #name is the tab name(if you hover over the tab in google chrome it will say the name)
    path('', views.index, name='index'),
    path('genlist',views.genBucketList, name='genlist'),
    path('list', views.list, name='list'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register')
]