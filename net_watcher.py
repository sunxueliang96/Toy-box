from scapy.all import *
import pygeoip

gi = pygeoip.GeoIP('./db/GeoLiteCity.dat')

def sniffer():
    try:
        dpkt  = sniff(iface = "enp3s0", count = 1)
    #print (dpkt)
        return dpkt
    except:
        print('sniff failed')
    #return dpkt

def printer(dpkt):
    for i in range(len(dpkt)):
        try:
            #print(dpkt[i][IP].src,'---->',dpkt[i][IP].dst)
            src = get_geoip(dpkt[i][IP].src)
            dst = get_geoip(dpkt[i][IP].dst)
            print(src['city'])
            print('------>')
            print(dst['city'])
        except:
            pass
            #print('getip failed')
def loop():
    test = sniffer()
    printer(test)

def get_geoip(tgt):
    rec = gi.record_by_addr(tgt)
   # city = rec['city']
   # lon = rec['longitude']
   # lat = rec['latitude']
    return rec

def main():
    try:
        while True:
            loop()
    except KeyboardInterrupt:
        exit('user exit')
main()
