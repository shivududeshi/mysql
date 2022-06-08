
import os
from Mobibooks import Mobibooks
from booksexceptions import BooksException

class PostPaymentToMobibooks:

    def __init__(self):
        self.loc = os.environ.get('MOBI_LOCATION')
        self.user = os.environ.get('MOBI_USER')
        self.password = os.environ.get('MOBI_PASSWORD')
        self.host = os.environ.get('MOBI_HOST')
        self.cust = os.environ.get('MOBI_CUSTOMER')
        
    def post_payment(self,payment_data):
        if payment_data is None or len(payment_data)==0 or type(payment_data)!=dict:
            raise Exception('incorrect input data format to "post_payment" method,required format is none empty dict')
        # connect to mobibibooks
        o = Mobibooks(self.host,self.user,self.password,self.loc,self.cust)
        # login
        o.login()
        # post and print payment
        # print(voucher)
        resp = o.post('voucher/receipt/',payment_data)
        if 'voucher_id' in resp:
            return resp
        elif 'error' in resp:
            raise Exception(f"payment posting to mobibooks had error and the error is: {resp}")
        
        #need to check when respone will return empty string
        
        # elif resp=='':
        #     #pending
        #     raise Exception('')
        
        
