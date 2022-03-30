import json
from traceback import print_tb
import requests

#Functions
api_url = "https://xsb8acpx2a.execute-api.us-east-1.amazonaws.com/dev/barcode"


#tells API that order number has been placed in locker number so that 
#it can notify User app that it is placed and give locker number
def order_ready(locker_number, order_number):
    print("sending message that locker {} has been placed in locker".format(locker_number))
    response = requests.get(api_url)
    print(response.status_code)
    initial_response = response.json()
    print(initial_response['body'])

#tells API that order_number has new temp. Will tell user updated temp
def order_temp_update(order_number, temp):
    return

#asks API to give order_number for given barcode
#this is so that we can authenticate, get order number so I know which locker to unlock
def barcode_to_order_numer(barcode):
    return

#tells API to remove entry for order_number since it has been picked up
def delete_order_number(order_number):
    return


#just testing 
order_ready(7)