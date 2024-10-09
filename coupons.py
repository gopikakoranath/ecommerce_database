#importing libraries
from faker import Faker
from datetime import datetime
import pandas as pd
import numpy as np
import random

#declaring fake variable
fake = Faker()

#Coupons table
def make_coupons(num):
    
    st_start_date = datetime.strptime('2022-08-01', '%Y-%m-%d').date()
    st_end_date = datetime.strptime('2022-08-05', '%Y-%m-%d').date()

    ed_start_date = datetime.strptime('2023-01-01', '%Y-%m-%d').date()
    ed_end_date = datetime.strptime('2023-01-05', '%Y-%m-%d').date()
    

    
    fake_coupons=[]
    cpn_list=[]
    
    for i in range(num):
        
        PD=float(fake.pydecimal(left_digits=2, right_digits=2, min_value=5, max_value=10))
        MV=float(fake.random_int(min=200, max=499))
        cpn=fake.lexify(text='????').upper() +'_'+ str(round(PD))
        
        while cpn in cpn_list:
            cpn=fake.lexify(text='????').upper() +'_'+ str(round(PD))
        
        fake_coupons_dict = {'Coupon_Code':cpn, 
             'Percentage_Discount':PD,
             'Min_Order_Value':MV,
             'Max_Discount':fake.random_int(min=int(round(MV*0.05+(MV*PD)/100)), max=int(round(MV*0.1+(MV*PD)/100))),
             'Coupon_Start_Date':fake.date_between_dates(date_start=st_start_date, date_end=st_end_date),
             'Coupon_End_Date':fake.date_between_dates(date_start=ed_start_date, date_end=ed_end_date)
            }
        
        fake_coupons.append(fake_coupons_dict)
        cpn_list.append(cpn)
    
    df_coupons=pd.DataFrame(fake_coupons)
    

    return df_coupons
