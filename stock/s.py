import csv
import re
def addDate(year,month,day,a):
    try:
        f = open(year+month+day+'.txt','r+',encoding='utf-8')
        txt = f.read()
        txt  = txt.split('"本益比",')
        txt = txt[1]
        txt = txt.replace(',\n',',"'+year+month+day+'"\n')
        txt1 = ''
        for i in txt:   
            txt1+=i
        txt1 = txt1.replace('=','')
        txt1 = txt1.split('"備註:')[0]
        a=a+txt1
        
        f.close()
        return a
    except:
        pass
year = str(2013)
months = ['01','02','03','04','05','06','07','08','09','10','11','12']
days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
a = ''
f1 = open(year+'_withdate.txt','w',encoding='utf-8')
for month in months:
    for day in days:
        if addDate(year,month,day,a) != None:
            f1.write(addDate(year,month,day,a))
f1.close()
