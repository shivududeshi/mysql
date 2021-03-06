import requests
import datetime
import json
import hmac
import hashlib
import base64
from pycognito import aws_srp

class egoclient:

    def __init__(self,url=None,headers=None,payload=None):
        self.url=url
        self.headers=headers
        self.payload=payload
    

    def login(self,username= None,password=None):

        #get aceess token using user_password_auth
        self.url = 'https://cognito-idp.us-east-1.amazonaws.com'
        self.headers = {
                "x-amz-target": "AWSCognitoIdentityProviderService.InitiateAuth",
                "content-type": "application/x-amz-json-1.1"
                }
        payload={
	    "AuthFlow": "USER_PASSWORD_AUTH",
	    "ClientId": "2m2s4a2m2cn62pb6jfhrarqju1",
	    "AuthParameters": {
		"USERNAME": username,
		"PASSWORD": password
	    }
        }
        self.payload=json.dumps(payload)
        r = requests.post(url=self.url,data=self.payload,headers=self.headers)
        return r.json()['AuthenticationResult']['AccessToken']

        ## get access token using boto3

        # if username is None or password is None:
        #     return "please provide [username] and [password]"
        # elif len(username) == 0 or len(password) == 0:
        #     return "please provide valid [username] and [password]"
        # else:
        #     client = boto3.client('cognito-idp',region_name='us-east-1')
        #     response = client.initiate_auth(
        #         ClientId ='2m2s4a2m2cn62pb6jfhrarqju1',
        #         AuthFlow ='USER_PASSWORD_AUTH',
        #         AuthParameters={
        #             'USERNAME' :  username
        #             ,'PASSWORD' :  password
        #         }
        #     )
        #     self.accesstoken = response['AuthenticationResult']['AccessToken']
        #     return self.accesstoken


        # # get access token using pycognito module

        # u = Cognito('us-east-1_e5uzGdrC6','2m2s4a2m2cn62pb6jfhrarqju1',username=username)
        # u.authenticate(password=password)
        # return u.access_token


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
    
    def add_cart(self,access_token):
        self.url = "https://m76jgm5mv5a5ta56kwht6e6ipm.appsync-api.us-east-1.amazonaws.com/graphql"
        self.headers = {
                'authorization': access_token,
                'Content-Type': 'application/json'
                }
        self.payload = "query":"mutation($input:CreateCartInputu0021){n createCart(input: $input) {n idn customer_idn }n }"
        r = requests.post(url=self.url,data=self.payload,headers=self.headers)
        print(r.status_code)
        print(r.json())
    

    def login_with_srp(self,username= None,password=None):
        
        #get access token using USER_SRP_AUTH

        pool_id='us-east-1_e5uzGdrC6'
        client_id='2m2s4a2m2cn62pb6jfhrarqju1'
        pool_region='us-east-1'

        aws = aws_srp.AWSSRP(
        username=username,
        password=password,
        pool_id=pool_id,
        client_id=client_id,
        pool_region=pool_region
        )
        srp_a =aws.get_auth_params()['SRP_A']
        print(aws.get_auth_params())
        print(help(aws))

        self.url = "https://cognito-idp.us-east-1.amazonaws.com/"
        self.headers={
        "content-type" : "application/x-amz-json-1.1",
        "x-amz-target" : "AWSCognitoIdentityProviderService.InitiateAuth"
        }
        payload ={
            "AuthFlow":"USER_SRP_AUTH",
            "ClientId":client_id,
            "AuthParameters":{
            "USERNAME":username,
            "SRP_A":srp_a
            }
            }
        self.payload=json.dumps(payload)

        res1 = requests.post(url=self.url, headers=self.headers, data=self.payload)
        print('call 1:',res1.status_code)

        srp_b=int(res1.json()['ChallengeParameters']['SRP_B'],16)
        salt=res1.json()['ChallengeParameters']['SALT']
        user_id_for_srp=res1.json()['ChallengeParameters']['USER_ID_FOR_SRP']
        secret_key=res1.json()['ChallengeParameters']['SECRET_BLOCK']
        user_name=res1.json()['ChallengeParameters']['USERNAME']
        time_stamp=datetime.datetime.utcnow().strftime("%a %b %d %H:%M:%S UTC %Y")


        secret_key_bytes = base64.standard_b64decode(secret_key)
        msg = bytearray(pool_id.split('_')[1], 'utf-8') + bytearray(user_id_for_srp, 'utf-8') + \
            bytearray(secret_key_bytes) + bytearray(time_stamp, 'utf-8')
        hkdf = aws.get_password_authentication_key(user_id_for_srp,password,srp_b, salt)
        hmac_obj = hmac.new(hkdf, msg, digestmod=hashlib.sha256)
        signature_string = (base64.standard_b64encode(hmac_obj.digest())).decode()
        self.url = "https://cognito-idp.us-east-1.amazonaws.com/"
        self.headers={
        "content-type" : "application/x-amz-json-1.1",
        "x-amz-target": "AWSCognitoIdentityProviderService.RespondToAuthChallenge"
        }
        payload ={
            "ChallengeName":"PASSWORD_VERIFIER",
            "ClientId":client_id,
            "ChallengeResponses":{
            "USERNAME":user_name,
            "PASSWORD_CLAIM_SECRET_BLOCK":secret_key,
            "TIMESTAMP":time_stamp,
            "PASSWORD_CLAIM_SIGNATURE":signature_string
            }
            }
        self.payload=json.dumps(payload)

        res2 = requests.post(url=self.url, headers=self.headers, data=self.payload)
        print('call 2:',res2.status_code)
        return res2.json()['AuthenticationResult']['AccessToken']


    
    def user_login_with_srp(self,username= None,password=None):
        
        #get access token using USER_SRP_AUTH

        pool_id='us-east-1_LmIBVgrWX'
        client_id='1elqc1ok4eqb1c9sjlhhiq74sd'
        pool_region='us-east-1'

        aws = aws_srp.AWSSRP(
        username=username,
        password=password,
        pool_id=pool_id,
        client_id=client_id,
        pool_region=pool_region
        )
        srp_a =aws.get_auth_params()['SRP_A']

        self.url = "https://cognito-idp.us-east-1.amazonaws.com/"
        self.headers={
        "content-type" : "application/x-amz-json-1.1",
        "x-amz-target" : "AWSCognitoIdentityProviderService.InitiateAuth"
        }
        payload ={
            "AuthFlow":"USER_SRP_AUTH",
            "ClientId":client_id,
            "AuthParameters":{
            "USERNAME":username,
            "SRP_A":srp_a
            }
            }
        self.payload=json.dumps(payload)

        res1 = requests.post(url=self.url, headers=self.headers, data=self.payload)
        print('call 1:',res1.status_code)

        srp_b=int(res1.json()['ChallengeParameters']['SRP_B'],16)
        salt=res1.json()['ChallengeParameters']['SALT']
        user_id_for_srp=res1.json()['ChallengeParameters']['USER_ID_FOR_SRP']
        secret_key=res1.json()['ChallengeParameters']['SECRET_BLOCK']
        user_name=res1.json()['ChallengeParameters']['USERNAME']
        time_stamp=datetime.datetime.utcnow().strftime("%a %b %d %H:%M:%S UTC %Y")


        secret_key_bytes = base64.standard_b64decode(secret_key)
        msg = bytearray(pool_id.split('_')[1], 'utf-8') + bytearray(user_id_for_srp, 'utf-8') + \
            bytearray(secret_key_bytes) + bytearray(time_stamp, 'utf-8')
        hkdf = aws.get_password_authentication_key(user_id_for_srp,password,srp_b, salt)
        hmac_obj = hmac.new(hkdf, msg, digestmod=hashlib.sha256)
        signature_string = (base64.standard_b64encode(hmac_obj.digest())).decode()
        self.url = "https://cognito-idp.us-east-1.amazonaws.com/"
        self.headers={
        "content-type" : "application/x-amz-json-1.1",
        "x-amz-target": "AWSCognitoIdentityProviderService.RespondToAuthChallenge"
        }
        payload ={
            "ChallengeName":"PASSWORD_VERIFIER",
            "ClientId":client_id,
            "ChallengeResponses":{
            "USERNAME":user_name,
            "PASSWORD_CLAIM_SECRET_BLOCK":secret_key,
            "TIMESTAMP":time_stamp,
            "PASSWORD_CLAIM_SIGNATURE":signature_string
            }
            }
        print(f"username: {username}")
        self.payload=json.dumps(payload)

        res2 = requests.post(url=self.url, headers=self.headers, data=self.payload)
        print('call 2:',res2.status_code)
        return res2.json()['AuthenticationResult']['AccessToken']


if __name__=='__main__':
    # try:
    x=egoclient()
    access_token=x.user_login_with_srp(username="+918309665409",password="Asdf@123")
    print(access_token)
    t = input('Enter <item> for item category or <sub> for subcriptions:')
    if t=='item':
        x.item_category()
    elif t=='sub':
        x.subcription(access_token)
    else:
        raise Exception('incorrect method entered, please enter <item> for item category or <sub> for subcriptions.')
    # except Exception as e:
    #     print('Error is :',e)
