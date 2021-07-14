from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [

         path('register/', views.register, name ='register'),
         
         
]