import requests
import datetime
import json
import hmac
import hashlib
import base64
from pycognito import aws_srp
# import boto3
# from pycognito import Cognito

class egoclient:

    def __init__(self,url=None,headers=None,payload=None):
        self.url=url
        self.headers=headers
        self.payload=payload
        self.pool_id='us-east-1_LmIBVgrWX'
        self.client_id='1elqc1ok4eqb1c9sjlhhiq74sd'
    
    def login_with_srp(self,username,password):
        
        #get access token using USER_SRP_AUTH
        aws = aws_srp.AWSSRP(
        username=username,
        password=password,
        pool_id=self.pool_id,
        client_id=self.client_id,
        pool_region=self.pool_id.split('_')[0]
        )
        srp_a =aws.get_auth_params()['SRP_A']

        self.url = "https://cognito-idp.us-east-1.amazonaws.com/"
        self.headers={
        "content-type" : "application/x-amz-json-1.1",
        "x-amz-target" : "AWSCognitoIdentityProviderService.InitiateAuth"
        }
        payload ={
            "AuthFlow":"USER_SRP_AUTH",
            "ClientId":self.client_id,
            "AuthParameters":{
            "USERNAME":username,
            "SRP_A":srp_a
            }
            }
        self.payload=json.dumps(payload)

        res1 = requests.post(url=self.url, headers=self.headers, data=self.payload)
        user_name=res1.json()['ChallengeParameters']['USERNAME']
        secret_key=res1.json()['ChallengeParameters']['SECRET_BLOCK']
        time_stamp=datetime.datetime.utcnow().strftime("%a %b %d %H:%M:%S UTC %Y")


        srp_b=int(res1.json()['ChallengeParameters']['SRP_B'],16)
        salt=res1.json()['ChallengeParameters']['SALT']
        user_id_for_srp=res1.json()['ChallengeParameters']['USER_ID_FOR_SRP']
        secret_key=res1.json()['ChallengeParameters']['SECRET_BLOCK']
        user_name=res1.json()['ChallengeParameters']['USERNAME']
        time_stamp=datetime.datetime.utcnow().strftime("%a %b %d %H:%M:%S UTC %Y")


        secret_key_bytes = base64.standard_b64decode(secret_key)
        msg = bytearray(self.pool_id.split('_')[1], 'utf-8') + bytearray(user_id_for_srp, 'utf-8') + \
            bytearray(secret_key_bytes) + bytearray(time_stamp, 'utf-8')
        hkdf = aws.get_password_authentication_key(user_id_for_srp,password,srp_b, salt)
        hmac_obj = hmac.new(hkdf, msg, digestmod=hashlib.sha256)
        signature_key = (base64.standard_b64encode(hmac_obj.digest())).decode()

        self.url = "https://cognito-idp.us-east-1.amazonaws.com/"
        self.headers={
        "content-type" : "application/x-amz-json-1.1",
        "x-amz-target": "AWSCognitoIdentityProviderService.RespondToAuthChallenge"
        }
        payload ={
            "ChallengeName":"PASSWORD_VERIFIER",
            "ClientId":self.client_id,
            "ChallengeResponses":{
            "USERNAME":user_name,
            "PASSWORD_CLAIM_SECRET_BLOCK":secret_key,
            "TIMESTAMP":time_stamp,
            "PASSWORD_CLAIM_SIGNATURE":signature_key
            }
            }
        self.payload=json.dumps(payload)

        res2 = requests.post(url=self.url, headers=self.headers, data=self.payload)
        return res2.json()['AuthenticationResult']['AccessToken']

    def login(self,username,password):

        #get aceess token using 'user_password_auth' flow with requests module 
        self.url = 'https://cognito-idp.us-east-1.amazonaws.com'
        self.headers = {
                "x-amz-target": "AWSCognitoIdentityProviderService.InitiateAuth",
                "content-type": "application/x-amz-json-1.1"
                }
        payload={
	    "AuthFlow": "USER_PASSWORD_AUTH",
	    "ClientId": self.client_id,
	    "AuthParameters": {
		"USERNAME": username,
		"PASSWORD": password
	    }
        }
        self.payload=json.dumps(payload)
        r = requests.post(url=self.url,data=self.payload,headers=self.headers)
        return r.json()['AuthenticationResult']['AccessToken']

    def login_with_boto3(self,username,password):
        # get access token using boto3
        client = boto3.client('cognito-idp',region_name=self.pool_id.split('_')[0])
        response = client.initiate_auth(
            ClientId =self.client_id,
            AuthFlow ='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME' :  username
                ,'PASSWORD' :  password
            }
        )
        self.accesstoken = response['AuthenticationResult']['AccessToken']
        return self.accesstoken

    def login_with_cognito(self,username,password):
        # get access token using pycognito module

        u = Cognito(self.pool_id,self.client_id,username=username)
        u.authenticate(password=password)
        return u.access_token


    def item_category(self):                
        self.url = "https://ca57f53chjghzmmjskz3e6sptq.appsync-api.us-east-1.amazonaws.com/graphql"
        self.headers = {
                'x-api-key': 'da2-orjjngnz3ffc3jjnn75bfm4roi',
                'Content-Type': 'application/json'
                }
        self.payload="{\"query\":\"{\\n listItemCategories(limit:3) {\\n items {\\n id\\n name\\n display_name\\n description\\n status\\n upd_by\\n upd_on\\n }\\n }\\n }\",\"variables\":{}}"
        r = requests.post(url=self.url,data=self.payload,headers=self.headers)
        print(r.status_code)
        print(r.json())


    def subcription(self,access_token):
        self.url = "https://4du5xi23jneq5gmwctl2vl42ty.appsync-api.us-east-1.amazonaws.com/graphql"
        self.headers = {
                'authorization': access_token,
                'Content-Type': 'application/json'
                }
        self.payload = "{\"query\":\"{listSubscriptions(filter : {from_date: {eq: \\\"2022-04-27\\\"},to_date: {eq: \\\"2022-04-27\\\"},, status: {eq: \\\"A\\\"}, itemperpage: {eq: 10}, pagenumber: {eq: 0}}){\\n item_count\\n items{\\n L_balance\\n B_balance\\n D_balance\\n paid_amount\\n status\\n customer {\\n display_name\\n id\\n mobile\\n name\\n status\\n upd_by\\n upd_on\\n }\\n finish_date\\n id\\n product {\\n category\\n display_name\\n status\\n sale_price\\n name\\n id\\n }\\n start_date\\n upd_by\\n upd_on\\n cartitem_id\\n cart_id\\n orderscount {\\n meal_type\\n meals_consumed\\n meals_ordered\\n meals_remaining\\n meals_pausedORcancelled\\n }\\n }\\n }\\n }\\n\",\"variables\":{}}"
        r = requests.post(url=self.url,data=self.payload,headers=self.headers)
        print(r.status_code)
        print(r.json())
    
    def cart_list(self,access_token):
        self.url = "https://m76jgm5mv5a5ta56kwht6e6ipm.appsync-api.us-east-1.amazonaws.com/graphql"
        self.headers = {
                'authorization': access_token,
                "content-type" : "text/plain"
                }
        payload={
            "query":"""query ($customer_id: ID!){ listCarts(filter: {customer_id: {eq: $customer_id},pay_status:{eq:"UNPAID"}}) {items {customer_id customer_mobile customer_name id ciid grand_total pay_status item {defaultimg_url item_name tax_methods uom_name category item_id sub_total base_price delivery_charge distance discount_amount qty tax_amount subscription {address {aline1 aline2 city tag landmark postalcode}isDelivery meal_type notes order_dates sale_val}variants {display_name items {display_name}}}}grand_total total_tax total_deliverycharge total_discount items_value}}""",
            "variables" : {"customer_id" : "d59e2310-c83f-4c1d-80ca-351504ce64e3"}
            }

        self.payload=json.dumps(payload)
        r = requests.post(url=self.url,data=self.payload,headers=self.headers)
        print(r.status_code)
        print(r.json())
    

    def add_to_cart(self,access_token):

        self.url = "https://m76jgm5mv5a5ta56kwht6e6ipm.appsync-api.us-east-1.amazonaws.com/graphql"
        self.headers = {
        'authorization': access_token,
        "content-type" : "text/plain;charset=UTF-8"
        }
        payload = {
            "query": "mutation ($input: CreateCartInput!){\n  createCart(input: $input) {\n  id\n   customer_id\n  }\n }",
            "variables":"""{"input":{"customer_id":"d59e2310-c83f-4c1d-80ca-351504ce64e3","item":{"item_id":"1ae54853-3cb0-a1f9-bb74-9f8643a55641","qty":1,"subscription":[{"address":{"aline1":"4/440","aline2":"mobigesture","community":"abc ","landmark":"ACB","city":"hyd","state":"telangana","postalcode":"500034","tag":"office","customer_name":"shiva"},"addon_items":[],"isDelivery":true,"meal_type":"B","notes":"","order_dates":["2022/06/29","2022/06/30","2022/07/01","2022/07/02","2022/07/03","2022/07/04","2022/07/05","2022/07/06","2022/07/07","2022/07/08","2022/07/09","2022/07/10","2022/07/11","2022/07/12"]}],"variants":[{"display_name":"Duration","items":{"display_name":"14 Days"}}]}}}"""
            }
        self.payload=json.dumps(payload)

        res = requests.post(url=self.url, headers=self.headers, data=self.payload)
        print(res.status_code)
        print(res.json())
    



