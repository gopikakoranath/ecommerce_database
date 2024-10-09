#importing libraries
from faker import Faker
from datetime import datetime
import pandas as pd
import numpy as np
import random

#declaring fake variable
fake = Faker()

#Sub orders table
def make_suborders(num,df_ord,df_sku):
    
    if (num<len(df_ord)):
        raise ValueError("Sub_orders need to be higher than orders")
    else:
        unq_orders=df_ord['Order_ID'].unique().tolist()
        unq_skus=df_sku['SKU'].unique().tolist()
        status=['Processing','Canceled','Order Placed','Delivered','Return']
        fulfilment=['AnyKart','Third Party']
        DID_list=[]
        
        subord=[]
#         pd.DataFrame(columns=['SubOrder_ID','SKU','Order_ID','QTY','Status','SubOrder_Value','Order_Fulfilment','Delivery_ID'])
        
        for value in unq_orders:
            
            ff=fake.random_element(elements=fulfilment)
            if ff=='Third Party':
                DID=''
            else:
                DID=f"55_{'{:2d}'.format(fake.random_number(digits=8))}"
                while DID in DID_list:
                    DID=f"55_{'{:2d}'.format(fake.random_number(digits=8))}"
                DID_list.append(DID)
                    
            
            fake_suborders = {
             'SubOrder_ID':f"{value}_{'{:2d}'.format(fake.random_number(digits=2))}", 
             'SKU':fake.random_element(elements=unq_skus), 
             'Order_ID':value,
             'QTY':fake.random_int(min=1, max=10),
             'Status':fake.random_element(elements=status),
             'Order_Fulfilment':ff,
             'Delivery_ID':DID
            } 
            
            subord.append(fake_suborders)
        
#         global df_subord
        df_subord=pd.DataFrame(subord)
        
#         unq_suborders=subord['SubOrder_ID'].unique().tolist()
        
#         while len(df_subord) < num:
#             oid = np.random.choice(unq_orders)
        for value in unq_orders:
            
            if len(subord) >= num:
                break

            #random select a number i= between 1 and 4
            rnd_n1=fake.random_int(min=1, max=4)
            #if 1, move to next order_id
            if rnd_n1==1:
                pass
            #if not, random toss 0 or 1
            else:
                rnd_n2=fake.random_int(min=0, max=1)
                
                if rnd_n2==0:
                    #if 0, then pick the suborder_id for that order_id, generate a new sku for i records
#                         print(value)
                    unq_suborders=df_subord[df_subord['Order_ID']==value]['SubOrder_ID'].unique().tolist()
                    so_val=fake.random_element(elements=unq_suborders)
                    unq_so_skus=df_subord[df_subord['SubOrder_ID']==so_val]['SKU'].unique().tolist()
                    sub_ff=df_subord[df_subord['SubOrder_ID']==so_val]['Order_Fulfilment'].iloc[0]
                    
                    if sub_ff=='Third Party':
                        del_ID=''
                    else:
                        del_ID=df_subord[df_subord['SubOrder_ID']==so_val]['Delivery_ID'].iloc[0]
                    
                    sub_status=df_subord[df_subord['SubOrder_ID']==so_val]['Status'].iloc[0]

                    for sub_cnt in range(rnd_n1):
                        
                        if len(subord) >= num:
                            break
                        
                        #updated so sku list
                        unq_so_skus=df_subord[df_subord['SubOrder_ID']==so_val]['SKU'].unique().tolist()
                        
                        new_sku=fake.random_element(elements=unq_skus)

                        while new_sku in unq_so_skus:
                            new_sku=fake.random_element(elements=unq_skus)
                            
                        fake_suborders = {
                         'SubOrder_ID':so_val, 
                         'SKU':new_sku, 
                         'Order_ID':value,
                         'QTY':fake.random_int(min=1, max=10),
                         'Status':sub_status,
                         'Order_Fulfilment':sub_ff,
                         'Delivery_ID':del_ID
                        } 

                        subord.append(fake_suborders)
                        #create df and update unq_so_skus and check that list. This could be reason why there is duplication in soborder_ID sku
                        df_subord = pd.concat([df_subord, pd.DataFrame.from_records([fake_suborders])])
#                         df_subord.append(fake_suborders,ignore_index=True)
#                         df_subord=pd.DataFrame(subord)
                else:
                    #if 1, then create a new suborder_id, pick a sku
                    

                    for sub_cnt in range(rnd_n1):
                        unq_so_skus=df_subord[df_subord['Order_ID']==value]['SKU'].unique().tolist()
                        new_sku=fake.random_element(elements=unq_skus)
                        
                        if len(subord) >= num:
                            break
                        
                        #make sure that this sku doesn't exist for this order already
                        while new_sku in unq_so_skus:
                            new_sku=fake.random_element(elements=unq_skus)
                        
                        #make sure that this suborder doesn't already exist
                        unq_so_soid=df_subord[df_subord['Order_ID']==value]['SubOrder_ID'].unique().tolist()
                        new_so_id=f"{value}_{'{:2d}'.format(fake.random_number(digits=2))}"
                        
                        while new_so_id in unq_so_soid:
                            new_so_id=f"{value}_{'{:2d}'.format(fake.random_number(digits=2))}"
                        
                        #check if fulfilled by thirdparty
                        ff=fake.random_element(elements=fulfilment)
                        if ff=='Third Party':
                            DID=''
                        else:
                            DID=f"55_{'{:2d}'.format(fake.random_number(digits=8))}"
                            while DID in DID_list:
                                DID=f"55_{'{:2d}'.format(fake.random_number(digits=8))}"
                        DID_list.append(DID)
                        
                        fake_suborders = {
                         'SubOrder_ID':new_so_id, 
                         'SKU':new_sku, 
                         'Order_ID':value,
                         'QTY':fake.random_int(min=1, max=10),
                         'Status':fake.random_element(elements=status),
                         'Order_Fulfilment':ff,
                         'Delivery_ID':DID
                        } 

                        subord.append(fake_suborders)
#                         df_subord=pd.DataFrame(subord)
                        df_subord = pd.concat([df_subord, pd.DataFrame.from_records([fake_suborders])])
#                         df_subord.append(fake_suborders,ignore_index=True)

#                 df_subord=pd.DataFrame(subord)    
            #make sure that the order_id, suborder_id, sku combination doesn't already exist
            
#         df_subord=pd.DataFrame(subord)    
        return df_subord