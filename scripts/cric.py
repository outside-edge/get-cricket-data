##--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~--++
##                                             ##
##        Cricket: Main
##        Last Edited: 10.01.12               
##        Gaurav Sood                          ##
##--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~--++

import urllib2
import csv
import re
import time
import docric
from urlparse import urlparse
from BeautifulSoup import BeautifulSoup, SoupStrainer

# Initialize four tables
winloss = csv.writer(open('winloss.csv', 'wb'))
winloss.writerow(('match id', 'odiurl', 'team1', 'team1.total', 'team2', 'team2.total', 'toss', 'won', 'margin', 'bat.or.bowl', 'date', 'day.n.night', 'ground', 'ground.country', 'groundurl')) # Win Head
batting = csv.writer(open('batting.csv', 'wb'))
batting.writerow(('match id', 'batsman', 'dismissal', 'runs', 'mins', 'balls', 'fours', 'sixes', 'sr', 'batsman.url', 'playerid')) # Bat Head
bowling = csv.writer(open('bowling.csv', 'wb'))
bowling.writerow(('match id', 'bowler', 'over', 'maiden', 'run', 'wckt', 'econ', 'extra', 'bowler.url', 'playerid')) # Bowl Head
exception = csv.writer(open('exception.csv', 'wb'))
exception.writerow(('match id', 'odiurl', 'exception')) 

#for i in range(3, 9):
#    soup = BeautifulSoup(urllib2.urlopen('http://www.espncricinfo.com/iccct2009/engine/match/41527' + str(i) + '.html').read())

for i in range(1, 268):
    soupy = BeautifulSoup(urllib2.urlopen('http://search.espncricinfo.com/ci/content/match/search.html?search=odi;all=1;page=' + str(i)).read())
    time.sleep(1)
    for new_host in soupy.findAll('a', {'class' : 'srchPlyrNmTxt'}):
        try:
            new_host = new_host['href']
        except:
            continue
        odiurl = 'http://www.espncricinfo.com' + urlparse(new_host).geturl()
        print(new_host)
        soup = BeautifulSoup(urllib2.urlopen(odiurl).read())

        #try:
        # match id
        temp = soup.findAll(text=re.compile("ODI no. "))
        temp2 = soup.findAll(text=re.compile("List A "))
        temp3 = soup.findAll(text=re.compile("unofficial ODI "))
    
        if(len(temp) != 0):
            try:
                id = re.findall(r'[0-9]+', temp[0].string)[0]
            except:
                exception.writerow(('ID Not Available', odiurl, 'Main page issue'))
                continue
        elif(len(temp2) != 0):
            id = "List A"
        elif(len(temp3) != 0):
            id = "unofficial ODI"
        else:
           exception.writerow(('ID Not Available', odiurl, 'Main page issue'))
           continue
          #  try:
           #     temp = soup.findAll(text=re.compile("unofficial ODI "))[0].string
            #    id = "unofficial ODI"
             #   print temp
            #except:
             #  print('Couldnt find id') 
              # continue
       
        
        # win loss table
        docric.winloss(id, odiurl, soup, winloss)
        
        # bowling table
        docric.bowl('inningsBowl1', soup, bowling, id, odiurl, exception)
        docric.bowl('inningsBowl2', soup, bowling, id, odiurl, exception)
        
        # batting table    
        docric.bat('inningsBat1', soup, batting, id)
        docric.bat('inningsBat2', soup, batting, id)
    
