import urllib.parse
import urllib.request
import settings
import sys, json

# Load the data that PHP sent us
try:
    data = json.loads(sys.argv[1])
    print ('hello'+ data['name']);	
except:
    print ("nigu");
    sys.exit(1)

# Generate some data to send to PHP
result = {'status': 'Yes!'}

# Send it to stdout (to PHP)
print(json.dumps(result));


a="https://api.clickatell.com/http/sendmsg?user=sunnyrajkotiya&password=PASSWORD&api_id=3476725&to=917667839974&text=Test"
b='https://api.clickatell.com/http/sendmsg'
try:	
	
	print ("Here it is 1 <br/>")
	#params = {'user': 'sunnyrajkotiya','password': 'HGgDMMgUYeMRfS','api_id': 'RSVP01','to': '918124612664','text':'Test'	}
	print ("Here it is 2 <br/>");
	username=settings.username
	print ("Here it is 3.11 <br/>");
	password=settings.password
	print ("Here it is 3.12 <br/>");
	apiid=settings.apiid
	print ("Here it is 3.2 <br/>");
	tom=data['number']
	print ("Here it is 3.3 <br/>");
	#to=settings.to
	text=settings.text
	print ("Here it is 3.4 <br/>");
	url_values="user="+username+"&password="+password+"&api_id="+apiid+"&to="+tom+"&text="+text
	print ("Here it is 3.41 <br/>");
	print (url_values)
	print ("Here it is 3.5 <br/>");
	print (url_values)
	print ("Here it is 4 <br/>");
	
	print ("Here it is 5 <br/>");
	fullurl= b+'?'+url_values
	print ("Here it is 6 <br/>");
	print(fullurl)
	#datavar=urllib.request.urlopen(fullurl)	
	print ("Here it is 7 <br/>");
	#response=datavar.read()
	print ("successfull <br/>");
	
except:
	print ("nigu error");
   
'''response = urllib.urlopen(a)
result = succeed('message sent to: %s' % form['recipient_addr'])
'''