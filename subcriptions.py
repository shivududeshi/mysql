import requests
from item_categories import egoclient

def post_method():
    x=egoclient()
    access_token=x.login('vltest1@gmail.com','Test@1234')
    url = "https://4du5xi23jneq5gmwctl2vl42ty.appsync-api.us-east-1.amazonaws.com/graphql"
    headers = {
            'authorization': access_token,
            'Content-Type': 'application/json'
            }
    payload = "{\"query\":\"{listSubscriptions(filter : {from_date: {eq: \\\"2022-04-27\\\"},to_date: {eq: \\\"2022-04-27\\\"},, status: {eq: \\\"A\\\"}, itemperpage: {eq: 10}, pagenumber: {eq: 0}}){\\n item_count\\n items{\\n L_balance\\n B_balance\\n D_balance\\n paid_amount\\n status\\n customer {\\n display_name\\n id\\n mobile\\n name\\n status\\n upd_by\\n upd_on\\n }\\n finish_date\\n id\\n product {\\n category\\n display_name\\n status\\n sale_price\\n name\\n id\\n }\\n start_date\\n upd_by\\n upd_on\\n cartitem_id\\n cart_id\\n orderscount {\\n meal_type\\n meals_consumed\\n meals_ordered\\n meals_remaining\\n meals_pausedORcancelled\\n }\\n }\\n }\\n }\\n\",\"variables\":{}}"
    r = requests.post(url=url,data=payload,headers=headers)
    print(r.status_code)
    print(r.request.headers['authorization'])
    print(r.json())

# post_method()

from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session
client_id = '2m2s4a2m2cn62pb6jfhrarqju1'
client_secret = 'USER_PASSWORD_AUTH'
username = 'vltest1@gmail.com'
password = 'Test@1234'
oauth = OAuth2Session(client=LegacyApplicationClient(client_id=client_id))
token = oauth.fetch_token(token_url="https://4du5xi23jneq5gmwctl2vl42ty.appsync-api.us-east-1.amazonaws.com/graphql",
        username=username, password=password, client_id=client_id)
print(token)
