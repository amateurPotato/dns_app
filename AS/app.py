import urllib.request
from flask import Flask
from ast import literal_eval
from flask import request
from socket import *
import json

server_port = 53533
socket_conn_as = socket(AF_INET , SOCK_DGRAM)
socket_conn_as.bind(('' , server_port))


while True:
    
    payload , client_address = socket_conn_as.recvfrom(2048)
    payload_data = literal_eval(json.loads(json.dumps(payload.decode())) )
    
    if len(payload_data) == 4:
        
        with open('tmp.txt', 'w') as outfile:
            json.dump(payload_data, outfile)
        message = {
                "status": '201'
            }
        message = json.dumps(message)
            
    elif len(payload_data) == 2: 
        with open("tmp.txt", 'r', encoding='utf-8') as outfile:
            for line in outfile.readlines():
                data = json.loads(line)
                if payload_data['TYPE'] == data['TYPE'] and payload_data['NAME'] == data['NAME']:
                    message = json.dumps(data)
                else:
                    message = {
                        "status": '500'
                    }
                    message = json.dumps(message)
    else:
        message = {
                "status": '500'
            }
        message = json.dumps(message)
    socket_conn_as.sendto(message.encode(), client_address)