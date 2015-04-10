# -*- coding: utf-8 -*-

# Imports
import sys
import socket
import string
import os
from spotilinkki import searchTracks
from ilmoparseri import *

# Variables
HOST = "irc.utu.fi"
PORT = 6667
PASSWORD = ""
NICK = "Bot1nator"
IDENTITY = NICK
REALNAME = "lorenz0bot"
CHANNELINIT = ["#lorenzobotti"]
OWNER = "Lorenz0"


# Komentojen jakaja
def parseri(data):
	print(data)
	viesti = data.lower()
	silvottu = jaaKahteen(data)
	if viesti.find("hah") != -1:
		print("Hah kutsuttu.")
		kanava = findChannel(viesti.split(" "))
		messageSender(kanava, "gayyyyy!")
	if viesti.find("ping") != -1:
		print("PONG that shit.")
		sukka.send('PONG ' + silvottu[1] + '\r\n')
	if viesti.find("!spotitracks") != -1:
		kanava = findChannel(viesti.split(" "))
		messageSender(kanava, etsiKipaleet(silvottu[2]))
	if viesti.find("!ilmot") != -1:
		print("ilmoja pidellyt")
		kanava = findChannel(viesti.split(" "))
		ilmot(kanava)

# Functions

def messageSender(channel, message):
	sukka.send("PRIVMSG "+ channel + " :" + message + "\r\n")

def jaaKahteen(data):
	data = data.split(":")
	return(data)

def etsiKipaleet(data):
	data = data.split(" ")
	if len(data)>2:
		artisti = data[len(data)-2]
		amount = data[len(data)-1]
		print("Searching "+amount+" tracks from: "+ artisti)
		return(searchTracks(artisti, amount))
	else:
		print("Poor arguments.")

def findChannel(lista):
	for word in lista:
		if word[0] == "#":
			return word;
			pass

def ilmot(kanava):
	print("Fetching ilmot.")
	auki = scrapeEvents()
	for event in auki:
		print(event)
		messageSender(kanava, event)

# Connect to server
sukka = socket.socket( )
sukka.connect((HOST, PORT))
sukka.send('NICK ' + NICK + '\r\n')
sukka.send('USER ' + IDENTITY + ' '+HOST+' bla :'+ REALNAME+'\r\n')
for channel in CHANNELINIT:
	sukka.send('JOIN ' +channel+'\r\n')
print("Connection established.")

# Main
while True:
	data = sukka.recv(4096)
	parseri(data)