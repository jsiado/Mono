#!/usr/bin/env python
from random import randint, shuffle
from operator import attrgetter

import logging
import matplotlib.pyplot as plt
import numpy as np
import Monofn
import operator
import random

# update of the code
'''
implemented 
'''

'''Finish rent is calculated depending on the amount of railroads owned'''
def land_on_railroad():
	for r in Monofn.all_railroads:
		if r.position == p.position:
			if r.name in unowend_properties:
				res = input(p.name + ' you have ' + str(p.cash) + ' and landed in '+ r.name + ', would you like to buy it for '+ str(r.price) + '? :')
				if res == 'Y' or res == 'y' or res == 'yes':
					p.trains.append(r.name)
					p.cash -= r.price
					unowend_properties.remove(r.name)
					fout.write(p.name +' you just bought ' + r.name + ' now you have ' + str(p.cash) + '\n')
				else:
					auction()
					# pass
					#Player decided not to buy, implement auction logic
			else:
				for k in Monofn.all_players:
					if r.name in k.trains:
						if p.name != k.name:
							fout.write(p.name + ' ' + r.name + ' is owned by ' + k.name + ' you have to pay ' + str(r.rent[len(k.trains)-1]) + ' rent \n')
							k.cash +=r.rent[len(k.trains)-1]
							p.cash -=r.rent[len(k.trains)-1]
							fout.write(p.name + ' now has ' + str(p.cash) + '\n')
							fout.write(k.name + ' now has ' + str(k.cash) + '\n')
	return

'''Finish rent is calculated as 4 or ten times the amount rolled'''
def land_on_utility():
	for u in Monofn.all_utilities:
		if u.position == p.position:
			if u.name in unowend_properties:
				res = input(p.name + ' you have ' + str(p.cash) + ' and landed in '+ u.name + ' would you like to buy it for '+ str(u.price) + '? :')
				if res == 'Y' or res == 'y' or res == 'yes':
					p.services.append(u.name)
					p.cash -= u.price
					unowend_properties.remove(u.name)
					fout.write(p.name +' you just bought ' + u.name + ' your cash ' + str(p.cash) + '\n')
				else:
					auction()
					# pass
					#Player decided not to buy, implement auction logic
			else:
				for k in Monofn.all_players:
					if u.name in k.services:
						if p.name != k.name:
							nn = roll[0] + roll[1]
							k.cash +=(nn)*u.rent[len(k.services)-1]
							p.cash -=(nn)*u.rent[len(k.services)-1]
							fout.write(p.name + ' ' + u.name + ' is owned by ' + k.name + ' you have to pay ' + str((nn)*u.rent[len(k.services)-1]) + ' rent \n')
							fout.write(p.name + ' your cash ' + str(p.cash) + '\n')
							fout.write(k.name + ' your cash ' + str(k.cash) + '\n')
	return

def land_on_brown():
	for b in Monofn.all_brown:
		if b.position == p.position:
			if b.name in unowend_properties:
				res = input(p.name + ' you have ' + str(p.cash) + ' and landed in '+ b.name + ' would you like to buy it for '+ str(b.price) + '? :')
				if 'y' in res or 'Y' in res:
					p.properties.append(b.name)
					unowend_properties.remove(b.name)
					p.nbrown += 1
					p.cash -= b.price
					fout.write(p.name +' you just bought ' + b.name + '. Your cash ' + str(p.cash) + '\n')
				else:
					auction()	#Player decided not to buy, implement auction logic
			else:
				for player in Monofn.all_players:
					if b.name in player.properties:
						if p.name != player.name:
							if player.nbrown == b.nset:
								if b.n_house == 0:#set but no house
									fout.write(p.name+': '+b.name+' is owned by '+player.name+' and owns all properties, pay double the rent '+str(b.rent[1])+' \n')
									fout.write(p.name+'('+ str(p.cash)+')' + player.name + '('+ str(player.cash)+')' +'\n')	
									player.cash += b.rent[1]
									p.cash -= b.rent[1]
									fout.write(p.name+' your cash '+ str(p.cash)+'\n')
									fout.write(player.name +' your cash '+ str(player.cash)+'\n')

								
								else:#player has houses in the property
									player.cash += b.rent[b.n_house +1]
									p.cash -= b.rent[b.n_house +1]
									#print(p.name+' pays '+ player.name+' '+str(b.rent[b.n_house+1])+' for '+b.name)
							else:#player only owns one property
								fout.write(p.name + ' ' + b.name + ' is owned by ' + player.name + ' you have to pay ' + str(b.rent[0]) + ' rent \n')
								#print(p.name+' pays '+ player.name+' '+str(b.rent[0])+' for '+b.name)
								player.cash += b.rent[0]
								p.cash -= b.rent[0]
								fout.write(p.name + ' your cash ' + str(p.cash) + '\n')
								fout.write(player.name +' your cash '+ str(player.cash)+'\n')
								

	return

