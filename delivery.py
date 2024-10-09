#importing libraries
from faker import Faker
from datetime import datetime
import pandas as pd
import numpy as np
import random

#declaring fake variable
fake = Faker()

#Delivery table
def make_delivery(df_subord):
    
    delivery=[]
    unq_delivery=df_subord[df_subord['Delivery_ID']!='']['Delivery_ID'].unique().tolist()
    print(len(df_subord))
    print(len(unq_delivery))
    unq_proc_st=['In Transit','Packed','Out for Delivery','Shipped']
    
    for value in unq_delivery:
        so_val=df_subord[df_subord['Delivery_ID']==value]['SubOrder_ID'].iloc[0]
        status_val=df_subord[df_subord['Delivery_ID']==value]['Status'].iloc[0]
        
        base_status=['Canceled','Delivered','Return','Order Placed']
        
        if status_val in base_status:
            del_status=status_val
        else:
            del_status=fake.random_element(elements=unq_proc_st)
            
        fake_delivery={
            'Delivery_ID':value,
#             'SubOrder_ID':so_val,
            'Warehouse_ID':f"WH_{'{:2d}'.format(fake.random_number(digits=4))}",
            'Status':del_status
        }
        delivery.append(fake_delivery)
        
    df_delivery=pd.DataFrame(delivery)
    
    return df_delivery
