#importing libraries
from faker import Faker
from datetime import datetime
import pandas as pd
import numpy as np
import random


#declaring fake variable
fake = Faker()

#Sales Table
def make_sales(df_subord,df_sku,df_coupons,df_ord):
    
    sales=[]
#     global x_sku
#     global x_cpn
    df_sales= pd.DataFrame(columns=['SubOrder_ID', 'SKU', 'Product_Buying_Price','Product_Selling_Price','Coupon_Code','Discount_Percentage','Delivery_Charge','Tax','SubOrder_Value'])
    
    for i in range(len(df_subord)):
        #print(i,"th record")
        x_subord=df_subord.iloc[i]
        sub_id=x_subord['SubOrder_ID']
        sku=x_subord['SKU']
        x_sku=df_sku[df_sku['SKU']==sku].iloc[0]
        unq_coupons=df_coupons['Coupon_Code'].unique().tolist()
        cpn=fake.random_element(elements=unq_coupons)
        x_cpn=df_coupons[df_coupons['Coupon_Code']==cpn].iloc[0]
        
        #check if coupon can be applied
        if (x_subord['QTY']*x_sku['Product_Selling_Price'])>=x_cpn['Min_Order_Value']:
            
            #check if max discount criteria is met
            if ((x_subord['QTY']*x_sku['Product_Selling_Price'].item()*x_cpn['Percentage_Discount'].item())/100)>x_cpn['Max_Discount'].item():
                sp=x_subord['QTY']*x_sku['Product_Selling_Price']-x_cpn['Max_Discount']
            else:
                sp=x_subord['QTY']*x_sku['Product_Selling_Price']-x_subord['QTY']*x_sku['Product_Selling_Price']*x_cpn['Percentage_Discount']/100
            
        
        #check if delivery charge is 0
#         global ord_id
        
        ord_id=x_subord['Order_ID']
        x_ord=df_ord[df_ord['Order_ID']==ord_id]
        
        if str(x_ord['Shipment_Type'])=='Prime':
            dlv_chrg=0
        else:
            dlv_chrg=float(fake.pydecimal(left_digits=2, right_digits=2, min_value=2, max_value=10))
        
        #Tax
        psp=x_sku['Product_Selling_Price'].max()
        Tax=round(sp*0.02,2)
#         Tax=float(fake.pydecimal(left_digits=2, right_digits=2, min_value=3, max_value=5))
        
        #sub_value=x['SKU']
        fake_sales = {
         'SubOrder_ID':sub_id, 
         'SKU':sku, 
         'Product_Buying_Price':x_sku['Product_Buying_Price'],
         'Product_Selling_Price':x_sku['Product_Selling_Price'],
         'Coupon_Code':cpn,
         'Discount_Percentage':x_cpn['Percentage_Discount'],
         'Delivery_Charge':dlv_chrg,
         'Tax':Tax,
         'SubOrder_Value':sp+Tax+dlv_chrg
                        }
        sales.append(fake_sales)
        
        df_sales = pd.concat([df_sales, pd.DataFrame.from_records([fake_sales])])
#         df_sales=pd.DataFrame(sales)
    
    return df_sales
