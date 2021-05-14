# -*- coding: utf-8 -*-
"""
Created on Wed May 12 19:58:53 2021

@author: Harivyas S
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://www.amazon.co.uk/All-New-Fire-Tablet-Alexa-Display/product-reviews/B07952CV7L/ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews'

def get_soup(url):
    r=requests.get(url,params={'url': url, 'wait': 2})
    #print(r.text)
    soup=BeautifulSoup(r.text,'html.parser')
    #print(soup.title.text)
    return soup

reviewlist=[]
def get_reviews(soup):
    reviews=soup.find_all('div',{'data-hook':'review'})
    try:
        for item in reviews:
            review={
            #'product': soup.title.text.replace('Amazon.co.uk:Customer reviews:', '').strip(),
            'Review Title':item.find('a',{'data-hook':'review-title'}).text.strip(),
            #print(Review Title)
            'Review description':item.find('span',{'data-hook':'review-body'}).text.strip(),
            'No of stars':float(item.find('i',{'data-hook':'review-star-rating'}).text.replace('out of 5 stars', '').strip()),
            'Review given by':item.find('span',{'class':'a-profile-name'}).text.strip(),
            'Date of review':item.find('span',{'data-hook':'review-date'}).text.replace('Reviewed in the United Kingdom on','').strip()
            #print(No of stars)
            #print(Date of Review)
            }
            #print(review)
            reviewlist.append(review)
    except:
        pass
    
for x in range(1,999):
    #print(x)
    soup=get_soup(f'https://www.amazon.co.uk/All-New-Fire-Tablet-Alexa-Display/product-reviews/B07952CV7L/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Getting page: {x}')
    get_reviews(soup)
    print(len(reviewlist))
    if not soup.find('li', {'class': 'a-disabled a-last'}):
        pass
    else:
        break

df = pd.DataFrame(reviewlist)
df.to_csv('C:/Users/asd/anaconda3/amazon_customer_review.csv', index=False)
print('Finish')