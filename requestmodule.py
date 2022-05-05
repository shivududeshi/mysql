import requests

class egoclient:

    def __init__(self):
        self.url = "https://ca57f53chjghzmmjskz3e6sptq.appsync-api.us-east-1.amazonaws.com/graphql"

        self.headers = {
        'x-api-key': 'da2-orjjngnz3ffc3jjnn75bfm4roi',
        'Content-Type': 'application/json'
        }

        self.payload="{\"query\":\"{\\n listItemCategories(limit:3) {\\n items {\\n id\\n name\\n display_name\\n description\\n status\\n upd_by\\n upd_on\\n }\\n }\\n }\",\"variables\":{}}"
    def get_method(self):
        pass
    def post_method(self):
        r = requests.post(url=self.url,data=self.payload,headers=self.headers)
        print(r.status_code)
        print(r.json())
        # print(help(r))
        # print(r.content)
        # print(self.r.text)


x=egoclient()
x.post_method()

