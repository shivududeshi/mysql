import json
from http.cookiejar import CookieJar
from urllib.request import urlopen,build_opener,install_opener,Request
from urllib.request import HTTPCookieProcessor
import traceback
import urllib.request
import time
import traceback
import urllib.error
import sys
from booksexceptions import BooksException
import time
#from django.core import serializers
#from LedgerGroup import LedgerGroup

class Mobibooks:

    def __init__(self,host,user,password,location,cust=None):

        if host is None or user is None or password is None:
            raise Exception("host,user,password can't be nulls")
        self.host = host
        self.url = 'http://' + host +'/act/api/'
        self.base_url = 'http://' + host + '/act/'
        self.user = user
        self.password = password
        self.is_logged_in = False
        self.auth_denied = False
        self.location = location
        self.location_id = None
        self.cust = cust
        self.retry = 1

    def login(self):
        if self.is_logged_in:
            return True
        # Store the cookies and create an opener that will hold them
        cj = CookieJar()
        opener = build_opener(HTTPCookieProcessor(cj))

        # Add our headers
        opener.addheaders = [('Content-Type','application/json; charset=UTF-8')]

        # Install our opener (note that this changes the global opener to the one
        # we just made, but you can also just call opener.open() if you want)
        install_opener(opener)

        # The action/ target from the form
        authentication_url = self.url + 'login/'

        # Input parameters we are going to send
        payload = json.dumps({'mobile': self.user,
            'password': self.password,'device_id':'11111111'}).encode('utf-8')

        # Use urllib to encode the payload
        # data = urllib.urlencode(payload)
        data = payload

        # Build our Request object (supplying 'data' makes it a POST)
        req = Request(authentication_url,
                data,{'Content-Type': 'application/json'})

        # Make the request and read the response
        try:
            cookies_set = False
            resp = urlopen(req)
            contents = resp.read()
            #print(contents)
            res = contents.decode('utf-8')
            o = json.loads(res)

            #import pprint
            #pprint.pprint(o)
            if 'error' in o:
                raise Exception (o['error']['message'] )
            if 'tenant' in o and len(o['tenant']) > 1:
                #print ('Multi-tenant Access, Sent Location Access Request for {0} Location'.format(self.cust))
                for c in cj:
                    if c.name == 'csrftoken':
                        opener.addheaders = [('X-CSRFToken', c.value)]
                o = self.post('second_lg/',{'tenant_name':self.cust,'device_id':'11111111'})
                cookies_set = True
            #import pprint
            #pprint.pprint(o)
            locs = o['location']

            if self.location is None: # assign first available location
                if len(locs) > 0:
                    self.location = locs[0]['display_name']
                    self.location_id = locs[0]['id']
                else:
                    raise Exception('Error: You do not have access to Any location')

            else:
                for l in locs:
                    if self.location == l['display_name']:
                        self.location_id = l['id']
                        #print ("Setting location, ID:{0}".format(self.location_id))
                        break
            if self.location_id is None:
                print('ERROR: You are not allowed to Use the location {0}, Your locations are:'.format(self.location))
                i = 1
                for l in locs:
                    print ("\t\t{0}. {1}".format(i,l['display_name']))
                    i +=1
                sys.exit(1)
            self.is_logged_in = True
            self.user = o
            # set CSRF header
            if not cookies_set:
                for c in cj:
                    if c.name == 'csrftoken':
                        opener.addheaders = [('X-CSRFToken', c.value)]
                    cookies_set = True
        except urllib.error.HTTPError as e:
            if e.code == 401:
                self.auth_denied = True
            print ('Authentication Failure, Reason[{0}]'.format(e.reason))
            raise Exception('Authentication Failure, Reason[{0}]'.format(e.reason))
        except urllib.error.URLError as e:
            print ('Authentication Failure, Reason[{0}]'.format(e.reason))
            raise Exception('Authentication Failure, Reason[{0}]'.format(e.reason))
        except Exception as e:
            #traceback.print_exc()
            raise

    def post(self,url,payload,module='api'):
        url = self.base_url + module + '/' + url
        retry = self.retry
        try:
            data = json.dumps(payload).encode('utf-8')
        except:
            print (payload)
            raise

        for npass in range (retry):
            try:
                req = Request(url,data,{'Content-Type': 'application/json'})
                resp = urlopen(req)
                contents = resp.read()
                res = contents.decode('utf-8')
                if res is None or res == '':
                    return ''
                else:
                    o = json.loads(res)
                    if 'error' in o: #Error Condition
                        raise BooksException(code = o['error']['code'], message = o['error']['message'] )
                    return o
            except BooksException:
                raise
            except:
                if npass == retry - 1:
                    raise
                else:
                    time.sleep(1)
                    print ('Retry url: {0}'.format(url))


    def upload(self, url, fname):
        url = self.base_url + url

        with open(fname, 'rb') as f:
            data = f.read()
        # print (data)
        req = Request(url, data,
                {'Content-Type': '*/*',
                'Content-Disposition':'attachment; filename={0}'.format(fname)})
        resp = urlopen(req)
        contents = resp.read()
        # print(contents)
        res = contents.decode('utf-8')
        if res is None or res == '':
            return ''
        else:
            o = json.loads(res)
            if 'error' in o:  # Error Condition
                raise Exception('ERROR {0}, Reason:{1}'.format(o['error']['code'], o['error']['message']))
            return o

    def zippost(self, url, data,module='api'):
        url = self.base_url + module + '/' + url
        req = Request(url, data,
                {'Content-Type': '*/*',
                'Content-Disposition':'attachment; filename={0}'.format('vouchers.gz')})
        resp = urlopen(req)
        contents = resp.read()
        # print(contents)
        res = contents.decode('utf-8')
        if res is None or res == '':
            return ''
        else:
            o = json.loads(res)
            if 'error' in o:  # Error Condition
                raise Exception('ERROR {0}, Reason:{1}'.format(o['error']['code'], o['error']['message']))
            return o

    def get(self,url,module='api'):
        url = self.base_url + module + '/' + url

        for npass in range (3):
            try:
                req = Request(url,None,{'Content-Type': 'application/json'})
                resp = urlopen(req)
                contents = resp.read()
                res = contents.decode('utf-8')
                if res is None or res == '':
                    return ''
                else:
                    o = json.loads(res)
                    if 'error' in o: #Error Condition
                        raise BooksException(code = o['error']['code'], message = o['error']['message'] )
                    return o
            except BooksException:
                raise
            except:
                if npass == 2:
                    raise
                else:
                    time.sleep(1)
                    print ('Retry url: {0}'.format(url))
#o = Mobibooks('104.131.142.154','9849314444','Pradeep1','WORKSHOP A9')