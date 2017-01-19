#!/usr/bin/python
# -*- coding: utf8 -*-

__author__ = "Davyd Maker"
__version__ = "1.0"

import requests

headers = {
    'User-Agent': 'Mozilla/5.0'
}

username = input('Steam Username: ')

try:
	r = requests.get('http://steamcommunity.com/id/'+username,headers=headers)
except Exception as e:
	print('This site is currently unavailable.')
	exit()

c = r.text

if '<div class="persona_name" style="font-size: 24px;">' not in c:
	print('\nUser does not exist.')
elif '<div class="profile_private_info">' in c:
	print('\nPrivate profile.')
else:

	#Time played in the last weeks
	if '<div class="recentgame_quicklinks recentgame_recentplaytime">' in c:
		time = c.split('<div class="recentgame_quicklinks recentgame_recentplaytime">')
		time = time[1].strip()
		time = time.split('</div>')
		time = time[0].replace('<h2>','').replace('</h2>','').strip()
		print('\nPlayed '+time+'.')
	else:
		print('\nUser did not play recently.')	

	#Account status
	if '<div class="playerAvatar profile_header_size online">' in c:
		print('Status: Online')
	elif '<div class="playerAvatar profile_header_size in-game">' in c:
		time = c.split('<div class="profile_in_game_name">')
		time = time[1].split('</div>')
		print('Status: Online, playing ' + time[0]+'.')
	else:
		time = c.split('<div class="profile_in_game_name">')
		time = time[1].split('</div>')
		print('Status: Offline, '+time[0].lower()+'.')

	#Player Level
	if '<span class="friendPlayerLevelNum">' in c:
		time = c.split('<span class="friendPlayerLevelNum">')
		time = time[1].strip()
		time = time.split('</span>')
		time = time[0].strip()
		print('Level: '+time)
	else:
		print('Unidentified level.')

	#Number of badges
	if '<a href="http://steamcommunity.com/id/'+username+'/badges/">' in c:
		time = c.split('<a href="http://steamcommunity.com/id/'+username+'/badges/">')
		time = time[1].strip()
		time = time.split('</a>')
		time = time[0].split('<span class="profile_count_link_total">')
		time = time[1].replace('</span>','').strip()
		print('Badges: '+time)
	else:
		print('Quantity of badges not found.')

	#Number of games
	if '<a href="http://steamcommunity.com/id/'+username+'/games/?tab=all">' in c:
		time = c.split('<a href="http://steamcommunity.com/id/'+username+'/games/?tab=all">')
		time = time[1].strip()
		time = time.split('</a>')
		time = time[0].split('<span class="profile_count_link_total">')
		time = time[1].replace('</span>','').strip()
		print('Games: '+time)
	else:
		print('Number of games not found.')

	#Number of groups
	if '<a href="http://steamcommunity.com/id/'+username+'/groups/">' in c:
		time = c.split('<a href="http://steamcommunity.com/id/'+username+'/groups/">')
		time = time[1].strip()
		time = time.split('</a>')
		time = time[0].split('<span class="profile_count_link_total">')
		time = time[1].replace('</span>','').strip()
		print('Groups: '+time)
	else:
		print('Number of groups not found.')

	#Number of friends
	if '<a href="http://steamcommunity.com/id/'+username+'/friends/">' in c:
		time = c.split('<a href="http://steamcommunity.com/id/'+username+'/friends/">')
		time = time[1].strip()
		time = time.split('</a>')
		time = time[0].split('<span class="profile_count_link_total">')
		time = time[1].replace('</span>','').strip()
		print('Friends: '+time)
	else:
		print('Number of friends not found.')