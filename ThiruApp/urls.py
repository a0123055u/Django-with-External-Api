"""ThiruApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from Analytics import urls,views
from rest_framework import routers
# from django.urls import path
from Analytics.views import home
router = routers.DefaultRouter()
router.register(r'analytics_bus_arrival', views.BusArrivalV2)



urlpatterns = [
    url(r'get_bus_arrival', views.get_bus_arrival, name="get_bus_arrival_post/"),
    url(r'^analytics/$',views.index,name="analytics"),
    url(r'^analytics_bus_arrival/$',(views.BusArrivalV2).as_view({'get': 'list'}),name="analytics_bus_arrival"),
    url(r'^admin/', admin.site.urls),

    url(r'^$',views.home, name="home"),

    # url(r'^search/', include('haystack.urls')),

]
