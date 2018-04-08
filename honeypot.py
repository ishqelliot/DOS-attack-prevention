from sys import argv
import BaseHTTPServer
import SocketServer

PORT = int(argv[1])

class MyHTTPServer(BaseHTTPServer.BaseHTTPRequestHandler):
    #def handle_one_request(self):
    def do_GET(self):
    
        print(self.client_address[0])
        
 	self.send_response(203,'Success')


	return #BaseHTTPServer.BaseHTTPRequestHandler.handle_one_request(self)



print("Serving local directory")
httpd = SocketServer.TCPServer(("", PORT), MyHTTPServer)

try:
	httpd.serve_forever()

except KeyboardInterrupt:
	pass

print "Closing Server..."

httpd.server_close();
