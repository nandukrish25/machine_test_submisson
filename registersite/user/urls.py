from django.urls import path
from . import views
from django.urls import include




urlpatterns = [
    path('', views.homepage, name='home'),
     path('register', views.registeruser, name='register'),
      path('login', views.loginuser, name='login'),
      path('student', views.student, name='student'),
      path('staff', views.staff, name='staff'),
      path('admins', views.admin, name='admins'),
      path('editor', views.editor, name='editor'),
      path('logout', views.logoutuser, name='logout'),
       path('redirect', views.redirect, name='redirect')





     
]