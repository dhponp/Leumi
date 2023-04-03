import requests
import SocketServer
from BaseHTTPServer import BaseHTTPRequestHandler
import sys

print(f"Hi Leumi starting")

def print_function():
    print "Hi Leumi from handler"

class HttpsHandler(BaseHTTPRequestHandler):
    def do_GET(self):         
        print_function()

        self.send_response(200)

httpd = SocketServer.TCPServer(("", 443), HttpsHandler)
httpd.serve_forever()