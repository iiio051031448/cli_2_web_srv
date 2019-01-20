from socket import *
import time
import json


class CshClient():
    port = 28111
    host = '192.168.199.240'
    client = None
    BUFFSIZE=1024

    def __init__(self, host='192.168.199.240', port=28111):
        self.host = host
        self.port = port
        self.client = socket(AF_INET, SOCK_STREAM)
        self.addr = (self.host, self.port)
        self.client.connect(self.addr)

    def __del__(self):
        self.client.close()

    def req(self, req_data):
        req_json = json.dumps(req_data)
        self.client.send(req_json.encode())
        data = self.client.recv(self.BUFFSIZE).decode()
        return data


if __name__=="__main__":
    csh_client = CshClient()

    req = {"path": "stadb.s", "arguments": ""}
    data = csh_client.req(req)
    print(data)
    del csh_client

