from Analytics.models import *
from rest_framework import serializers


class BusArrivalBaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = busarrivalv2
        fields = ['service_number', 'operator', 'bus_stop_id']


