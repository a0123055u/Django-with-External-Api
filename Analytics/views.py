from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from json.decoder import JSONDecodeError
import json
import requests
from Analytics.models import busarrivalv2
import requests as req
def index(request):
    print('entering')
    return render(request,'analytics/index.html')


def get_bus_arrival(request):
    if request.method == 'POST':
        request_json = request.body.decode('utf-8')
        ########################### EXTERNAL API CALL TO LTA DATA MALL BusArrivalv2 STARTS########################
        if request_json:
            url_bus_arrival_lta_datamall_api = 'http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2'
            headers= {
                'AccountKey': '3xwuowbkRXuw0XI9SRqPcw==',
                'Accept': 'application/json'}
            data = {'BusStopCode':str(request_json)}
            response = requests.get(url_bus_arrival_lta_datamall_api,headers=headers,params=data)
        else:
            context = {'status_code': 404, 'msg': 'Please fill in the Bud Stop Id','status':'error'}
            return JsonResponse(context)
        ##############################EXTERNAL API CALL TO LTA DATA MALL BusArrivalv2 ENDS HERE####################
        # print (json.dumps(response.json(), indent=2, sort_keys=True))
        test = []
        print('response.status_code',response.status_code)
        for k, v in response.json().items():
            if (k == 'Services'):
                test = v
        if response.status_code == 200 and len(test)!=0:
            bus_arr_v2_obj = busarrivalv2
            # val = body_unicode['item_text']
            for x in test:
                print(x['ServiceNo']," ",x['Operator']," ",x['NextBus']['EstimatedArrival']," ",x['NextBus2']['EstimatedArrival'])
                bus_arr_v2_obj = busarrivalv2()
                bus_arr_v2_obj.service_number = x['ServiceNo']
                bus_arr_v2_obj.operator=x['Operator']
                bus_arr_v2_obj.destination_code=x['NextBus']['DestinationCode']
                bus_arr_v2_obj.estimated_arrival=x['NextBus']['EstimatedArrival']
                bus_arr_v2_obj.feature=x['NextBus']['Feature']
                bus_arr_v2_obj.latitude= x['NextBus']['Latitude']
                bus_arr_v2_obj.longitute=x['NextBus']['Longitude']
                bus_arr_v2_obj.load=x['NextBus']['Load']
                bus_arr_v2_obj.origin_code=x['NextBus']['OriginCode']
                bus_arr_v2_obj.type=x['NextBus']['Type']
                bus_arr_v2_obj.visit_number=x['NextBus']['VisitNumber']
                bus_arr_v2_obj.save()
                # print(body_unicode)
            # print('request.body',body_unicode)
            context ={'Services':test,'status_code':200,'msg':'Successfully recieved data'}
            return JsonResponse(context)
        else:
            context = {'status_code': 500, 'msg': 'Server Not available pls try after some time'}
            return JsonResponse(context)

