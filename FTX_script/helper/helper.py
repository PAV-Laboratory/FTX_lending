import time, hmac
from requests import Request, Session 
import requests

def authentication(request, API_KEY, API_SECRET): # login to the account necessacry to all api
    ts = int(time.time() * 1000)
    prepared = request.prepare()
    signature_payload = f"{ts}{prepared.method}{prepared.path_url}".encode()
    if prepared.body:
        signature_payload += prepared.body
    signature = hmac.new(API_SECRET.encode(), signature_payload, 'sha256').hexdigest()
    request.headers['FTX-KEY'] = API_KEY
    request.headers['FTX-SIGN'] = signature
    request.headers['FTX-TS'] = str(ts)

def make_request(method="", endpoint="", API_KEY="", API_SECRET="", **kwargs): #execute ther request
    _session = Session()
    url = "https://ftx.com/api" + endpoint
    if method == "GET":
        request = Request(method, url, params=kwargs.get("params"))
    if method == "POST":
        request = Request(method, url, json=kwargs.get("json")) 
    authentication(request=request,API_KEY=API_KEY, API_SECRET=API_SECRET)
    response = _session.send(request.prepare())
    return response.json() 


def get_balance(API_KEY="", API_SECRET=""):
    endpoint = "/wallet/balances"
    response = make_request(method= "GET", endpoint= endpoint, API_KEY=API_KEY, API_SECRET=API_SECRET)
    return response["result"]

def get_lending_rates(API_KEY="", API_SECRET=""):
    endpoint = "/spot_margin/lending_rates"
    response = make_request(method= "GET", endpoint= endpoint, API_KEY=API_KEY, API_SECRET=API_SECRET)
    return response['result']
 
def post_lending_offer(pair="", size=0.00, rate=0.00, API_KEY="", API_SECRET=""):
    endpoint = "/spot_margin/offers"
    payload = {
            "coin": pair,
            "size": size,
            "rate": rate
            }
    response = make_request(method= "POST", endpoint= endpoint, API_KEY=API_KEY, API_SECRET=API_SECRET, json=payload)
    if response["success"] == True:
        return "success"
    if response["success"] == False:
        return response              

def get_lending_history(API_KEY="", API_SECRET=""):
    endpoint = "/spot_margin/lending_history"
    response = make_request(method= "GET", endpoint= endpoint, API_KEY=API_KEY, API_SECRET=API_SECRET)
    print (response)
    return response['result']

def get_lending_history_by_time(API_KEY="", API_SECRET="",start_time=0, end_time=0):
    endpoint = "/spot_margin/lending_history"
    params = {
            "start_time": start_time,
            "end_time": end_time
            }
    response = make_request(method= "GET", endpoint= endpoint, API_KEY=API_KEY, API_SECRET=API_SECRET, params=params)
    return response['result']         
