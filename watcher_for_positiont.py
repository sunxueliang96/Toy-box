import requests
import smtplib
import time
from email.mime.text import MIMEText
from bs4 import BeautifulSoup

def get():
    s=requests.session()
    url='http://ischoolgu.xmu.edu.cn/admin_bookChair.aspx'
    headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    }
    cookies={'ASP.NET_SessionId':'**********************'}
    rs=s.get(url,headers=headers,cookies=cookies,verify=False)
    rs.encoding='utf-8'
    return rs
def soup(res):
	soup = BeautifulSoup(res.content,'html.parser',from_encoding='utf-8')
	try:
		target = soup.find_all('tr')[7].find_all('td')[1].text
		if(target=='0'):
			print('fuck')
		else:
			send_email()
			exit()
	except:
		refresh()
		print('refreshing~~~~~~~~~~~~~~~~~~~~')

def refresh():
	burp0_url = "http://ischoolgu.xmu.edu.cn:80/Default.aspx"
	burp0_cookies = {"ASP.NET_SessionId": "*****************"}
	burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Connection": "close", "Referer": "http://ischoolgu.xmu.edu.cn/Default.aspx", "Upgrade-Insecure-Requests": "1"}
	burp0_data = {"__EVENTTARGET": '', "__EVENTARGUMENT": '', "__VIEWSTATE": "/wEPDwUKMTE2MjQyMDE1NmRkP8UscZhhd3sXLtLUzRvuh9hwxY8=", "__VIEWSTATEGENERATOR": "CA0B0334", "__EVENTVALIDATION": "/wEWBwLEmeSiDQKPpuq2CAKSvuCRDwKLkaclAoqRpyUC1a2LhAYCw93S7gGSZe3tRMUx0l1pUUbtsGNyku5mng==", "userName": "**********", "passWord": "**********", "userType": "1", "sumbit": "\xb5\xc7\xa1\xa1\xc2\xbd"}
	requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
def send_email():
	msg_from='**********@qq.com'                                 #发送方邮箱
	passwd='c*********tbigi'                                   #填入发送方邮箱的授权码
	msg_to='2***********@qq.com'                                  #收件人邮箱			
	subject="gogogoogogo"                                     #主题     
	content="gogoogogo" 
	msg = MIMEText(content)
	msg['Subject'] = subject
	msg['From'] = msg_from
	msg['To'] = msg_to
	try:
		s = smtplib.SMTP_SSL("smtp.qq.com",465)
		s.login(msg_from, passwd)
		s.sendmail(msg_from, msg_to, msg.as_string())
		print ("发送成功")
		time.sleep('100')
	except:
		print ("发送失败")
	finally:
		s.quit()
if __name__ == '__main__':
	while(True):
		soup(get())
		time.sleep(3)
		print(time.time())