from sys import argv
import BaseHTTPServer
import SocketServer
import threading
import time
import sys

#import secondscounter

suspects=[] #To store the possible DOS attack suspects
clients={} #This dictionary stores the IP addresses of the clients and the number of times they have accessed the server per second
requestLimit = 2 # No. of maximum requests in timeInterval seconds before redirection
timeInterval = 5
PORT = int(argv[1])
HONEYPORT = argv[2]

def clearclients():
	clients.clear()
	
class SecondCounter(threading.Thread):
    '''
    create a thread object that will do the counting in the background
    default interval is 1/1000 of a second
    '''
    def __init__(self, interval=0.001):
        # init the thread
        threading.Thread.__init__(self)
        self.interval = interval  # seconds
        # initial value
        self.value = 0
        # controls the while loop in method run
        self.alive = False

    def run(self):
        '''
        this will run in its own thread via self.start()
        '''
        self.alive = True
        while self.alive:
            time.sleep(self.interval)
            # update count value
            self.value += self.interval
            
            if int(self.value) % timeInterval ==0:
            	clearclients()
            	#print 'clearclients() called'

    def peek(self):
        '''
        return the current value
        '''
        return self.value

    def finish(self):
        '''
        close the thread, return final value
        '''
        # stop the while loop in method run
        self.alive = False
        return self.value

class MyHTTPServer(BaseHTTPServer.BaseHTTPRequestHandler):
    #def handle_one_request(self):
    def do_GET(self):
    
        
        if self.client_address[0] not in clients:
    		clients[self.client_address[0]]=1
    	else:
    		clients[self.client_address[0]]+=1
	print 'requests: ' + clients[self.client_address[0]]
    	if clients[self.client_address[0]]>requestLimit:
	    	#self.send_response(401,'Request Limit Reached')
	    	self.send_response(303)
	       	self.send_header('Location','http://127.0.0.1:'+HONEYPORT)#8011') 'http://127.0.0.1:8010
  	        self.end_headers()    			
	else:
		self.send_response(202,'Success')
				

		print self.address_string() + ' - ' + self.log_date_time_string() # + ' ' + format%args

	        print(self.client_address[0])


	#print clients[self.client_address[0]]

	return #BaseHTTPServer.BaseHTTPRequestHandler.handle_one_request(self)


    def log_message(self, format, *args):
	return
	 	

counter = SecondCounter()
counter.start()


print("Serving local directory")
httpd = SocketServer.TCPServer(("", PORT), MyHTTPServer)

try:
	#print counter.peek()
	httpd.serve_forever()

except KeyboardInterrupt:
	pass
#print counter.peek()
print "Closing Server..."

httpd.server_close();
