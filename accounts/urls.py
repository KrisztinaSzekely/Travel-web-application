from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path('register/', views.registerPage, name="register"),
   path('login/', views.loginPage, name="login"),
   path('', views.loginPage, name="home"),
   # path('logout/', PresentationLayer.views.logoutUser, name="logout"),

]
