import requests
import bs4
import urllib.parse as up
import re
import time
import csv
import os
import json
year = str(2015)
tw50 = [1101,1102,1216,1301,1303,1326,1402,1722,2002,2105,2201,2207,2301,2303,2308,2311,2317,2324,2325,2330,2347,2353,2354,2357,2382,2409,2412,2454,2474,2498,2801,2880,2881,2882,2883,2885,2886,2890,2891,2892,2912,3008,3045,3231,3481,3673,3697,4904,5880,6505]
month = ['01','02','03','04','05','06','07','08','09','10','11','12']
for i in tw50:
    try:
        f = open(str(i), 'a')
    except IOError:
        f = open(str(i), 'w')
    a = ''
    for j in month:
        url = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=csv&date='+year+j+'01&stockNo='+str(i)
        response = requests.get(url)
        a+=response.text
        time.sleep(4)
    f.write(a)
    f.close()



    # response = response.text.replace(',','')
    # response = response.split('"')




# for i in response:
#     j+=1
#     print(str(j)+' : '+str(i))
