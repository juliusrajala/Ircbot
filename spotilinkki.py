# -*- coding: utf-8 -*-

import spotipy
import sys
import spotipy.util as util

ClientID = "f6acddb1e68b45d9bb517783d9e5cd98"
ClientSecret  = "51f91fe6f15b460da2c0e6438004b12b"
user = "digitteekkari"
pw = "d1k1tt1"

sp = spotipy.Spotify()

def searchTracks(artist, number):
	returned = ""
	if number > 6:
		number = 6
	
	results = sp.search(q=artist, limit=number)

	for i, t in enumerate(results['tracks']['items']):
		returned = returned + "TRACK: " + str(i) + " " + t['name'] +", "
	return returned.encode("utf8")

def addToQueue(track):
	# Toteuta trackin lisääminen kiltiksen soittolistaan
	return track

def signToSpotify(user, pw):
	# Toteuta spotifyn tunnistautuminen
	print("Signed in.")