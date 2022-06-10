import boto3
import os
class VL_Users():
    def __init__(self):
        self.client=boto3.client('cognito-idp',region_name=os.environ.get('REGION_NAME'),aws_access_key_id=os.environ.get('aws_access_key_id'),aws_secret_access_key=os.environ.get('aws_secret_access_key'))
        self.pool_id=os.environ.get('user_pool_id')
        env_vars=(os.environ.get('REGION_NAME'),os.environ.get('aws_access_key_id'),os.environ.get('aws_secret_access_key'),os.environ.get('user_pool_id'))
        if None in env_vars:
            raise Exception('one/more credentials is/are None')

    def group_users(self,group_list):
        users={}
        group_data=[]
        for group in group_list:
            if type(group) is str and group!='':
                response=self.client.list_users_in_group(UserPoolId=self.pool_id,GroupName=group)
                for user in response['Users']:
                    user_data={}
                    user_data['role']=group
                    user_data['username']=user['Username']
                    user_data['userstatus']=user['UserStatus']
                    for att in user['Attributes']:
                        user_data[att['Name']]=att['Value']
                    group_data.append(user_data)
        
                while 'NextToken' in response:
                    response = self.client.list_users_in_group(
                    UserPoolId=self.pool_id,
                    Limit=60,
                    GroupName=self.group_name,
                    NextToken=response['NextToken'])

                    for user in response['Users']:
                        user_data={}
                        user_data['username']=user['Username']
                        user_data['userstatus']=user['UserStatus']
                        for att in user['Attributes']:
                            user_data[att['Name']]=att['Value']
                        group_data.append(user_data)
       
            else:
                name=input('Please enter group name: ').strip().split(',')
                return self.group_users(name)
        users['users']=group_data
        return users