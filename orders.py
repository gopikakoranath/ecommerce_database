#importing libraries
from faker import Faker
from datetime import datetime
import pandas as pd
import numpy as np
import random

#declaring fake variable
fake = Faker()

#fake orders - except order_value
def make_orders(num):
    
    start_date = datetime.strptime('2022-09-01', '%Y-%m-%d').date()
    end_date = datetime.strptime('2022-12-31', '%Y-%m-%d').date()

    order_source=['Others','AnyKart.Com']
    shpmt_typ=['Prime','Standard']
    fake_orders=[]
    Ord_list=[]
    
    for x in range(num):
        Ord_ID='AKT_' + fake.numerify('########')
        
        while Ord_ID in Ord_list:
            Ord_ID='AKT_' + fake.numerify('########')
        
        fake_orders_dict = {'Order_ID':Ord_ID, 
             'Order_Date':fake.date_between_dates(date_start=start_date, date_end=end_date),
             'Order_Source':fake.random_element(elements=order_source),
             'Shipment_Type':fake.random_element(elements=shpmt_typ)
            } 
        
        Ord_list.append(Ord_ID)
        fake_orders.append(fake_orders_dict)
    
    df_ord=pd.DataFrame(fake_orders)
    
    return df_ord