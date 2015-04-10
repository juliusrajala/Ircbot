# -*- coding: utf-8 -*-

# Nyt se toimii, toteuta tätä kutsuva metodi botissa
# muista encode/decode

from bs4 import BeautifulSoup
import requests

def scrapeEvents():
	address = "http://digit.fi/enrol.php"
	page = requests.get(address)
	data = page.content
	soup = BeautifulSoup(data)
	events = soup.find_all('span', class_='eventlistitem')
	
	titles = []
	times = []
	returnable = []
	for event in events:
		titles.append(clean(event)[0])
		times.append(clean(event)[1])
		returnable.append(clean(event)[0]+" : " + clean(event)[1] + "\n")
	return(returnable)

def clean(event):
	global dictionary
	event = str(event).split("span")
	event = "".join(event)
	event = event.split('< class="eventlistitem">')
	event = "".join(event)
	event = event.split('< class="temporaltext">')
	event = "".join(event)
	event = event.split('<b>')
	event = "".join(event)
	event = event.split('<br>')
	event = "".join(event)
	event = event.split('</b>')
	event = "".join(event)
	event = event.split('<br/>')
	event = "".join(event)
	event = event.split('<')
	event = "".join(event)
	event = event.split('>')
	event = "".join(event)
	event = event.split('/')
	event = "".join(event)
	event = event.split('Ilmoittautuminen on käynnissä.')

	return event
	


scrapeEvents()