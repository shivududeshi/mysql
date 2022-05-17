from Egoclient import egoclient

if __name__=='__main__':
    try:
        obj=egoclient()
        method = (input('Enter <item> for item category or <sub> for subcriptions or <cart> for cart items: ')).lower()
        if method=='item':
            obj.item_category()
        elif method in ['sub','cart']:
            username,password=tuple(input('Enter <username,password> credentials: ').split(','))
            access_token=obj.login_with_srp(username=username,password=password)
            if method=='cart':
                obj.add_cart(access_token)  
            else:
               obj.subcription(access_token) 
        else:
            raise Exception('incorrect method entered, please enter <item> for item category or <sub> for subcriptions or <cart> for cart items.')
    except Exception as e:
        print('Error is :',e)