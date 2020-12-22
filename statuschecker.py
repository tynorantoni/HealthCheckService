import datetime

import requests
import json

from dbconnector import connect_to_db
from dbmanipulation import insert_status_to_db

list_of_services = {
    'BSS':'http://127.0.0.1:5000/ping',
    'KSS':'http://127.0.0.1:5000/ping',
    'WCS':'http://127.0.0.1:5000/ping',
    'DAS':'http://127.0.0.1:5000/ping',
    'UIS':'http://127.0.0.1:5050/ping'
}


def get_health_status():
    dict_of_requests = {}
    conn = connect_to_db()
    for service in list_of_services:
        try:
            request = requests.get(list_of_services[service])
            dict_of_requests[service] = request.text

        except Exception as exc:
            print("failure ", exc)
            dict_of_requests[service] = 'dead'

    insert_status_to_db(conn,
                        date_of_ping=datetime.datetime.today(),
                        BSS=dict_of_requests['BSS'],
                        KSS=dict_of_requests['KSS'],
                        WCS=dict_of_requests['WCS'],
                        DAS=dict_of_requests['DAS'],
                        UIS=dict_of_requests['UIS'])
    return dict_of_requests

