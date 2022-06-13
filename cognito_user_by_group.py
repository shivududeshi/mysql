from group_users import Users
# import json

event={'groups':['admin','developer']}
# event={'groups':'All'}

if __name__=='__main__':
    try:
        mbg=Users()
        # group=json.loads(event["params"]["querystring"]["groups"])
        group=event["groups"]
        if type(group[0])==str and group[0]=='all':
            group=mbg.all_groups()
        group_user_list=mbg.group_users(group)
        # return group_user_list
    except Exception as error:
        print('Error is: ',error)