def land_on_lblue():
	for b in Monofn.all_lblue:
		if b.position == p.position:
			if b.name in unowend_properties:
				res = input(p.name + ' you have ' + str(p.cash) + ' and landed in '+ b.name + ' would you like to buy it for '+ str(b.price) + '? :')
				if 'y' in res or 'Y' in res:
					p.properties.append(b.name)
					unowend_properties.remove(b.name)
					p.nlblue += 1
					p.cash -= b.price
					fout.write(p.name +' you just bought ' + b.name + '. Your cash ' + str(p.cash) + '\n')
				else:
					auction()	#Player decided not to buy, implement auction logic
			else:
				for player in Monofn.all_players:
					if b.name in player.properties:
						if p.name != player.name:
							if player.nlblue == b.nset:
								if b.n_house == 0:#set but no house
									fout.write(p.name+': '+b.name+' is owned by '+player.name+' and owns all properties, pay double the rent '+str(b.rent[1])+' \n')
									fout.write(p.name+'('+ str(p.cash)+')' + player.name + '('+ str(player.cash)+')' +'\n')	
									player.cash += b.rent[1]
									p.cash -= b.rent[1]
									fout.write(p.name+'('+ str(p.cash)+')' + player.name + '('+ str(player.cash)+')' +'\n')
								
								else:#player has houses in the property
									player.cash += b.rent[b.n_house +1]
									p.cash -= b.rent[b.n_house +1]
									# print(p.name+' pays '+ player.name+' '+str(b.rent[b.n_house+1])+' for '+b.name)
							else:#player only owns one property
								fout.write(p.name + ' ' + b.name + ' is owned by ' + player.name + ' you have to pay ' + str(b.rent[0]) + ' rent \n')
								# print(p.name+' pays '+ player.name+' '+str(b.rent[0])+' for '+b.name)
								player.cash += b.rent[0]
								p.cash -= b.rent[0]
	return

def land_on_rosa():
	for b in Monofn.all_rosa:
		if b.position == p.position:
			if b.name in unowend_properties:
				res = input(p.name + ' you have ' + str(p.cash) + ' and landed in '+ b.name + ' would you like to buy it for '+ str(b.price) + '? :')
				if 'y' in res or 'Y' in res:
					p.properties.append(b.name)
					unowend_properties.remove(b.name)
					p.nrosa += 1
					p.cash -= b.price
					fout.write(p.name +' you just bought ' + b.name + '. Your cash ' + str(p.cash) + '\n')
				else:
					auction()	#Player decided not to buy, implement auction logic
			else:
				for player in Monofn.all_players:
					if b.name in player.properties:
						if p.name != player.name:
							if player.nrosa == b.nset:
								if b.n_house == 0:#set but no house
									fout.write(p.name+': '+b.name+' is owned by '+player.name+' and owns all properties, pay double the rent '+str(b.rent[1])+' \n')
									fout.write(p.name+'('+ str(p.cash)+')' + player.name + '('+ str(player.cash)+')' +'\n')	
									player.cash += b.rent[1]
									p.cash -= b.rent[1]
									fout.write(p.name+'('+ str(p.cash)+')' + player.name + '('+ str(player.cash)+')' +'\n')
								
								else:#player has houses in the property
									player.cash += b.rent[b.n_house +1]
									p.cash -= b.rent[b.n_house +1]
									# print(p.name+' pays '+ player.name+' '+str(b.rent[b.n_house+1])+' for '+b.name)
							else:#player only owns one property
								fout.write(p.name + ' ' + b.name + ' is owned by ' + player.name + ' you have to pay ' + str(b.rent[0]) + ' rent \n')
								# print(p.name+' pays '+ player.name+' '+str(b.rent[0])+' for '+b.name)
								player.cash += b.rent[0]
								p.cash -= b.rent[0]
	return

