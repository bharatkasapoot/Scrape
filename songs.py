
#utf8
# scrape
import requests
from bs4 import BeautifulSoup

#URL = "http://www.geekforgeeks.org/data-structures/"
URL = "http://www.directlyrics.com/adele-25-lyrics.html"
r = requests.get(URL)
#print (r.content)
soup = BeautifulSoup(r.content,'html5lib')
#print type(soup)
#soup = soup.prettify().encode('utf-8')
#print soup
#find first instance of table with class name tableAlbumDetail. RETURNS STRING
tables = soup.find_all('div', attrs = {'class':'lyrics'})

print type(tables)
print type(tables[0].find_all('a'))
#print len(tables)
listed=[]
for row in tables[0].find_all('a'):
	#add each row in tbles using append

	rowtxt = row.text.encode('utf-8')
	#rowtxt = rowtxt.encode('utf-8')
	listed.append(rowtxt)
	print rowtxt
	print "@@@@@@@@@@@@@@@@@@@@@@"
newfilename = 'Adel25.txt'
with open(newfilename,'w') as f:
	for row in listed:
		f.write(row + '\n')
#tables contains string of html
#create a list



'''
listed = []
#iterate over all td's which have align = left

for row in tables:
	#add each row in tbles using append
	rowtxt = row.text
	#rowtxt='\n'.join(row.text)
	#print rowtxt
	#print row
	#print row.text
	listed.append(rowtxt)

#print listed[:-2]
#print type(listed)
#print len(listed)
#print listed
#print listed[:-2] #, start with zero element, skip one	
###print len(listed[::2])
filename = 'Adel25.txt'
with open(filename,'w') as f:
	for lnt in listed:
		#f.writelines('\n'.join(lnt.encode('utf-8'))) 
		print lnt
		#nine = '\n'.join(lnt)
		#print nine
		#f.write('\n')
		f.write(lnt + '\n')

'''