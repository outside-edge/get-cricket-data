'''

Download Cricket Data

'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import csv
import sys
import time
import os
import unicodedata
from urlparse import urlparse
from BeautifulSoup import BeautifulSoup, SoupStrainer

BASE_URL = 'http://www.espncricinfo.com'

if not os.path.exists('./espncricinfo-fc'):
    os.mkdir('./espncricinfo-fc')

for i in range(0, 6019):
    #odi: soupy = BeautifulSoup(urllib2.urlopen('http://search.espncricinfo.com/ci/content/match/search.html?search=odi;all=1;page=' + str(i)).read())
    #test: soupy = BeautifulSoup(urllib2.urlopen('http://search.espncricinfo.com/ci/content/match/search.html?search=test;all=1;page=' + str(i)).read())
    #t20i: soupy = BeautifulSoup(urllib2.urlopen('http://search.espncricinfo.com/ci/content/match/search.html?search=t20i;all=1;page=' + str(i)).read())
    #t20: soupy = BeautifulSoup(urllib2.urlopen('http://search.espncricinfo.com/ci/content/match/search.html?search=t20;all=1;page=' + str(i)).read())
    #list a: soupy = BeautifulSoup(urllib2.urlopen('http://search.espncricinfo.com/ci/content/match/search.html?search=list%20a;all=1;page=' + str(i)).read())
    #fc:
    soupy = BeautifulSoup(urllib2.urlopen('http://search.espncricinfo.com/ci/content/match/search.html?search=first%20class;all=1;page=' + str(i)).read())

    time.sleep(1)
    for new_host in soupy.findAll('a', {'class' : 'srchPlyrNmTxt'}):
        try:
            new_host = new_host['href']
        except:
            continue
        odiurl = BASE_URL + urlparse(new_host).geturl()
        new_host = unicodedata.normalize('NFKD', new_host).encode('ascii','ignore')
        print new_host
        #print(type(str.split(new_host)[3]))
        print str.split(new_host, "/")[4]
        html = urllib2.urlopen(odiurl).read()
        if html:
            with open('espncricinfo-fc/%s' % str.split(new_host, "/")[4], "wb") as f:
                f.write(html)



        
