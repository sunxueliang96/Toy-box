from scapy.all import *
import pygeoip
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
#from mpl_toolkits.basemap import Basemap

gi = pygeoip.GeoIP('./db/GeoLiteCity.dat')
plt.axis([0, 999999, 0, 100])
plt.ion()
G = nx.MultiDiGraph()


def sniffer(num):
    try:
        dpkt = sniff(iface="wlp4s0", count=num)
    #print (dpkt)
        return dpkt
    except BaseException:
        print('sniff failed')
    # return dpkt

# def basemap(lon,lat):


def printer(dpkt):
    for i in range(len(dpkt)):
        try:
            # print(dpkt[i][IP].src,'---->',dpkt[i][IP].dst)      #print
            # 1.1.1.1  ----> 2.2.2.2 e.m.
            src = get_geoip(dpkt[i][IP].src)
            dst = get_geoip(dpkt[i][IP].dst)
            # print('from')
            print(src['city'])
            print(str(src['latitude']) + ',' + str(src['longitude']))
            #generate_map(str(src['longitude']), str(src['latitude']))
            print(dst['city'])
            print(str(dst['latitude']) + ',' + str(dst['longitude']))

        except BaseException:
            pass


def decoder(dpkt):
    for i in range(len(dpkt)):
        try:
            #dst = get_geoip(dpkt[i][IP].dst)
            # return (dst['city'])
            len = len(dpkt)
        except BaseException:
            pass
# def generate_map(lats, lons):
#   m = Basemap(projection='cyl', resolution='l')
#    m.bluemarble()
#    x, y = m(lons, lats)
#    m.scatter(x, y, s=1, color='#ff0000', marker='o', alpha=0.3)


def loop(num):
    try:
        for i in range(num):
            # while True:
            rec = sniffer(1)
            plt.scatter(i, len(rec[Raw]))
            print(len(rec[Raw]))
            plt.pause(0.1)
            printer(rec)

    except KeyboardInterrupt:
        exit()


def get_geoip(tgt):
    rec = gi.record_by_addr(tgt)
    return rec


def main():
    try:
        plt.show()
        loop(9999999999)
        # plt.show()
    except KeyboardInterrupt:
        exit('user exit')


main()
