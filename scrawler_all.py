import requests
import bs4
import urllib.parse as up
import re
import time
import csv
import os
import json
stock_price = 'http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&type=ALLBUT0999&date='
indi = 'http://www.twse.com.tw/fund/TWT43U?response=csv&date='
fund = 'http://www.twse.com.tw/fund/TWT44U?response=csv&date='
fore = 'http://www.twse.com.tw/fund/TWT38U?response=csv&date='
year = str(2012)
month = ['01','02','03','04','05','06','07','08','09','10','11','12']
day = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
# month = ['01','02']
# day = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
# day = ['28','29','30','31']
for i in month:
    for j in day:
        na = year + str(i) +str(j)+'_indi'
        f = open(na, 'w',encoding='utf-8')
        url =  indi+year+i+j
        response = requests.get(url)
        f.write(response.text)
        f.close()
        time.sleep(5)

        
