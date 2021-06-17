"""mpgWebApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from firstpage import views
from firstpage import example
from firstpage.views import tableCrud

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$',views.index,name='Homepage'),
    path('table' , tableCrud , name='tableCrud'),
    # url('predictMPG',views.predictMPG, name='predictMPG'),
    # url('viewDataBase',views.viewDatabase,name='viewDatabase'),
    # url('updateDataBase',views.updateDataBase,name='updateDataBase'),
    url('sentdata',views.sentdata,name='sentdata'),
    # url('profile',views.profile,name='profile'),
    # url('DataBase1',views.DataBase1,name='DataBase1'),
    # url('tabledata',views.tabledata,name='tabledata'),
     url('update',views.update1,name='update1'),
 
]
