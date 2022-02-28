from email import message
from ast import literal_eval
import urllib.request
from flask import Flask
from flask import request
from socket import *
import json

app = Flask(__name__)


@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    args = request.args
    # for k, v in args.items():
    #     print(f"{k}: {v}")
    hostname = None
    fs_port = None
    number = None
    as_ip = None
    as_port = None
    if "hostname" in args:
        hostname = args["hostname"]
    if "fs_port" in args:
        fs_port = args.get("fs_port")
    if "number" in args:
        number = args["number"]
    if "as_ip" in request.args:
        as_ip = request.args.get("as_ip")
    if "as_port" in request.args:
        as_port = request.args.get("as_port")

    if not hostname or not fs_port or not number or not as_ip or not as_port:
        return {'Error': 'Missing one or more required params: hostname, fs_port, number, as_ip, as_port'}, 400
        
    message_str = {
        'TYPE': 'A',
        'NAME': hostname
        }
    message = json.dumps(message_str)
    
    server = as_ip
    server_port = 53533
    
    #socket connection
    socket_conn_us = socket(AF_INET, SOCK_DGRAM)
    socket_conn_us.sendto(message.encode(), (server, server_port))
    resp, server_address = socket_conn_us.recvfrom(2048)
    data = literal_eval(json.loads(json.dumps(resp.decode())) )
    #data= json.loads(json.dumps(resp)) 

    message_address=data['VALUE']
    socket_conn_us.close()
    
    #fibonacci
    page='http://{}:{}/fibonacci?number={}'.format(message_address,fs_port,number)
    next_page = urllib.request.urlopen(page)
    
    return next_page.read()  
    
if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=8080, debug=True)