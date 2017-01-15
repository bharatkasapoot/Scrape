import requests
from bs4 import BeautifulSoup
import csv
#To scrape delloite articles that I like
URL = "https://dupress.deloitte.com/dup-us-en/focus/executive-transitions/dysfunctional-teams-turnaround-strategies-team-performance.html?id=us:2em:3na:dup3094:awa:dup:122016:essay"
r = requests.get(URL)
#print (r.content)
soup = BeautifulSoup(r.content,'html5lib')
#print soup.prettify().encode('utf-8')
#find first instance of table with class name tableAlbumDetail. RETURNS STRING
tables = soup.find('article', attrs = {'class':'-full'})
#print tables
filename = 'dump.txt'
with open(filename,'w') as f:
	for row in tables.prettify().encode('utf-8'):
		f.write(row)
#in above code did not need to add \n as prettify adds that by itself
#tables contains string of html
#create a list

testing = tables.get_text().encode('utf-8')
newfilename = 'text_only.txt'
with open(newfilename,'w') as f:
	for row in testing:
		f.write(row)