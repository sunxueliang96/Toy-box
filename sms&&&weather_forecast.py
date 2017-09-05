#!/usr/bin/env python
# coding=utf-8
import os
import urllib2  
import json  

curl = "curl  http://www.weather.com.cn/data/cityinfo/101050101.html"
process = os.popen(curl)
msg = process.read()
dic = eval(msg)
dic1 = dic['weatherinfo']

city = '\n'+ '\nHi My Darling \n' + dic1['city']
temp1 = '\nlowest temperature : ' + dic1['temp1']
temp2 = '\nhighest temperature : ' + dic1['temp2']
weather = '\nand the weather : ' + dic1['weather'] + "\nYour kiss still burns on my lips, everyday of mine is so beautiful"


data_head ="curl 'https://api.twilio.com/2010-04-01/Accounts/ACe98c1b5cdd2b4c95599ccb8f77e647fb/Messages.json' -X POST \
        --data-urlencode 'To=+8618845143119' \
        --data-urlencode 'From=+18064524086' \
        --data-urlencode "
data_head1 ="curl 'https://api.twilio.com/2010-04-01/Accounts/ACe98c1b5cdd2b4c95599ccb8f77e647fb/Messages.json' -X POST \
        --data-urlencode 'To=+8613945693374' \
        --data-urlencode 'From=+18064524086' \
        --data-urlencode "
data_body0 ="'Body="
data_body1 ="'"
data_tail =" -u ACe98c1b5cdd2b4c95599ccb8f77e647fb:5c6c46844597c1799ddc7aaa77d16b34"
data0 = city + temp1 + temp2 + weather

data = data_head + data_body0 + data0 + data_body1 + data_tail
data1 = data_head1 + data_body0 + data0 + data_body1 + data_tail 
#print data
os.system(data)
os.system(data1)
