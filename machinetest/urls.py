"""machinetest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from machinetestapp import views

urlpatterns = [
    path('', views.showregistration,name='showregistration'),
    path('showregistration', views.showregistration,name='showregistration'),
    path('dologin',views.dologin,name='dologin'),
    path('save_user',views.save_user,name='save_user'),
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('adminpage', views.admin, name='adminpage'),
    path('student', views.student, name='student'),
    path('editor', views.editor, name='editor'),
    path('staff', views.staff, name='staff'),
    path('logout_user',views.logout_user),
]
