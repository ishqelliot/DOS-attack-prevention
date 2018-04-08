from sys import argv
import urllib2

PORT = argv[1]
urllib2.urlopen('http://192.168.43.197:'+PORT)

#import httplib

#conn = httplib.HTTPConnection("192.168.43.218:8000")
#i=1;
#while i<2 :
#	conn.request("HEAD","/index.html")
#	res = conn.getresponse()
#print res.status, res.reason
