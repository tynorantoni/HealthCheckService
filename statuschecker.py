import requests
import json

list_of_services = {
    'BSS': 'http://3.133.136.130:8888/ping',
    'KSS': 'http://18.223.182.198:8888/ping',
    'WCS':'http://3.128.205.73:8888/ping',
    # 'DAS':'/ping',
    # 'UIS':'/ping'
}


def get_health_status():
    dict_of_requests = {}
    for service in list_of_services:
        try:
            request = requests.get(list_of_services[service])
            dict_of_requests[service] = request.json()
        except Exception as exc:
            print("failure ", exc)
            dict_of_requests[service] = 'dead'
    return json.dumps(dict_of_requests)
