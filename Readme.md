## Data and scripts for 5000+ ODI Cricket Matches

### Scripts

The script scrapes data from espncricinfo. 
There are two scripts: `cric.py` and `docric.py` 
`cric.py` relies on `docric.py`
To run, <code>python cric.py</code>

### Data

The scripts produce four csvs: `winloss.csv`, `batting.csv`, `bowling.csv`, and `exception.csv`:

* [winloss.csv](https://raw.githubusercontent.com/soodoku/get-cricket-data/master/data/winloss.csv) contains the following columns: match id (unique id for the match), odiurl (url for the odi), team1 (first team), team1.total (total made by the team), team2 (second team), team2.total (second team's total), toss (team that won the toss), won (team that won), margin (margin of victory), bat.or.bowl (did the team that won the toss elect to bat or bowl), date, day.n.night (was it a day and night match), ground (ground name), ground.country (country in which the ground is located), groundurl (url for the ground)

* [batting.csv](https://raw.githubusercontent.com/soodoku/get-cricket-data/master/data/batting.csv) contains the following columns: match id (unique id for the match), batsman (batsman name), dismissal (how the batsman was dismissed), runs (total runs scored), mins (total minutes at the crease), balls (total balls faced), fours (total fours), sixes (total sixes), sr (strike rate), batsman.url (url for the batsman), playerid (unique id for the player)

* [bowling.csv](https://raw.githubusercontent.com/soodoku/get-cricket-data/master/data/bowling.csv) contains the following columns: match id (unique id for the match), bowler (bowler name), over (number of overs bowled), maiden (number of maidens), run (number of runs scored against), wckt (total # of wickets), econ (economy), extra (extras), bowler.url (url for the bowler), playerid  (unique id for the player)

* [exception.csv](https://github.com/soodoku/get-cricket-data/blob/master/data/exception.csv) contains the following columns: match id (unique id for the match), odiurl (url for the odi), exception (what exception was raised)

### Application

An article based on the data: [Cricket: An Unfairly Random Game](http://gbytes.gsood.com/2011/05/07/cricket-an-unfairly-random-game/)

### License

* Data released under [Creative Commons License](https://github.com/soodoku/ODI-Cricket-Match-Data/blob/master/License%20For%20Data.html).
* Scripts released under [MIT License](https://github.com/soodoku/ODI-Cricket-Match-Data/blob/master/LICENSE%20FOR%20SCRIPTS)

