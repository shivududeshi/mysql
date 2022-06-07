import os
import uuid
# import json
import boto3
from boto3.dynamodb.conditions import Attr

class payment_data:
    def __init__(self):
        self.dynamoDbUrl = os.environ.get('DYNAMODBURL')
        self.dynamodb = boto3.resource('dynamodb',region_name=os.environ.get('REGION_NAME'))

    def prepare_payment(self,data):
        print('prepare_json-{}'.format(data))
        pay_obj = {}
        pay_obj["force_isverified"] = False
        pay_obj["is_multi_loc_vou"] = False
        pay_obj["force"] = False
        pay_obj["unique_key"] = str(uuid.uuid4())
        pay_obj["location_id"] = os.environ.get('LOCATION_ID')
        pay_obj["v_id"] = 0
        pay_obj["credit_period"] = None
        pay_obj["generalledger_id"] = os.environ.get('GENERAL_LEDGER_ID')
        pay_obj["GLines"] = self.GLinesData(data)
        pay_obj["amount"] = data["dynamodb"]["payment_amount"]
        pay_obj["isverified"] = False
        pay_obj["ismodified"] = False
        pay_obj["output_pos"] = 0
        pay_obj["input_pos"] = 0
        pay_obj["refname"] = "Vibrant Living Foods"
        pay_obj["brs_id"] = 0
        pay_obj["server_brs_date"] = ''
        pay_obj["transdate"] = data["dynamodb"]["date_time"].split()[0]
        pay_obj["tx_type"] = "BR"
        pay_obj["roundoffamt"] =  0.0

        return pay_obj
    

    def GLinesData(self,data):
        customer=self.getCustomerByName(data["dynamodb"]["customer_name"])
        customer_id=int(customer['sl_id'])
        Glines = []
        seq=1
        for item in data['cart']['Items']:
            Gline={}
            Gline["gu_id"]="00000000-0000-0000-0000-000000000000"
            Gline["seq"]=seq
            Gline["generalledger_id"]=1010
            Gline["location_id"]=1
            Gline["subledger_id"]=customer_id
            Gline["narration"]=''
            Gline["line_id"]=0
            Gline["brs_date"]=None
            Gline["amount"]=item['grand_total']
            seq+=1
            Glines.append(Gline)
        return Glines


    def getCustomerByName(self,customer_name):
        customer_name = ''.join(e.upper() for e in customer_name if e.isalnum())
    
        item_table = self.dynamodb.Table('Customer')
        response = item_table.scan(
            FilterExpression=Attr('name').eq(customer_name)
        )
        if response['Count'] > 0:
            return response['Items'][0]
        else:
            return ''