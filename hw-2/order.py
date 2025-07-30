import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import pandas as pd
import arabic_reshaper 
from bidi.algorithm import get_display

dataset = pd.read_csv("orders.csv")
# print(dataset)
print(dataset.columns) #ابتدا داده و مشخصاتشان ها را بررسی میکنیم
print(dataset["Quantity_item"].sum())

tehran_count = dataset["city_name_fa"].value_counts().get('تهران', 0)
print(tehran_count)#چون مثلا تهران پایتخته ببینیم چنتا سفارش داشته در کل
unique_cities = dataset['city_name_fa'].dropna().unique()
city_count = len(unique_cities)
print(city_count)#در کل اسم همه ی شهر ها و تعدادشون

def fix_farsi(text):
    reshaped = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped)
    return bidi_text

# for city in unique_cities:
#     print(fix_farsi(city))#اسم شهر ها رو تمیز کردیم با تابعfix_farsi

num= dataset.select_dtypes(include='number')
print(num.where(num["Amount_Gross_Order"]==num["Amount_Gross_Order"].max()).dropna()["ID_Item"])
#آیدی اون کالایی که بیشترین قیمت خالص رو داشته 

counts = dataset['ID_Customer'].value_counts()
print(counts)
duplicates = counts[counts > 1]
print(duplicates)#یعنی از کل مشتری ها 28700 تاشون بیش از دو خرید در فایل orders داشتند


data= dataset[dataset['city_name_fa'] == 'تهران']
mean_quantity = data['Quantity_item'].mean()
print(mean_quantity)#یعنی به طور متوسط هر سفارش تهران 1.2 که گرد کنیم میشه یک آیتم تعداش است

most_freq_id = dataset['ID_Customer'].value_counts().idxmax()
customer_data = dataset[dataset['ID_Customer'] == most_freq_id]
max_amount_row = customer_data.loc[customer_data['Amount_Gross_Order'].idxmax()]
print(max_amount_row['DateTime_CartFinalize'])  
#اون مشتری ای که بیشترین تعداد خرید رو داشته گرونترین خرید اش در چه ساعتی بوده