def land_on_naranja():
	for b in Monofn.all_naranja:
		if b.position == p.position:
			if b.name in unowend_properties:
				res = input(p.name + ' you have ' + str(p.cash) + ' and landed in '+ b.name + ' would you like to buy it for '+ str(b.price) + '? :')
				if 'y' in res or 'Y' in res:
					p.properties.append(b.name)
					unowend_properties.remove(b.name)
					p.nnaranja += 1
					p.cash -= b.price
					fout.write(p.name +' you just bought ' + b.name + '. Your cash ' + str(p.cash) + '\n')
				else:
					auction()	#Player decided not to buy, implement auction logic
			else:
				for player in Monofn.all_players:
					if b.name in player.properties:
						if p.name != player.name:
							if player.nnaranja == b.nset:
								if b.n_house == 0:#set but no house
									fout.write(p.name+': '+b.name+' is owned by '+player.name+' and owns all properties, pay double the rent '+str(b.rent[1])+' \n')
									fout.write(p.name+'('+ str(p.cash)+')' + player.name + '('+ str(player.cash)+')' +'\n')	
									player.cash += b.rent[1]
									p.cash -= b.rent[1]
									fout.write(p.name+'('+ str(p.cash)+')' + player.name + '('+ str(player.cash)+')' +'\n')
								
								else:#player has houses in the property
									player.cash += b.rent[b.n_house +1]
									p.cash -= b.rent[b.n_house +1]
									# print(p.name+' pays '+ player.name+' '+str(b.rent[b.n_house+1])+' for '+b.name)
							else:#player only owns one property
								fout.write(p.name + ' ' + b.name + ' is owned by ' + player.name + ' you have to pay ' + str(b.rent[0]) + ' rent \n')
								# print(p.name+' pays '+ player.name+' '+str(b.rent[0])+' for '+b.name)
								player.cash += b.rent[0]
								p.cash -= b.rent[0]
	return

def land_on_red():
	for b in Monofn.all_red:
		if b.position == p.position:
			if b.name in unowend_properties:
				res = input(p.name + ' you have ' + str(p.cash) + ' and landed in '+ b.name + ' would you like to buy it for '+ str(b.price) + '? :')
				if 'y' in res or 'Y' in res:
					p.properties.append(b.name)
					unowend_properties.remove(b.name)
					p.nred += 1
					p.cash -= b.price
					fout.write(p.name +' you just bought ' + b.name + '. Your cash ' + str(p.cash) + '\n')
				else:
					auction()	#Player decided not to buy, implement auction logic
			else:
				for player in Monofn.all_players:
					if b.name in player.properties:
						if p.name != player.name:
							if player.nred == b.nset:
								if b.n_house == 0:#set but no house
									fout.write(p.name+': '+b.name+' is owned by '+player.name+' and owns all properties, pay double the rent '+str(b.rent[1])+' \n')
									fout.write(p.name+'('+ str(p.cash)+')' + player.name + '('+ str(player.cash)+')' +'\n')	
									player.cash += b.rent[1]
									p.cash -= b.rent[1]
									fout.write(p.name+'('+ str(p.cash)+')' + player.name + '('+ str(player.cash)+')' +'\n')
								
								else:#player has houses in the property
									player.cash += b.rent[b.n_house +1]
									p.cash -= b.rent[b.n_house +1]
									# print(p.name+' pays '+ player.name+' '+str(b.rent[b.n_house+1])+' for '+b.name)
							else:#player only owns one property
								fout.write(p.name + ' ' + b.name + ' is owned by ' + player.name + ' you have to pay ' + str(b.rent[0]) + ' rent \n')
								# print(p.name+' pays '+ player.name+' '+str(b.rent[0])+' for '+b.name)
								player.cash += b.rent[0]
								p.cash -= b.rent[0]
	return

