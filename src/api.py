#file in charge of all API requests
import json
from wsgiref.util import request_uri
import requests

#Functions
api_url = "https://xsb8acpx2a.execute-api.us-east-1.amazonaws.com/dev/barcode"
base_url = "https://xsb8acpx2a.execute-api.us-east-1.amazonaws.com/prod/locker/"


#tells API that order number has been placed in locker number so that 
#it can notify User app that it is placed and give locker number
def order_ready(locker_number, order_number):
    print("sending message that locker {} has been placed in locker".format(locker_number))
    response = requests.get(api_url)
    print(response.status_code)
    initial_response = response.json()
    print(initial_response['body'])

#tells API that order_number has new temp. Will tell user updated temp
def order_temp_update(order_number, temp, locker_number):
    print(order_number)
    print(temp)
    print(locker_number)
    url = base_url + order_number
    print(url)

    r = requests.put(url, json = {"temperature": str(temp), "locker" : locker_number})
    print(r.status_code)
    print(r.content)
    return

#asks API to give order_number for given barcode
#this is so that we can authenticate, get order number so I know which locker to unlock
#no longer needed since barcode is order number
def barcode_to_order_numer(barcode):
    return

#tells API to remove entry for order_number since it has been picked up
def delete_order_number(order_number):
    print("deleting order")
    url = base_url + order_number
    print
    r = requests.delete(url)
    print(r.status_code)
    print(r.content)
    return


#just testing 
# order_ready(7, 1)