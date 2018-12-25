from django.conf.urls import url

import Analytics
from Analytics.views import get_bus_arrival,index

urlpatterns = [
    url('',index),
    # url('/get_bus_arrival',views.get_bus_arrival,name='get_bus_arrival'),
    # url(r'^test/$',test)

]