def land_on_yellow():
	for b in Monofn.all_yellow:
		if b.position == p.position:
			if b.name in unowend_properties:
				res = input(p.name + ' you have ' + str(p.cash) + ' and landed in '+ b.name + ' would you like to buy it for '+ str(b.price) + '? :')
				if 'y' in res or 'Y' in res:
					p.properties.append(b.name)
					unowend_properties.remove(b.name)
					p.nyellow += 1
					p.cash -= b.price
					fout.write(p.name +' you just bought ' + b.name + '. Your cash ' + str(p.cash) + '\n')
				else:
					auction()	#Player decided not to buy, implement auction logic
			else:
				for player in Monofn.all_players:
					if b.name in player.properties:
						if p.name != player.name:
							if player.nyellow == b.nset:
								if b.n_house == 0:#set but no house
									fout.write(p.name+': '+b.name+' is owned by '+player.name+' and owns all properties, pay double the rent '+str(b.rent[1])+' \n')
									fout.write(p.name+'('+ str(p.cash)+')' + player.name + '('+ str(player.cash)+')' +'\n')	
									player.cash += b.rent[1]
									p.cash -= b.rent[1]
									fout.write(p.name+'('+ str(p.cash)+')' + player.name + '('+ str(player.cash)+')' +'\n')
								
								else:#player has houses in the property
									player.cash += b.rent[b.n_house +1]
									p.cash -= b.rent[b.n_house +1]
									# print(p.name+' pays '+ player.name+' '+str(b.rent[b.n_house+1])+' for '+b.name)
							else:#player only owns one property
								fout.write(p.name + ' ' + b.name + ' is owned by ' + player.name + ' you have to pay ' + str(b.rent[0]) + ' rent \n')
								# print(p.name+' pays '+ player.name+' '+str(b.rent[0])+' for '+b.name)
								player.cash += b.rent[0]
								p.cash -= b.rent[0]
	return

def land_on_green():
	for b in Monofn.all_green:
		if b.position == p.position:
			if b.name in unowend_properties:
				res = input(p.name + ' you have ' + str(p.cash) + ' and landed in '+ b.name + ' would you like to buy it for '+ str(b.price) + '? :')
				if 'y' in res or 'Y' in res:
					p.properties.append(b.name)
					unowend_properties.remove(b.name)
					p.ngreen += 1
					p.cash -= b.price
					fout.write(p.name +' you just bought ' + b.name + '. Your cash ' + str(p.cash) + '\n')
				else:
					auction()	#Player decided not to buy, implement auction logic
			else:
				for player in Monofn.all_players:
					if b.name in player.properties:
						if p.name != player.name:
							if player.ngreen == b.nset:
								if b.n_house == 0:#set but no house
									fout.write(p.name+': '+b.name+' is owned by '+player.name+' and owns all properties, pay double the rent '+str(b.rent[1])+' \n')
									fout.write(p.name+'('+ str(p.cash)+')' + player.name + '('+ str(player.cash)+')' +'\n')	
									player.cash += b.rent[1]
									p.cash -= b.rent[1]
									fout.write(p.name+'('+ str(p.cash)+')' + player.name + '('+ str(player.cash)+')' +'\n')
								
								else:#player has houses in the property
									player.cash += b.rent[b.n_house +1]
									p.cash -= b.rent[b.n_house +1]
									# print(p.name+' pays '+ player.name+' '+str(b.rent[b.n_house+1])+' for '+b.name)
							else:#player only owns one property
								fout.write(p.name + ' ' + b.name + ' is owned by ' + player.name + ' you have to pay ' + str(b.rent[0]) + ' rent \n')
								# print(p.name+' pays '+ player.name+' '+str(b.rent[0])+' for '+b.name)
								player.cash += b.rent[0]
								p.cash -= b.rent[0]
	return

