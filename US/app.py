from email import message
from urllib.request import urlopen
from flask import Flask
from flask import request
from socket import *
import json

app = Flask(__name__)


@app.route('/fibonacci', methods=['GET'])
def fibonacci(n):
    args = request.args
    # for k, v in args.items():
    #     print(f"{k}: {v}")
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
        return '400'
        
    message_str = {
        'TYPE': 'A',
        'NAME': hostname
        }
    message = json.dump(message_str)
    
    server = as_ip
    server_port = 53533
    
    #socket connection
    socket_conn_us = socket(AF_INET, SOCK_DGRAM)
    socket_conn_us.sendto(message.encode(), (server, server_port))
    resp, server_address = socket_conn_us.recvfrom(2048)
    infor= json.loads(resp.decode())
    message_address=infor['VALUE']
    socket_conn_us.close()
    
    #fibonacci
    page='http://{}:{}/fibonacci?number={}'.format(message_address,fs_port,number)
    next_page = urlopen(page)
    
    return next_page.read()  
    
    
app.run(host='0.0.0.0', port=8080, debug=True)