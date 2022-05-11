import requests
# import boto3
import srp
import json
from pycognito import Cognito
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

        #get access token using boto3

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


        #get access token using pycognito module

        # u = Cognito('us-east-1_e5uzGdrC6','2m2s4a2m2cn62pb6jfhrarqju1',username="vltest1@gmail.com")
        # u.authenticate(password="Test@1234")
        # return u.access_token

        #get access token using USER_SRP_AUTH

        # srp_user = srp.User(username,password)
        # abc,srp_a_bytes = srp_user.start_authentication()
        # srp_a_hex =srp_a_bytes.hex()

        # self.url = "https://cognito-idp.us-east-1.amazonaws.com/"
        # self.headers={
        # "content-type" : "application/x-amz-json-1.1",
        # "x-amz-target" : "AWSCognitoIdentityProviderService.InitiateAuth"
        # }
        # payload ={
        #     "AuthFlow":"USER_SRP_AUTH",
        #     "ClientId":"2m2s4a2m2cn62pb6jfhrarqju1",
        #     "AuthParameters":{
        #     "USERNAME":username,
        #     "SRP_A":srp_a_hex
        #     }
        #     }
        # self.payload=json.dumps(payload)

        # r = requests.post(url=self.url, headers=self.headers, data=self.payload)
        # print(r.status_code)
        # print('')
        # secret_key=r.json()['ChallengeParameters']['SECRET_BLOCK']
        # user_name=r.json()['ChallengeParameters']['USERNAME']
        # pool_id='_e5uzGdrC6'
        # user_id_for_srp=r.json()['ChallengeParameters']['USER_ID_FOR_SRP']


        # self.url = "https://cognito-idp.us-east-1.amazonaws.com/"
        # self.headers={
        # "content-type" : "application/x-amz-json-1.1",
        # "x-amz-target": "AWSCognitoIdentityProviderService.RespondToAuthChallenge"
        # }
        # payload ={
        #     "ChallengeName":"PASSWORD_VERIFIER",
        #     "ClientId":"2m2s4a2m2cn62pb6jfhrarqju1",
        #     "ChallengeResponses":{
        #     "USERNAME":user_name,
        #     "PASSWORD_CLAIM_SECRET_BLOCK":secret_key,
        #     "TIMESTAMP":"Tue May 10 05:00:06 UTC 2022",
        #     "PASSWORD_CLAIM_SIGNATURE":"DDrdOVFR3Y2+hlR33b6pu+1bSLVKjeKJQe+xtvINwOs="
        #     }
        #     }
        # self.payload=json.dumps(payload)

        # res = requests.post(url=self.url, headers=self.headers, data=self.payload)
        # print(res.status_code)
        # print(res.json())
   


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


if __name__=='__main__':
    try:
        x=egoclient()
        access_token=x.login(username="vltest1@gmail.com",password="Test@1234")
        t = input('Enter <item> for item category or <sub> for subcriptions:')
        if t=='item':
            x.item_category()
        elif t=='sub':
            x.subcription(access_token)
        else:
            raise Exception('incorrect method entered, please enter <item> for item category or <sub> for subcriptions.')
    except Exception as e:
        print('Error is :',e)