def land_on_blue():
	for b in Monofn.all_blue:
		if b.position == p.position:
			if b.name in unowend_properties:
				res = input(p.name + ' you have ' + str(p.cash) + ' and landed in '+ b.name + ' would you like to buy it for '+ str(b.price) + '? :')
				if 'y' in res or 'Y' in res:
					p.properties.append(b.name)
					unowend_properties.remove(b.name)
					p.nblue += 1
					p.cash -= b.price
					fout.write(p.name +' you just bought ' + b.name + '. Your cash ' + str(p.cash) + ' \n')
				else:
					auction()	#Player decided not to buy, implement auction logic
			else:
				for player in Monofn.all_players:
					if b.name in player.properties:
						if p.name != player.name:
							if player.nblue == b.nset:
								if b.n_house == 0:#set but no house
									fout.write(p.name+': '+b.name+' is owned by '+player.name+' and owns all properties, pay double the rent '+str(b.rent[1])+' \n')
									fout.write(p.name+'('+ str(p.cash)+')' + player.name + '('+ str(player.cash)+')' +'\n')	
									player.cash += b.rent[1]
									p.cash -= b.rent[1]
									fout.write(p.name+'('+ str(p.cash)+')' + player.name + '('+ str(player.cash)+')' +'\n')
								
								else:#player has houses in the property
									player.cash += b.rent[b.n_house +1]
									p.cash -= b.rent[b.n_house +1]
									# print(p.name+' pays '+ player.name+' '+str(b.rent[b.n_house+1])+' for '+b.name)
							else:#player only owns one property
								fout.write(p.name + ' ' + b.name + ' is owned by ' + player.name + ' you have to pay ' + str(b.rent[0]) + ' rent \n')
								# print(p.name+' pays '+ player.name+' '+str(b.rent[0])+' for '+b.name)
								player.cash += b.rent[0]
								p.cash -= b.rent[0]
	return
		
