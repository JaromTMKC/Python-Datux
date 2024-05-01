import pandas as pd
import re 

dataAmazon=pd.read_csv('./modulo5/data/amazon.csv',sep=',')

## analisis
# hacer head 
# ver columnas
#print(dataAmazon.head())
columns=dataAmazon.columns
print(columns)
"""Index(['product_id', 'product_name', 'category', 'discounted_price',
       'actual_price', 'discount_percentage', 'rating', 'rating_count',
       'about_product', 'user_id', 'user_name', 'review_id', 'review_title',
       'review_content', 'img_link', 'product_link'],
      dtype='object')"""

def isLink(link:str):
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return link is not None and regex.search(link)

def settingColumn(row):
    if isLink(row):
        return True
    else:
        return False
    
dataAmazon["isLink"]=dataAmazon['product_link'].apply(settingColumn)

print(dataAmazon.head())


    

