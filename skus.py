#importing libraries
from faker import Faker
from datetime import datetime
import pandas as pd
import numpy as np
import random

#declaring fake variable
fake = Faker()

#Make SKUs table
def make_SKU(num):
    
    Product_Category=['Food','Clothing and Apparel','Home Supplies']
    
    Fd_subcat=['Frozen','Bakery','Groceries','Meat']
    CA_subcat=["Men's Clothing","Women's Clothing","Kids"]
    HS_subcat=["Pet Supplies","Utensils","Accessories","Cleaning"]
    
    Fd_Manf=['Mestle','Nyson','Allogs']
    CA_Manf=['MK','CK','H&M']
    HS_Manf=['Turina','PawLuv','PetLove']
    
    fake_SKUs=[]
    
    SKU_list=[]
    for i in range(num):
        Bp=fake.random_int(min=10, max=499)
        PC=fake.random_element(elements=Product_Category)
        SKU='SKU_' + fake.numerify('####')
        
        while SKU in SKU_list:
            SKU='SKU_' + fake.numerify('####')
                
        fake_SKUs_dict={'SKU':SKU,
             'Product_Category':PC,
             'Product_Sub_Category':fake.random_element(elements=Fd_subcat) if PC=='Food' else (fake.random_element(elements=CA_subcat) if PC=='Clothing and Apparel' else fake.random_element(elements=HS_subcat)),
             'Product_Color':fake.color_name() if PC=='Clothing and Apparel' or PC=='Home Supplies' else None,
             'Product_Manufacturer':fake.random_element(elements=Fd_Manf) if PC=='Food' else (fake.random_element(elements=CA_Manf) if PC=='Clothing and Apparel' else fake.random_element(elements=HS_Manf)),
             'Product_Buying_Price':Bp,
             'Product_Selling_Price':fake.random_int(min=Bp+1, max=500)
            }
        
        SKU_list.append(SKU)
        fake_SKUs.append(fake_SKUs_dict)

    df_SKUs=pd.DataFrame(fake_SKUs)
    
    return df_SKUs
