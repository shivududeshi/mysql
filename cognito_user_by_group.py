import boto3
import os

class VL_Users():
    def __init__(self,group_name=None):
        self.client=boto3.client('cognito-idp',region_name=os.environ.get('REGION_NAME'),aws_access_key_id=os.environ.get('aws_access_key_id'),aws_secret_access_key=os.environ.get('aws_secret_access_key'))
        self.pool_id=os.environ.get('user_pool_id')
        # self.group_name=group_name
        # if self.group_name is None:
        #     response = self.client.list_users(
        #     UserPoolId=self.pool_id,
        #     AttributesToGet=['name','phone_number'],
        #     Limit=60)
        # elif type(self.group_name) is str:


    def users(self):
        response = self.client.list_users(
            UserPoolId=self.pool_id,
            AttributesToGet=['name','phone_number'],
            Limit=60)
        users_data=[]
        for user in response['Users']:
            user_data={}
            user_data['username']=user['Username']
            user_data['userstatus']=user['UserStatus']
            for att in user['Attributes']:
                user_data[att['Name']]=att['Value']
            users_data.append(user_data)
        
        while response['PaginationToken']:
            response = self.client.list_users(
            UserPoolId=self.pool_id,
            AttributesToGet=['name','phone_number'],
            Limit=60,
            PaginationToken=response['PaginationToken'])

            for user in response['Users']:
                user_data={}
                user_data['username']=user['Username']
                user_data['userstatus']=user['UserStatus']
                for att in user['Attributes']:
                    user_data[att['Name']]=att['Value']
                users_data.append(user_data)
            if 'PaginationToken' not in response:
                break
        return users_data

    def group_users(self):
        r=self.client.list_users_in_group(UserPoolId=self.pool_id,GroupName=self.group_name)

if __name__=='__main__':
    x=VL_Users()
    y=x.users()
    print('y is:',y)
    # z=x.group_users('Customer')
    # print('z is:',z)