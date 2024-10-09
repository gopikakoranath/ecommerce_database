#importing libraries
from faker import Faker
from datetime import datetime
import pandas as pd
import numpy as np
import random

#import generation modules
from orders import *
from skus import *
from suborders import *
from coupons import *
from sales import *
from delivery import *

#declaring fake variable
fake = Faker()

#Make data
#Orders
orders_df = make_orders(num=900)

#SKUs
SKU_df=make_SKU(num=50)

#Suborders
suborders_df=make_suborders(orders_df,SKU_df,num=1000)

#Coupons
coupons=make_coupons(num=10)

#Sales
sales_df=make_sales(suborders_df,SKU_df,coupons,orders_df)

#Delivery
delivery_df=make_delivery(suborders_df)

#Test
#pd.merge(suborders_df,SKU_df,on=['SKU']).groupby('Order_ID').sum('Product_Selling_Price').to_csv("downloads//order_level.csv")

#update suborders for sales values
updated_suborders=pd.merge(suborders_df,sales_df,on=['SubOrder_ID','SKU'])[['SubOrder_ID','SKU','Order_ID','QTY','Status','SubOrder_Value','Order_Fulfilment','Delivery_ID']]

#update orders with order value
updated_orders=pd.merge(orders_df,pd.merge(orders_df,updated_suborders,on='Order_ID').groupby('Order_ID').sum('SubOrder_Value'),on='Order_ID').rename(columns={"SubOrder_Value":"Order_value"})[['Order_ID','Order_Date','Order_Source','Shipment_Type','Order_value']]

#Export DFs to CSV files
updated_suborders.to_csv("suborders.csv",index=False)
updated_orders.to_csv("orders.csv",index=False)
sales_df.to_csv("sales.csv",index=False)
SKU_df.to_csv("SKUs.csv",index=False)
delivery_df.to_csv("delivery.csv",index=False)
coupons.to_csv("coupons.csv",index=False)