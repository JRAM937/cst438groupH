from django.urls import path

from . import views

urlpatterns = [
    #the empty string is the end of the URL
    #the views.index is the function in in views.py to go to
    #name is the tab name(if you hover over the tab in google chrome it will say the name)
    path('', views.index, name='index'),
    path('genlist',views.genBucketList, name='genlist'),
    path('list', views.list, name='list'),
    path('adminMain', views.adminMain, name='adminMain'),
    path('adminAddItem', views.adminAddItem, name='adminAddItem'),
    path('manualAddItem', views.manualAddItem, name='manualAddItem'),
    path('manualAddUser', views.manualAddUser, name='manualAddUser'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('registerUser', views.registerUser, name='registerUser'),
    path('loginUser', views.loginUser, name='loginUser'),
    path('random-item', views.randomItem, name='randomItem'),
    path('login-failed', views.loginUser, name='loginFailed'),
    path('register-failed', views.registerUser, name='registerFailed'),
    path('user-list', views.userList, name='userList'),
    path('item/<int:item_id>',views.itemPage, name='itemPage'),
    path('search', views.search, name='search'),
    path('search-result', views.searchResult, name='searchResult'),
    path('user-add-item', views.userAddItem, name='userAddItem'),
]
