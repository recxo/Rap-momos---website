from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
   path('',views.index,name='homepage'),
   path('About/',views.about,name='Aboutpage'),
   path('Services/',views.services,name='Services'),
   path('Contact/',views.contact,name='Contact'),
   path('savecontact/',views.contact,name='savecontact'),
   path('login',views.loginUser,name='login'),
   path('logout', views.logoutUser, name='logout'),
]


