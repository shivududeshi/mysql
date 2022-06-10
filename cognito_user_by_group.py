from vl_users import VL_Users

if __name__=='__main__':
    try:
        vl=VL_Users()
        group=input('Enter group name to get users:').strip().split(',')
        group_user_list=vl.group_users(group)
        print(f'users of given groups: ',group_user_list)
    except Exception as error:
        print('Error is: ',error)
