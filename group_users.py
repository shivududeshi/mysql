import boto3
import os
class Users():
    def __init__(self):
        self.client=boto3.client('cognito-idp',region_name=os.environ.get('REGION_NAME'))
        env_vars=(os.environ.get('REGION_NAME'),os.environ.get('user_pool_id'))
        if None in env_vars:
            raise Exception('one/more credentials is/are None')

    def group_users(self,group_list):
        users={}
        group_data=[]
        for group in group_list:
            print(group)
            if type(group) is str and group!='':
                response=self.client.list_users_in_group(UserPoolId=os.environ.get('user_pool_id'),GroupName=group)
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
                    UserPoolId=os.environ.get('user_pool_id'),
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
                raise Exception('Incorrect datatype of group or empty group')
        users['users']=group_data
        return users
    

    def all_groups(self):
        response=self.client.list_groups(UserPoolId=os.environ.get('user_pool_id'),Limit=60)
        grp_list=[]
        for grp in response['Groups']:
            grp_list.append(grp['GroupName'])
        while 'NextToken' in response:
            response=self.client.list_groups(UserPoolId=os.environ.get('user_pool_id'),Limit=60,NextToken=response['NextToken'])
            for grp in response['Groups']:
                grp_list.append(grp['GroupName'])
        return grp_list

