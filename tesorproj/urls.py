"""tensorproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
#from tensorproject.views import helloworld,spidergame,jinjagame
from tesorproj.views import *



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index,name='index'),
#    url(r'^(?P<num1>\d+)/(?P<num2>\d+)/$',helloworld),
#    url(r'^(?P<num1>\d+)/$',spidergame),
#    url(r'^(?P<num1>\d+)/(?P<num2>\d+)/(?P<num3>\d+)/$',jinjagame),
    url(r'^write/',write,name='write'),
    url(r'^list/',list,name='list'),
    url(r'^view/(?P<num>[0-9]+)/$',view,name='view'),    

    
 #  url(r'', include('spider_v1.py')),
]



