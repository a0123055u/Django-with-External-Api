from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from json.decoder import JSONDecodeError
import json
import requests
from Analytics.models import busarrivalv2, busTiming
import requests as req
from datetime import datetime
from datetime import timedelta

from Analytics.tasks import delete_record_older_than_three_days

# import schedule
import time
def index(request):
    print('entering')
    return render(request,'analytics/index.html')


def get_bus_arrival(request):
    if request.method == 'POST':
        request_json = request.body.decode('utf-8')
        ########################### EXTERNAL API CALL TO LTA DATA MALL BusArrivalv2 STARTS########################
        if request_json:
            bus_list = busarrivalv2.objects.filter(bus_stop_id=str(request_json),last_updated_time__lte=datetime.now()-timedelta(seconds=-30)).\
                values_list('service_number','bus_stop_id','last_updated_time')
            for x in bus_list:
                print (x)
            print('TEST ',datetime.now()-timedelta(seconds=-30))
            # print(bus_list)
            url_bus_arrival_lta_datamall_api = 'http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2'
            headers = {
                'AccountKey': '3xwuowbkRXuw0XI9SRqPcw==',
                'Accept': 'application/json'}
            data = {'BusStopCode': str(request_json)}
            response = requests.get(url_bus_arrival_lta_datamall_api, headers=headers, params=data)
        else:
            context = {'status_code': 404, 'msg': 'Please fill in the Bud Stop Id', 'status': 'error'}
            return JsonResponse(context)
        print('Test scheduler ')
        ##############################EXTERNAL API CALL TO LTA DATA MALL BusArrivalv2 ENDS HERE####################

        print (json.dumps(response.json(), indent=2, sort_keys=True))
        response_data = []
        print('response.status_code',response.status_code)
        test = delete_record_older_than_three_days.delay()
        print('response from schediler ------->', test)
        for k, v in response.json().items():
            if (k == 'Services'):
                response_data = v
        if response.status_code == 200 and len(response_data)!=0:

            for x in response_data:
                # print(x['ServiceNo']," ",x['Operator']," ",x['NextBus']['EstimatedArrival']," ",x['NextBus2']['EstimatedArrival'])
                #primary table for basic details
                bus_arr_v2_obj = busarrivalv2()
                bus_timing = busTiming()
                bus_arr_v2_obj.service_number = x['ServiceNo']
                bus_arr_v2_obj.operator=x['Operator']
                bus_arr_v2_obj.bus_stop_id = str(request_json)
                bus_arr_v2_obj.save()
                #secondary table for details
                bus_timing.next_bus = x['NextBus']
                bus_timing.next_bus1 = x['NextBus2']
                bus_timing.next_bus2 = x['NextBus3']
                bus_timing.busarrivalv2_details = busarrivalv2.objects.latest('id')
                bus_timing.save()
                # print(body_unicode)
            # print('request.body',body_unicode)
            context ={'Services':response_data,'status_code':200,'msg':'Successfully recieved data'}
            return JsonResponse(context)
        else:
            context = {'status_code': 500, 'msg': 'Server Not available pls try after some time'}
            return JsonResponse(context)


