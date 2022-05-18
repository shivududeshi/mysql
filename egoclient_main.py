from Egoclient import egoclient
import time

if __name__=='__main__':
    try:
        obj=egoclient()
        method = (input("Enter <item> for 'item category' or <sub> for 'subcriptions' or <cart> for 'cart items' or <addcart> for 'add to cart': ")).lower()
        if method=='item':
            obj.item_category()
        elif method in ['sub','cart','addcart']:
            username,password=tuple(input('Enter <username,password> credentials: ').split(','))
            access_token=obj.login_with_srp(username=username,password=password)
            if method=='addcart':
                t1=time.time()
                obj.add_to_cart(access_token)  
                t2=time.time()
                print(f"time taken for 'add to cart' operation:{(t2-t1):.2f} seconds")
            elif method=='cart':
                obj.cart_list(access_token)
            else:
               obj.subcription(access_token) 
        else:
            raise Exception('incorrect method entered, please enter <item> for item category or <sub> for subcriptions or <cart> for cart items.')
    except Exception as e:
        print('Error is :',e)