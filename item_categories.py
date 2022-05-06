import requests
import boto3
class egoclient:

    def __init__(self,url=None,headers=None,payload=None):
        self.url=url
        self.headers=headers
        self.payload=payload
    

    def login(self,username= None,password=None):
        if username is None or password is None:
            return "please provide [username] and [password]"
        elif len(username) == 0 or len(password) == 0:
            return "please provide valid [username] and [password]"
        else:
            client = boto3.client('cognito-idp',region_name='us-east-1')
            response = client.initiate_auth(
                ClientId ='2m2s4a2m2cn62pb6jfhrarqju1',
                AuthFlow ='USER_PASSWORD_AUTH',
                AuthParameters={
                    'USERNAME' :  username
                    ,'PASSWORD' :  password
                }
            )
            self.accesstoken = response['AuthenticationResult']['AccessToken']
            return self.accesstoken


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


    def subcription(self):
        access_token=self.login('vltest1@gmail.com','Test@1234')
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
        x.item_category()
        print('')
        x.subcription()
    except Exception as e:
        print('Error is :',e)
