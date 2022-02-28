from email import message
import urllib.request
from flask import Flask
from flask import request
from ast import literal_eval
from socket import *
import json

app = Flask(__name__)

@app.route('/register', methods=['PUT'])
def register():
    payload_data = request.get_json()
    if 'hostname' in payload_data:
        hostname = payload_data['hostname']
    if 'as_port' in payload_data:
        as_port = payload_data['as_port']
    if 'as_ip' in payload_data:
        as_ip = payload_data['as_ip']
    if 'ip' in payload_data:
        ip = payload_data['ip']
    
    # mesaage 
    message_data = {
        'TYPE': 'A',
        'NAME': hostname,
        'TTL': 10,
        'VALUE' : ip
        }
    message = json.dumps(message_data)
    
    # socket
    server = as_ip
    server_port = 53533
    
    #socket connection
    socket_conn_fs = socket(AF_INET, SOCK_DGRAM)
    socket_conn_fs.sendto(message.encode(), (server, server_port))
    resp, server_address = socket_conn_fs.recvfrom(2048)
    socket_conn_fs.close()
    data = literal_eval(json.loads(json.dumps(resp.decode())) )
    return message_data, 201
    
@app.route('/fibonacci', methods=['GET'])
def fibonacci_req():
    args = request.args
    number = args['number']

    if not number.isnumeric():
        return {'Error': 'Int not found'}, 400
    number = int(number)
    X=fibonacci(number)
    return {'Fibonacci number for sequence {}'.format(number) : X}, 200

def fibonacci(n):
    if n<=1:
        return 0
    elif n==2:
        return 1
    else: 
        return fibonacci(n-1) + fibonacci(n-2)
    
app.run(host='0.0.0.0', port=9090, debug=True)
    

    