#need to implement make repairs and pay each player
# remove out of jail card from chance cards and add it back when used 
# finish go back 3 spaces
def land_on_chance():
	aux = chance[0]
	fout.write(p.name + ' you drew ' + aux + '\n')
	del chance[0]
	chance.append(aux)

	if aux == 'Go to jail':
		p.position = 10
		p.in_jail = True
		fout.write(p.name + ' you\'re in jail\n')

	elif aux == 'Advance to Go':
		p.cash +=200
		p.position = 0
		fout.write (p.name +' You have moved to go collect 200. You have'+str(p.cash)+ '\n')

	elif aux == 'Bank pays you 50':
		p.cash +=50
		fout.write (p.name + ' Bank pays you 50. You have '+str(p.cash)+ '\n')

	elif aux == 'Advance to the nearest railroad':
		fout.write (p.name + ' you drew Advance to the nearest railroad \n')
		if p.position == 7: 
			p.position = 15
			fout.write(p.name+' Your position '+str(p.position)+'\n')
		if p.position == 22: 
			p.position = 25
			fout.write(p.name+' Your position '+str(p.position)+'\n')
		if p.position == 36: 
			p.position = 5
			p.cash += 200
			fout.write (p.name + ' Your position '+str(p.position)+'. Your cash '+str(p.cash)+'\n')
		land_on_railroad()

	elif aux == 'Go back three spaces':
		p.position -=3
		fout.write (p.name +' Go back three spaces. Your position is '+str(p.position))
		#if p.position == 4:
			#p.cash -= 200

	elif aux == 'Your building loan matures. collect 150':
		p.cash +=150
		fout.write (p.name + ' Your building loan matures. collect 150. Your position '+str(p.position)+'. Your cash '+str(p.cash)+'\n')

	elif aux == 'speeding fine':
		p.cash -=15
		fout.write (p.name +' speeding fine. Pay 15. You have '+str(p.cash)+'\n')

	elif aux == 'Make repairs':	
		fout.write ('Make repairs')

	elif aux == 'Advance to the nearest utility':
		if p.position == 7:
			p.position = 12
			fout.write (p.name +' You drew Advance to the nearest utility. Your position '+ str(p.position)+'\n')
		elif p.position == 22:
			p.position = 28
			fout.write (p.name +' You drew Advance to the nearest utility. Your position '+ str(p.position)+'\n')
		else:
			p.cash += 200
			p.position = 12
			fout.write (p.name +' You drew Advance to the nearest utility. Your position '+ str(p.position)+' your cash '+str(p.cash)+'\n')
		land_on_utility()

	elif aux == 'Advance to Boarwalk':
		p.position = 39
		fout.write(p.name+' You drew Advance to Boarwalk. Your position '+ str(p.position)+'\n')
		land_on_blue()

	elif aux == 'Advance to St Charles Place':
		if p.position ==7:
			p.position = 11
			fout.write (p.name+' You drew Advance to St Charles Place. Your position '+str(p.position)+'\n')
		else:
			p.position =11
			p.cash+=200
			fout.write (p.name+' You drew Advance to St Charles Place. Your position '+str(p.position)+' your cash '+str(p.cash)+'\n')
		land_on_rosa()
	
	elif aux == 'Advance to Illinois avenue':
		if p.position == 36:
			p.position = 24
			p.cash +=200
			fout.write (p.name+' You drew Advance to Illinois Avenue. Your position '+str(p.position)+' your cash '+str(p.cash)+'\n')
		else:
			p.position = 24
			fout.write (p.name+' You drew Advance to Illinois Avenue. Your position '+str(p.position)+' your cash '+str(p.cash)+'\n')
		land_on_red()
	
	elif aux == 'Free get out of jail card':
		fout.write (p.name+' You drew Free get out of jail card')
		p.out_of_jail_cards +=1

	elif aux == 'Pay each player 50':
		fout.write ('Pay each player 50')
		fout.write (p.name+' You drew Pay each player 50. '+' your cash '+str(p.cash)+'\n')
		for pp in Monofn.all_players:
			if p.name != pp.name:
				p.cash -= 50
				pp.cash += 50

	else:
		p.position = 5
		p.cash += 200
		fout.write (p.name+' You drew Take a trip to reading railroad. Your position '+str(p.position)+' your cash '+str(p.cash)+'\n')



