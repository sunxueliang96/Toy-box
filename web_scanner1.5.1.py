#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<>
  Purpose: 
  Created: secret########
  need lib IPy
  pip install IPy
"""

import urllib
from BeautifulSoup import BeautifulSoup
import socket
import webbrowser
import sys
import getopt
from IPy import IP




sys.path.append("libs")                 
xml_all = ''
def version():
    print "web_discover_1.5     by raven"
def banner():
    print "********************************************************************************************************************************"  
    print "***************************************************                    *********************************************************"
    print "**********************************                     web_discover_1.5                *****************************************"  
    print "***************************************************                    *********************************************************"    
    print "********************************************************************************************************************************"  
    print "**************************************************************************             --raven        **************************"  
    print "********************************************************************************************************************************"
    print '**********************************************************fuck you raven ***********************************************--Dalion'


def titlemaker(url_open):                           #网站标题处理模块
    try:
        content = urllib.urlopen(url_open).read()
        soup = BeautifulSoup(content)
        text = soup.find('title')
        if text == None:
            text = "<title>None</title>"
    except:
        text = "<title>target is NONE or making an error</title>"
    return text

def retxml(url_open):                               #xml生成模块
    try:
        title=titlemaker(url_open)
        xml = (
            '<record>\n'
            '<ip_name>%s</ip_name>\n'
            '%s\n'
            '</record>\n'
            )%(url_open,title)
    except:
        xml = ''
    return xml
    
        
def scanner(dst,flag,print_flag):                                   #负责链接80端口主要模块
    global xml_all                                  #调用全局变量以便生成完整到xml表格
    try:
        for dst_ip in dst:
            ci_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.1)
            dst_ip = str(dst_ip)
            if dst_ip[-2:] == '.0':
                continue
            if dst_ip[-4:] == '.255':
                continue
            connect = ci_sock.connect_ex((dst_ip,80))
            if connect == 0:
                print str(dst_ip) + " web app is open"    

                url = "http://" + str(dst_ip)
        
                if flag == True:
                    print url + "opened on webbrowser"         
                    webbrowser.open(url)                   #在浏览器中打开界面'''
                if print_flag == True:
                    retxml_u = retxml(url)
                    xml_all  += str(retxml_u)
            try:
                ci_sock.shutdown(2)
            except:
                pass
    except KeyboardInterrupt:
        exit("user exit")

        
    if print_flag == True:
        printer(xml_all)


def printer(xml_all):                  #the printer 
    xmlhead = '<?xml version="1.0" encoding="UTF-8"?>\n<Document>\n'
    xmlfoot = '</Document>\n'    
    #print xml_finnal                               
    f= open('output.xml','w')
    #print >> f,xml_finnal
    xml_finnal = xmlhead + xml_all + xmlfoot
    f.write(xml_finnal)
    f.close

def helper(report):
    version()
    print "-h --help    show help message and exit"
    print "-v --version show version message and exit"
    print "-t --targetip     targetip input        "
    print "-o --output output the xml file"
    print "-b --wb scan an open ip in webbrowser"        
    
    print "-s --startip targetip start addr;need to use with -e arg building not use"
    print "-e --endip   endip addr; need to use combine with -s arg building not use"
    exit(report)   



def main():                                                 #主函数就只负责处理命令行参数好了
    try:                                                 
        opts, args = getopt.getopt(sys.argv[1:],         "vhot:s:be:", ["version","wb=","help", "output=","scan=","--startip=","--endip=","--targeip="])  
    except getopt.GetoptError:                           
        print "please cheak your input ...\n\n"          
        helper()                                         
                                                         
                                                         
    if len(sys.argv) < 2:                             
        helper("too few arguments")                      
    flag = False                                         
    print_flag = False
    dst_ip = ''
    s_ip = ''
    e_ip = ''
    for opt, value in opts:
        if opt in ("-b","--wb"):
            flag = True
        elif opt in ("-o", "--output"):  
            print_flag = True
        elif opt in ("-t", "--targetip"):  
            dst_ip = value
            ip = IP(dst_ip)
            if ip.version == 6:
                exit('no ipv4 addr')
        elif opt in ("-s","--startip"):
            s_ip = value
        elif optn in ("-e","--endip"):
            e_ip = value
        
        elif opt in ("-v","--version"):
            version()
        
        if dst_ip == None :
            helper()
         
    scanner(ip,flag,print_flag)
if __name__ == '__main__':
    main()
