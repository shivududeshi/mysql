# import boto3
# import os
# import uuid
from post_payment_mobibooks import PostPaymentToMobibooks
from PaymentData import payment_data

event={
  "cart": {
    "Items": [
      {
        "customer_mobile": "9550163323",
        "transcation_ref": "order_JC61zheRKZyTGd",
        "customer_id": "0cac5e0e-c56c-4c70-9345-93175408d9d5",
        "invoice_amount": "1",
        "pay_status": "PAID",
        "grand_total": "1",
        "item": {
          "defaultimg_url": "https://portalimg.s3.amazonaws.com/products/1(3).jpeg",
          "tax_methods": "GST5OUTPUT",
          "is_mealplan": True,
          "item_id": "7d721055-b8f9-45b0-b3b4-23e591d4e39b",
          "upd_on": "2022-03-27T11:03:20.000Z",
          "qty": "1",
          "item_name": "Wheatgrass Shot - MS",
          "subscription": [
            {
              "isDelivery": True,
              "address": {
                "aline2": "Lakshmi nivas",
                "aline1": "Flat no 102",
                "city": "Hyderabad ",
                "postalcode": "500084",
                "customer_name": "Satya Goli",
                "id": "17c82b72-0416-4053-a6af-9be3df4656bd",
                "state": "Telangana",
                "tag": "Home",
                "community": "1st right towards police battalion colony",
                "customer_id": "0cac5e0e-c56c-4c70-9345-93175408d9d5",
                "landmark": ""
              },
              "notes": "",
              "addon_items": [],
              "meal_type": "B",
              "order_dates": [
                "2022/03/28",
                "2022/03/29",
                "2022/03/30",
                "2022/03/31",
                "2022/04/01",
                "2022/04/02",
                "2022/04/03"
              ]
            },
            {
              "isDelivery": True,
              "address": {
                "aline2": "Lakshmi nivas",
                "aline1": "Flat no 102",
                "city": "Hyderabad ",
                "postalcode": "500084",
                "customer_name": "Satya Goli",
                "id": "17c82b72-0416-4053-a6af-9be3df4656bd",
                "state": "Telangana",
                "tag": "Home",
                "community": "1st right towards police battalion colony",
                "customer_id": "0cac5e0e-c56c-4c70-9345-93175408d9d5",
                "landmark": ""
              },
              "notes": "",
              "addon_items": [],
              "meal_type": "L",
              "order_dates": [
                "2022/03/28",
                "2022/03/29",
                "2022/03/30",
                "2022/03/31",
                "2022/04/01",
                "2022/04/02",
                "2022/04/03"
              ]
            },
            {
              "isDelivery": True,
              "address": {
                "aline2": "Lakshmi nivas",
                "aline1": "Flat no 102",
                "city": "Hyderabad ",
                "postalcode": "500084",
                "customer_name": "Satya Goli",
                "id": "17c82b72-0416-4053-a6af-9be3df4656bd",
                "state": "Telangana",
                "tag": "Home",
                "community": "1st right towards police battalion colony",
                "customer_id": "0cac5e0e-c56c-4c70-9345-93175408d9d5",
                "landmark": ""
              },
              "notes": "",
              "addon_items": [],
              "meal_type": "D",
              "order_dates": [
                "2022/03/28",
                "2022/03/29",
                "2022/03/30",
                "2022/03/31",
                "2022/04/01",
                "2022/04/02",
                "2022/04/03"
              ]
            }
          ],
          "variants": [
            {
              "display_name": "Duration",
              "items": [
                {
                  "display_name": "7 Day"
                }
              ]
            }
          ],
          "category": "Meal Subscription",
          "uom_name": "Units",
          "upd_by": "Admin"
        },
        "id": "1db63e8e-468a-42f2-b8a3-b6ad040d5c9c",
        "customer_name": "Satya Goli",
        "ciid": "c885f50c-5b11-420e-8fc7-30c254053ba7"
      }
    ],
    "Count": 1,
    "ScannedCount": 1496,
    "LastEvaluatedKey": {
      "id": "45761b0d-aef7-4103-95d7-994ecb72e799",
      "ciid": "fc26c326-78f7-474d-a41d-b70124b2bc57"
    },
    "ResponseMetadata": {
      "RequestId": "TSS2VCAASVIIKQ82QENCPEAOCJVV4KQNSO5AEMVJF66Q9ASUAAJG",
      "HTTPStatusCode": 200,
      "HTTPHeaders": {
        "server": "Server",
        "date": "Mon, 06 Jun 2022 10:55:23 GMT",
        "content-type": "application/x-amz-json-1.0",
        "content-length": "3017",
        "connection": "keep-alive",
        "x-amzn-requestid": "TSS2VCAASVIIKQ82QENCPEAOCJVV4KQNSO5AEMVJF66Q9ASUAAJG",
        "x-amz-crc32": "1745961853"
      },
      "RetryAttempts": 0
    }
  },
  "dynamodb": {
    "account_id": "acc_GSBwg76P2m2uWx",
    "event": "payment.authorized",
    "contains": [
      "payment"
    ],
    "date_time": "2022-06-06 10:55:22",
    "id": "b627de94-89af-482b-af62-5b78532bb856",
    "entity": "payment",
    "amount": 100,
    "currency": "INR",
    "status": "authorized",
    "order_id": "order_JC61zheRKZyTGd",
    "invoice_id": None,
    "international": False,
    "method": "upi",
    "amount_refunded": 0,
    "refund_status": None,
    "captured": False,
    "description": None,
    "card_id": None,
    "bank": None,
    "wallet": None,
    "vpa": "9550163323@ybl",
    "email": "satya.goli@mobigesture.com",
    "contact": "+918121153287",
    "notes": {
      "address": "VL"
    },
    "fee": None,
    "tax": None,
    "error_code": None,
    "error_description": None,
    "error_source": None,
    "error_step": None,
    "error_reason": None,
    "acquirer_data": {
      "rrn": "208635972985"
    },
    "created_at": 1648380420,
    "payment_id": "pay_JC62haidW8vjMG",
    "payment_created_at": 1648380409,
    "payment_status": "authorized",
    "payment_amount": 100,
    "customer_name": "Satya Goli",
    "customer_mobile": "9550163323"
  }
}
def lambda_handler(event):
    # try:     
    user_pay=payment_data()
    post_payment_data=user_pay.prepare_payment(event)
    x=PostPaymentToMobibooks()
    x.post_payment(post_payment_data)
    # except Exception as error_message:
    #     client=boto3.client('sqs',region_name=os.environ.get('REGION_NAME'))
    #     customer_id = boto3.client('sts').get_caller_identity()['Account']
    #     queue_name = os.environ.get('ERROR_QUEUE_NAME')
    #     res=client.send_message(QueueUrl=f'https://sqs.us-west-2.amazonaws.com/{customer_id}/{queue_name}',MessageBody=error_message.args[0],MessageGroupId='PaymentError')
    #     print('hiiii')
lambda_handler(event)

