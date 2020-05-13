from django.contrib import admin
from django.urls import path
import myapp.views 
#from .import views

urlpatterns = [
    path('', myapp.views.home, name="home"),
    path('profile/', myapp.views.profile, name="profile"),
    path('hobby/', myapp.views.hobby, name="hobby"),
]