#need to remove out of jail card from cards and add it back when used
#implement make repairs
def land_on_com_chest():
	aux = chest[0]
	fout.write(p.name + ' you drew ' + aux + '\n')
	del chest[0]
	chest.append(aux)
	
	if aux == 'Go to jail':
		p.position = 10
		p.in_jail = True
		fout.write(p.name + 'you\'re in jail\n')
	elif aux == 'Advance to Go':
		p.cash +=200
		p.position = 0
		fout.write (p.name +' You have moved to go collect 200. You have '+str(p.cash)+ '\n')
	elif aux == 'Doctor fee. Pay 50':
		p.cash += 50
		fout.write (p.name +' You got 50. You have '+str(p.cash)+ '\n')
	elif aux == 'You inherit 100':
		p.cash += 100
		fout.write (p.name +' You got 100. You have '+str(p.cash)+ '\n')
	elif aux == 'recive 25':
		p.cash += 25
		fout.write (p.name +' You got 25. You have ' +str(p.cash)+ '\n')
	elif aux == 'From your sale of stocks you get 50':
		p.cash += 50
		fout.write (p.name +' You got 50. You have '+str(p.cash)+ '\n')
	elif aux == 'Hollyday fund receive 100':
		p.cash += 100
		fout.write (p.name +' You got 100. You have '+str(p.cash)+ '\n')
	elif aux == 'Income tax refund. Collect 20':
		p.cash += 20
		fout.write (p.name +' You got 20. You have '+str(p.cash)+ '\n')
	elif aux == 'Life insurance matures. Collect 100':
		p.cash += 100
		fout.write (p.name +' You got 100. You have '+str(p.cash)+ '\n')
	elif aux == 'Free get out of jail card':
		fout.write (p.name +' You got a free get out of jail card \n')
		p.out_of_jail_cards +=1
		###
	elif aux == 'Make repairs':
		# p.cash -=
		fout.write (p.name +' pay for houses and hotels. You have '+str(p.cash)+ '\n')
	elif aux == 'Bank error. Collect 200':
		p.cash += 200
		fout.write (p.name +' You got 200. You have '+str(p.cash)+ '\n')
	elif aux == 'Hospital fees. Pay 100':
		p.cash -= 100
		fout.write (p.name +' You payed 100. You have ' +str(p.cash)+ '\n')
	elif aux == 'School Fees. Pay 50':
		p.cash -= 50
		fout.write (p.name +' You payed 50. You have '+str(p.cash)+ '\n')
	elif aux == 'Beauty contest. Collect 10':
		p.cash += 10
		fout.write (p.name +' You got 10. You have'+str(p.cash)+ '\n')
	else:#10 from each player
		for pp in Monofn.all_players:
			if p.name != pp.name:
				p.cash += 10
				pp.cash -= 10
		fout.write (p.name +' You got 10 from each player. You have'+str(p.cash)+ '\n')

def auction():
	pass
	return ''

def out_of_jail():
	pass
	return

