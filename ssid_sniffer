#!/usr/local/bin/python
#-*- coding: utf-8 -*-
import time
import wx
import sys
import os
import signal
import re
import string
from scapy.all import *

interface = 'wlan0mon'
hiddenNets = []
unhiddenNets = []
broads_list =[]
probeReqs = []
is_sigint_up = False

def sigint_handler(signum, frame):
    print 'catched interrupt signal!'
    is_sigint_up = True
    #sys.exit()
    f = open('ssid_list.txt','r+')
    f.write('hiddenNets')
    f.write(str(hiddenNets))
    f.write('unhiddenNets')
    f.write(str(broads_list))
    f.write(str(probeReqs))
    f.close()




class HelloFrame(wx.Frame):
    """
    A Frame that says Hello World
    """

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(HelloFrame, self).__init__(*args, **kw)

        # create a panel in the frame
        pnl = wx.Panel(self)
        self.textCtrl = wx.TextCtrl ( pnl, size = (400,100),value = "click file && start, starting scaning ssid",style = wx.TE_READONLY | wx.TE_CENTER)
        # and put some text with a larger bold font on it
        st = wx.StaticText(pnl, label="", pos=(25,25))
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

        # create a menu bar
        self.makeMenuBar()

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to ssid discover")


    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """

        # Make a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        helloItem = fileMenu.Append(-1, "&Start...\tCtrl-H",)
        fileMenu.AppendSeparator()
        # When using a stock ID we don't need to specify the menu item's
        # label
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)


    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)

    def OnHello(self, event):
        """Say hello to the user."""
        wx.MessageBox("Start for detect ssid")
	sniffer()



    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("designed by sunxueliang96",
                      "2015116319",
                      wx.OK|wx.ICON_INFORMATION)
class App(wx.App):

   def __init__(self,redirect=True,filename=None):

       print "App init..."

       wx.App.__init__(self,redirect,filename)

   def OnInit(self):

       print "oninit..."

       self.frame=Frame(parent=None,id=-1,title='hello')

       self.frame.Show()

       self.SetTopWindow(self.frame)

       print sys.stderr,"error message"

       return True

   def OnExit(self):

       print "OnExit"
'''
if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App(redirect=True)
    frm = HelloFrame(None, title='SSID discover')
    frm.Show()
    app.MainLoop()
'''



def pktPrint(pkt):
    if pkt.haslayer(Dot11Beacon):
        print('[+] Detected 802.11 Beacon Frame')
    elif pkt.haslayer(Dot11ProbeReq):
        print('[+] Detected 802.11 Probe Request Frame')
    elif pkt.haslayer(TCP):
        print('[+] Detected a TCP Packet')
    elif pkt.haslayer(DNS):
        print('[+] Detected a DNS Packet')


def sniff_ssid(p):
    try:
        if p.haslayer(Dot11Beacon):    
            addr2 = p.getlayer(Dot11).addr2
            if (addr2 not in hiddenNets) & (addr2 not in unhiddenNets):
                netName = p.getlayer(Dot11Beacon).info
                print '[+] Detected common SSID ' + netName + ' with MAC ' + addr2
                unhiddenNets.append(addr2)
                broads_list.append(netName)
            if p.getlayer(Dot11Beacon).info == '':
                addr3 = p.getlayer(Dot11).addr2
                if addr2 not in hiddenNets:
                    print '[*+*] Detect Hidden SSID' + ' with MAC ' + addr3
        if p.haslayer(Dot11ProbeReq):
            netName = p.getlayer(Dot11ProbeReq).info
    	    if netName not in probeReqs:
                probeReqs.append(netName)
                print('[+] Detected New SSID Request: ' + netName)
    except:
        pass

def iw_start():
    try:
        os.system('airmon-ng check kill')
        os.system('sudo /usr/sbin/airmon-ng start wlan0')
    except:
        sys.exit("Can't start interface ......")

def iw_stop():
    try:
        os.system('sudo /usr/sbin/airmon-ng stop wlan0mon')
        os.system('service network-manager start')
        exit('scaning finished')
    except:
        sys.exit("Can't stop interface ......")



def sniffer():
    signal.signal(signal.SIGINT, sigint_handler)                                  
    signal.signal(signal.SIGTERM, sigint_handler) 
    while True:
        try:
            sniff(iface=interface, prn=sniff_ssid, count=1)
            if is_sigint_up:
                break
        except KeyboardInterrupt:  
            print "exit by user"
            break
       # e
    #finally:
      #  print "exit by user"



if __name__=='__main__':
    try:
        app=wx.App(redirect=False)
        print "begin mainloop"
        frm = HelloFrame(None, title='SSID discover')
        frm.Show()
        iw_start()
        app.MainLoop()
    except KeyboardInterrupt:
        iw_stop()
        print "exit by user"
    finally:
        print "exit by user"

