"""AutomatedMachineLeanring URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from AutomatedMachineLeanring import views as mainView
from users import views as usr
from admins import views as admins

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainView.index, name='index'),
    path('logout/',mainView.logout, name='logout'),
    path('UserLogin/',mainView.UserLogin, name='UserLogin'),
    path('AdminLogin/',mainView.AdminLogin, name='AdminLogin'),
    path('UserRegister/',mainView.UserRegister, name='UserRegister'),

    ### User Side Views ####

    path('UserRegisterActions/', usr.UserRegisterActions, name='UserRegisterActions'),
    path('UserLoginCheck/', usr.UserLoginCheck, name='UserLoginCheck'),
    path('UserHome/', usr.UserHome, name='UserHome'),
    path('UserAutoMLTest/', usr.UserAutoMLTest, name='UserAutoMLTest'),
    path('UploadDatatoServer/',usr.UploadDatatoServer, name='UploadDatatoServer'),
    path('DataUploadForm/', usr.DataUploadForm, name='DataUploadForm'),
    path('AutoResponse/', usr.AutoResponse, name='AutoResponse'),
    path('UploadDatatoServerForPredections/', usr.UploadDatatoServerForPredections, name='UploadDatatoServerForPredections'),
    path('MyPredectionsSlot1/', usr.MyPredectionsSlot1, name='MyPredectionsSlot1'),
    path('MyPredectionsSlot2/', usr.MyPredectionsSlot2, name='MyPredectionsSlot2'),
    path('MyPredectionsSlot3/', usr.MyPredectionsSlot3, name='MyPredectionsSlot3'),
    path('AddDataToDataset/', usr.AddDataToDataset, name='AddDataToDataset'),
    path('AddDataForm/', usr.AddDataForm, name='AddDataForm'),

    ### Admin Side Urls ####

    path('AdminLoginCheck/', admins.AdminLoginCheck, name='AdminLoginCheck'),
    path('AdminHome/', admins.AdminHome, name='AdminHome'),
    path('ViewUsersList/', admins.ViewUsersList, name='ViewUsersList'),
    path('AdminActivaUsers/', admins.AdminActivaUsers, name='AdminActivaUsers'),
    path('UserPerformedOperations/', admins.UserPerformedOperations, name='UserPerformedOperations'),




]