if __name__ == "__main__":
	"""
	Monopoly game for n players. all properties implemented but could be improve by putting the same code in a loop or similar for all color properties
	
	Need to be implemented
	Ask the user how many player and add them to class player
	Jail: need to pay to get out in first turn.
	No houses option yet, but double rent implemented
	No mortagage option implemented yet
	No auction option implemented if a player decides not to buy a property	
	Add option for free parking money
	Add option for bankruptcy
	Few things in chance and com chest need to be implemented
	
	"""
	nroll = 100
	fout = open("mono.txt", "w")
	
	#fp = input('would like to play with free parking money? tax and jail: ')
	#if 'y' in fp:
	
	fout.write('Playing Monopoly with ' + str(nroll) + ' turns per player \n')
	fout.write('\n')
	
	unowend_properties = Monofn.bank_properties()
	Trains = [5, 15, 25, 35]
	Utilities = [12, 28]
	properties = [1,3,37,39]
	chance = Monofn.chance_cards()
	random.shuffle(chance)
	chest = Monofn.Community_chest_cards()
	random.shuffle(chest)

	for i in range(nroll):
		for p in Monofn.all_players:
			
			in_turn, count  = True, 0
			while (in_turn):
				fout.write('It is ' + p.name +'`s turn \n')
				#built houses need to finish
				'''if p.nbrown == 2:# and n_house <5:
					res = input(p.name + ' you have all Brown properties and have ' + str(p.cash) + ' would you like to put house(s) in any of them? :')
					if 'y' in res or 'Y' in res:
						for house in Monofn.all_brown:
							res = input(p.name + ' would you like a house in ' + house.name + '? :')
							if 'y' in res or 'Y' in res:
								house.n_house +=1
								p.cash -=house.h_cost
								#print ('awesome')
							else:
								pass'''
							
				#res = input(p.name + ' you have all ' + str(p.cash) + ' and landed in '+ b.name + ' would you like to buy it for '+ str(b.price) + '? :')
				#for c in all_brown:
					#('----- ',Monofn.Brown.nset)
				#prop = ['Brown', 'Blue']
				#for d in prop:
					#print (d.nset)
					#if p.nbrown == Blue.nset:
				
				
				
				if p.in_jail == True: #check if player's in jail
					#out_of_jail()
					#ans = input(str(p.name) + ' it is your turn. You`re in jail. Would you like to roll (r) or pay (p). for now paying is the only opcion: ')
					#if 'p' in ans or 'P' in ans:
						#in_jail ()
					p.cash -= 50
					fout.write(p.name +  ' you just paid 50 to get out of jail, you now have ' + str(p.cash) + ' \n')
					p.in_jail = False
					roll = Monofn.Roll()
					p.position = p.position + roll[0] + roll[1]
					fout.write(p.name + ' you rolled a ' + str(roll[0]) + ' and ' + str(roll[1]) + ' and are now in position ' + str(p.position) + '\n')
				else:#if not in jail roll normally
					roll = Monofn.Roll()
					p.position = p.position + roll[0] + roll[1]
					if p.position >= 40:#go and 200 collection
						p.cash += 200
						p.position -= 40
						fout.write(p.name + ' you rolled a ' + str(roll[0]) + ' and ' + str(roll[1]) + ' and are now in position ' + str(p.position) + '. You passed Go take 200 ' + 'for a total of '+ str(p.cash) +'\n')
					else:
						fout.write(p.name + ' you rolled a ' + str(roll[0]) + ' and ' + str(roll[1]) + ' and are now in position ' + str(p.position) + '\n')

				if p.position == 30:# jail
					#print(p.name + ' you just landed in jail \n')
					fout.write(p.name + ' you just landed in jail \n')
					p.position = 10
					p.in_jail = True
				elif p.position == 10: # just visiting
					#print(p.name + ' just visiting \n')
					fout.write(p.name + ' just visiting \n')
				elif p.position == 20: # free parking
					fout.write(p.name + ' free parking nothig for now \n')
				elif p.position in [7, 22, 36]: #chance
					fout.write(p.name + ' you landed on a chance square. Draw a card\n')
					land_on_chance()
				elif p.position in [2, 17, 33]:#com chest
					fout.write(p.name + ' you landed on a community chest square. Draw a card \n')
					land_on_com_chest()
				elif p.position == 4:#income tax
					p.cash -= 200
					fout.write(p.name + ' you just landed on income tax pay 200 you now have '+ str(p.cash) + '\n')
				elif p.position == 38:# luxury tax
					p.cash -= 100
					fout.write(p.name +' you just landed on luxury tax pay 100 you now have ' + str(p.cash) + '\n')
				elif p.position in Trains: #trains
					land_on_railroad ()
				elif p.position in Utilities:#utilities
					land_on_utility()
				elif p.position in [1, 3]: #browns
					land_on_brown()
				elif p.position in [6, 8, 9]: #light blues
					land_on_lblue()
				elif p.position in [11, 13, 14]: #Rosa
					land_on_rosa()
				elif p.position in [16, 18,19]: #Naranja
					land_on_naranja()
				elif p.position in [21,23, 24]: #reds
					land_on_red()
				elif p.position in [26,27,29]: #yellow
					land_on_yellow()
				elif p.position in [31,32,34]: #green
					land_on_green()
				elif p.position in [37,39]: #blue
					land_on_blue()
				else:
					pass
				
				if roll[2] == True:
					count+=1
					fout.write(p.name + ': you rolled a double, number ' + str(count) + ', go again \n')
					if count == 3:
						p.position = 10
						fout.write(p.name + ' you have been send to jail \n')
						fout.write('--------  done  -------\n')
						p.in_jail = True
						break
				else:
					fout.write('--------  done  -------\n')
					fout.write('\n')
					fout.write('\n')
					break
	
	
	#sorted_x = sorted(all_players, key=operator.attrgetter('name'))
	#print(sorted_x)
	#all_players.sort(key=lambda x: x.name)
	#employees.  sort(key=lambda x: x.name)
	#print(all_players)

	print('==============================')
	print('==============================')
	for p in Monofn.all_players:
		print (p.name, p.cash, p.trains+p.services+p.properties)
	#print(sorted(all_players, key=lambda x: x.cash))
					           #p.properties
		
	#sortedByName = sorted(all_players, key=lambda x: x.name)
	#print(all_players)
	#if x[1]:
		#print ('yes')
	fout.close()

	
