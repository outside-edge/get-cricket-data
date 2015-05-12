'''

Get Cricket Data: Functions
Functions to scrape data from the webpages

@date: 9.28.12  
@author: Gaurav Sood                          

'''

import urllib2
import re
from BeautifulSoup import BeautifulSoup, SoupStrainer

def winloss(id, odiurl, soup, winloss):
        # teams
        teams = soup.findAll('a', {'class' : 'teamLink'})
        team1 = teams[0].string
        team2 = teams[1].string
        
        # toss
        temp = (soup.findAll('tr', {'class' : 'notesRow'}))[0]
        temp2 = (temp.findAllNext(text=True)[3]).lstrip()
        toss = temp2
        
        # bat bowl
        batbowl = 'bat'
        if re.search('bat', temp2) is None:
            batbowl = 'bowl'
            #print(batbowl)
            
        # won
        temp = (soup.findAll('p', {'class' : 'statusText'}))[0].string
        won = temp.split('won')[0]
        
        # margin of victory
        if temp.find('by ') == -1:
            margin = temp
        else:
            margin = temp.split('by ')[1]
            
        # day/night 
        temp = (soup.find('div', {'class' : 'headRightDiv'})).findNext('ul').findNext('li').findNext('li').findNext('li').string
        dayn = 0
        if re.search('day', temp) is None:
            dayn = 0
        else:
            dayn = 1
                        
        # match date
        temp = soup.find('div', attrs={'class': 'headRightDiv'}).findNext('ul')
        temp2 = temp.findAll('li')[2].string.split('(')[0]
        date = temp2.split("- ")[0].lstrip() 
           
        # ground
        temp = soup.find('div', attrs={'class': 'headRightDiv'}).findNext('ul')
        ground = temp.findAll('li')[1].findNext('a').string
        
        # Ground URL
        tempgurl = temp.findAll('li')[1].findNext('a').get('href')
        groundurl = 'http://www.espncricinfo.com' + tempgurl
        
        # country in which the ground is
        countrysoup = BeautifulSoup(urllib2.urlopen(groundurl).read())
        country = countrysoup.findAll('h1')[0].find('span', attrs={'class': 'SubnavSubsection'}).string
        #print country
        #print soup.find(text=re.compile(ground)).parent.get('href')
       
        # who bowled first; assign team to batsmen and bowlers
        bat1 = bat2 = bowl1 = bowl2 = 'NA'
        a = soup.findAll('tr', {'class' : 'inningsHead'})
        
        t = a[0].findAll('td')
        t2 = t[1].text
        bat1 = bowl2 = t2.split(' innings')[0].strip()
        #print(bat1)
        if(len(a) > 2):  
            t = a[2].findAll('td')
            t2 = t[1].text
            bat2 = bowl1 = t2.split(' innings')[0].strip()
            #print(bat2)
            
        #team score
        team1sc = team2sc = 'na'
        t = soup.findAll(text='Total')
        # if only one innings was played
        if len(t) == 1:
            if bat1 == team1:
                team1sc = t[0].findNext('td').findNext('td').findNext('b').contents[0]   
            else:
                team2sc = t[0].findNext('td').findNext('td').findNext('b').contents[0]   
        # if both teams played 
        if len(t) > 1:
            if bat1 == team1:
                team1sc = t[0].findNext('td').findNext('td').findNext('b').contents[0]   
                team2sc = t[1].findNext('td').findNext('td').findNext('b').contents[0] 
            else:
                team2sc = t[0].findNext('td').findNext('td').findNext('b').contents[0]   
                team1sc = t[1].findNext('td').findNext('td').findNext('b').contents[0]

        # win loss table
        winloss.writerow((id, odiurl, team1, team1sc, team2, team2sc, toss, won, margin, batbowl, date, dayn, ground, country, groundurl)) # Win/Loss Data

# need bowler ID: to connect to bowler table
# need country for bowler
def bowl (tableid, soup, bowling, id, odiurl, exception):
    tabulka = soup.find('table', {'id' : tableid})
    if tabulka <> None:
        for row in tabulka.findAll('tr', {'class':'inningsRow'}):
                col = row.findAll('td', {'class':'bowlingDetails'})
                bowler = row.findAll('a', {'class':'playerName'})
                if ((len(bowler)) < 1):
                    over = maiden = run = wckt = econ = extra = 'null'
                else:
                    try:
                        bowlerurl = 'http://www.espncricinfo.com' + bowler[0].get('href')
                        playerid = bowler[0].get('href').split("/")[4].split(".html")[0]
                        over = col[0].string
                        maiden = col[1].string
                        run = col[2].string
                        wckt = col[3].string
                        econ = col[4].string
                        extra = col[5].string
                        record = (id, bowler[0].string, over, maiden, run, wckt, econ, extra, bowlerurl, playerid)
                        bowling.writerow(record)
                    except:
                        exception.writerow((id, odiurl, 'bowl issues'))
                        
                        
def bat(tableid, soup, batting, id):
    tabulka = soup.find('table', {'id' : tableid})
    if tabulka <> None:
        for row in tabulka.findAll('tr', {'class':'inningsRow'}):
            col = row.findAll('td', {'class':'battingDetails'})
            runs = row.findAll('td', {'class':'battingRuns'}) 
            batter = row.findAll('a', {'class':'playerName'})
            dismiss = row.findAll('td', {'class':'battingDismissal'})
            dis = run = mins = balls = fours = sixs = sr = 'na'
            if ((len(batter)) < 1):
                continue
            else:
                dis = dismiss[0].string
                run = runs[0].string
                batsman = batter[0].string
                batsmanurl = 'http://www.espncricinfo.com' + batter[0].get('href')
                playerid = batter[0].get('href').split("/")[4].split(".html")[0]
            if len(col) > 0: 
                mins = col[0].string
            if len(col) > 1: 
                balls = col[1].string
            if len(col) > 2: 
                fours = col[2].string
            if len(col) > 3: 
                sixs = col[3].string
            if len(col) > 4: 
                sr = col[4].string    
            record = (id, batsman, dis, run, mins, balls, fours, sixs, sr, batsmanurl, playerid)
            batting.writerow(record)
