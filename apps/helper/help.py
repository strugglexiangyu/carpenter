# -*- coding:utf8 -*-

import urllib2
import json
import datetime
import time
from  xml.dom.minidom import parseString
def get_customer_Channel(customer_code,types):
    res = urllib2.urlopen('http://rcmsapi.chinacache.com:36000/customer/'+str(customer_code)+'/product/'+str(types)+'/channels')
    #print 'http://rcmsapi.chinacache.com:36000/customer/'+str(customer_code)+'/product/'+str(types)+'/channels'
    return json.loads(res.read())
   

def get_customer_code(name):
    res = urllib2.urlopen('http://rcmsapi.chinacache.com:36000/customer/'+name)
    code = json.loads(res.read())['code']
    return code

def get_origin(start,end,channel):
    try:
        res = urllib2.urlopen('http://icp.chinacache.com/upqueryservice/pub/query/billing/LogBandWidthByChannelID?Type=standard&RegionID=9050&ChannelCount=1&StartTime='+start+'&EndTime='+end+'&ChannelID1='+str(channel))
        #print 'http://icp.chinacache.com/upqueryservice/pub/query/billing/LogBandWidthByChannelID?Type=standard&RegionID=9050&ChannelCount=1&StartTime='+start+'&EndTime='+end+'&ChannelID1='+str(channel)
        xmldata =  parseString(res.read()).getElementsByTagName('OutData')[0].childNodes[0].nodeValue.split(',')  
    except:
        xmldata = []  
    return xmldata

def get_data_by_Channel(channels,day=4):
 
    if len(channels) > 0:

        ChannelCount = len(channels)
    else:
    	return {}
    channel_url = ''
    for i in range(len(channels)):
    	j = i + 1
    	channel_url = channel_url + '&ChannelID'+str(j)+'='+str(channels[i])
    d = datetime.datetime.now()
    oneday = datetime.timedelta(days=day)
    day = d - oneday
    
    endtime = time.strftime('%Y%m%d',time.localtime(time.time()))
    starttime = day.strftime('%Y%m%d')
    try:
        
        res = urllib2.urlopen('http://icp.chinacache.com/BillQueryService3/pub/query/billing/LogBandWidthByChannelID?Type=standard&RegionID=9050&ChannelCount='+str(ChannelCount)+'&StartTime='+str(starttime)+'&EndTime='+str(endtime)+channel_url )
        #print 'http://icp.chinacache.com/BillQueryService3/pub/query/billing/LogBandWidthByChannelID?Type=standard&RegionID=9050&ChannelCount='+str(ChannelCount)+'&StartTime='+str(starttime)+'&EndTime='+str(endtime)+channel_url
        xmldata =  parseString(res.read()).getElementsByTagName('OutData')[0].childNodes[0].nodeValue.split(',')  
    except:
    	xmldata = []
    if len(xmldata) == 0:
        try:
            res = urllib2.urlopen('http://icp.chinacache.com/BillQueryService3/pub/query/billing/LogBandWidthByChannelID?Type=standard&RegionID=9050&ChannelCount='+str(ChannelCount)+'&StartTime='+str(starttime)+'&EndTime='+str(endtime)+channel_url )
            #print 'http://icp.chinacache.com/BillQueryService3/pub/query/billing/LogBandWidthByChannelID?Type=standard&RegionID=9050&ChannelCount='+str(ChannelCount)+'&StartTime='+str(starttime)+'&EndTime='+str(endtime)+channel_url
            xmldata =  parseString(res.read()).getElementsByTagName('OutData')[0].childNodes[0].nodeValue.split(',')  
        except:
            xmldata = []

    return xmldata
     	

 



def toint(row):
    if row !='':
        return int(row)
    else:
        return 0

 
