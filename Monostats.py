#!/usr/bin/env python
from random import randint
from operator import attrgetter

import logging
import matplotlib.pyplot as plt
import numpy as np
import Monofn
import operator
import sys

'''def land_on_railroad():
	for r in Monofn.all_railroads:
		if r.position == p.position:
			if r.name in unowend_properties:
				res = input(p.name + ' you have ' + str(p.cash) + ' and landed in '+ r.name + ' Railroad, would you like to buy it for '+ str(r.price) + '? :')
				if res == 'Y' or res == 'y' or res == 'yes':
					p.trains.append(r.name)
					p.cash -= r.price
					unowend_properties.remove(r.name)
					fout.write(p.name +' you just bought ' + r.name + ' now you have ' + str(p.cash) + '\n')
				else:
					pass
					#Player decided not to buy, implement auction logic
			else:
				for k in Monofn.all_players:
					if r.name in k.trains:
						if p.name != k.name:
							fout.write(p.name + ' ' + r.name + ' Railroad is owned by ' + k.name + ' you have to pay ' + str(r.rent[len(k.trains)-1]) + ' rent \n')
							k.cash +=r.rent[len(k.trains)-1]
							p.cash -=r.rent[len(k.trains)-1]
							fout.write(p.name + ' now has ' + str(p.cash) + '\n')
							fout.write(k.name + ' now has ' + str(k.cash) + '\n')
	return'''

'''def land_on_utility():
	for u in Monofn.all_utilities:
		if u.position == p.position:
			if u.name in unowend_properties:
				res = input(p.name + ' you have ' + str(p.cash) + ' and landed in '+ u.name + ' would you like to buy it for '+ str(u.price) + '? :')
				if res == 'Y' or res == 'y' or res == 'yes':
					p.services.append(u.name)
					p.cash -= u.price
					unowend_properties.remove(u.name)
					fout.write(p.name +' you just bought ' + u.name + ' now you have ' + str(p.cash) + '\n')
				else:
					pass
					#Player decided not to buy, implement auction logic
			else:
				for k in Monofn.all_players:
					if u.name in k.services:
						if p.name != k.name:
							n1, n2 , d = Monofn.Roll()
							k.cash +=(n1+n2)*u.rent[len(k.services)-1]
							p.cash -=(n1+n2)*u.rent[len(k.services)-1]
							fout.write(p.name + ' ' + u.name + ' is owned by ' + k.name + ' you have to pay ' + str((n1+n2)*u.rent[len(k.services)-1]) + ' rent \n')
							fout.write(p.name + ' now has ' + str(p.cash) + '\n')
							fout.write(k.name + ' now has ' + str(k.cash) + '\n')
	return'''

'''def land_on_brown():
	for b in Monofn.all_brown:
		if b.position == p.position:
			if b.name in unowend_properties:
				res = input(p.name + ' you have ' + str(p.cash) + ' and landed in '+ b.name + ' would you like to buy it for '+ str(b.price) + '? :')
				if 'y' in res or 'Y' in res:
					p.properties.append(b.name)
					p.nbrown += 1
					p.cash -= b.price
					unowend_properties.remove(b.name)
					fout.write(p.name +' you just bought ' + b.name + ' now you have ' + str(p.cash) + ' remaining \n')
				else:
					pass
					#Player decided not to buy, implement auction logic
			else:
				for player in Monofn.all_players:
					if b.name in player.properties:
						if p.name != player.name:
							if player.nbrown == b.nset:
								if b.n_house == 0:#set but no house
									fout.write(p.name+': '+b.name+' is owned by '+player.name+' and owns all properties, pay double rent '+str(2*b.rent[1])+' \n')
									player.cash += b.rent[1]*2
									p.cash -= b.rent[1]*2
									#print ('set but no house '+p.name + ' pay ' +str(b.rent[1])+' to '+ player.name)
									print(p.name+' pay '+ player.name+' '+str(2*b.rent[b.rent[1]])+' for '+b.name+''+str(p.cash)+''+player.cash)
								else:
									player.cash += b.rent[b.n_house +1]
									p.cash -= b.rent[b.n_house +1]
									#print ('set and houses '+p.name + ' pay ' + str(rent[b.n_house +1])+' to '+ player.name)
									print(p.name+' pay '+ player.name+' '+str(b.rent[b.n_house+1])+' for '+b.name)
							else:
								fout.write(p.name + ' ' + b.name + ' is owned by ' + player.name + ' you have to pay ' + str(b.rent[0]) + ' rent \n')
								print(p.name+' pay '+ player.name+' '+str(b.rent[0])+' for '+b.name)
								player.cash += b.rent[0]
								p.cash -= b.rent[0]
	return'''

'''def land_on_blue():
	for b in Monofn.all_blue:
		if b.position == p.position:
			if b.name in unowend_properties:
				res = input(p.name + ' you have ' + str(p.cash) + ' and landed in '+ b.name + ' would you like to buy it for '+ str(b.price) + '? :')
				if 'y' in res or 'Y' in res:
					p.properties.append(b.name)
					p.nblue += 1
					p.cash -= b.price
					unowend_properties.remove(b.name)
					fout.write(p.name +' you just bought ' + b.name + ' now you have ' + str(p.cash) + ' remaining \n')
				else:
					pass
					#Player decided not to buy, implement auction logic
			else:
				for player in Monofn.all_players:
					if b.name in player.properties:
						if p.name != player.name:
							if player.nbrown == b.nset:
								fout.write(p.name + ': ' + b.name + ' is owned by ' + player.name + ' and owns all properties you have to pay double rent ' + str(2* b.rent) + ' \n')
								player.cash += b.rent*2
								p.cash -= b.rent*2
							else:
								fout.write(p.name + ' ' + b.name + ' is owned by ' + player.name + ' you have to pay ' + str(b.rent) + ' rent \n')
								player.cash += b.rent
								p.cash -= b.rent
	return'''


# class rent

rent_hotel = [250, 0, 450, 0, 200, 550, 0, 550, 600, 0, 
			  750, 50, 750, 900, 0, 950, 0, 950, 1000, 0, 
			  1050, 0, 1050, 1100, 200, 1150, 1150, 50, 1200, 0, 
			  1275, 1275, 0, 1400, 200, 0, 1500, 0, 2000, 0]

if __name__ == "__main__":
	"""
	Some stats of the Monopoly game
	"""
	#a mess that should be fixed
	nroll = 50
	trains, utilities, brown, lblue, rosa, orange, red, yellow, green, blue, chance, communitychest, tax, other = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16, pos17, pos18, pos19, pos20, pos21, pos22, pos23, pos24, pos25, pos26, pos27, pos28, pos29, pos30, pos31, pos32, pos33, pos34, pos35, pos36, pos37, pos38, pos39, pos40 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
	# uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, x10, x11, x12, x13, x14, x15 = 0, 0,0,0,0,0
	pos1m, pos2m, pos3m, pos4m, pos5m, pos6m, pos7m, pos8m, pos9m, pos10m, pos11m, pos12m, pos13m, pos14m, pos15m, pos16m, pos17m, pos18m, pos19m, pos20m, pos21, pos22, pos23, pos24, pos25, pos26, pos27, pos28, pos29, pos30, pos31, pos32, pos33, pos34, pos35, pos36, pos37, pos38, pos39, pos40 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
	

	for i in range(nroll):
		for p in Monofn.all_players:
			# roll = Monofn.Roll()


			in_turn, count  = True, 0
			while (in_turn):
				roll = Monofn.Roll()
				p.position = p.position + roll[0] + roll[1]
				#check for passing GO
				if p.position>40:
					p.position -=40
				
				# go to jail
				if p.position == 30:
					p.position =10
				
				# print (p.name+' roll a '+str(roll[0]+roll[1])+' in '+str(p.position))
				if p.position == 1:
					pos1+=1
					pos1m += rent_hotel[p.position-1]
					brown=+1
					# print(unoh)
				elif p.position == 2:
					dos+=1
					communitychest+=1
				elif p.position ==3:
					tres+=1
					tresh+=rent_hotel[p.position-1]
				elif p.position ==4:
					cua+=1
					tax+=1
				else:
					pass

				'''if p.position in [5,15,25,35]:
					trains +=1
				elif p.position in [1,3]:
					brown+=1
				elif p.position in [6,8,9]:
					lblue+=1
				elif p.position in [11,13,14]:
					rosa +=1
				elif p.position in [16,18,19]:
					orange +=1
				elif p.position in [21,23,24]:
					red+=1
				elif p.position in [26,27,29]:
					yellow+=1
				elif p.position in [31,32,34]:
					green+=1
				elif p.position in [37,39]:
					blue+=1
				elif p.position in [7,22,36]:
					chance+=1
				elif p.position in [2,17,33]:
					communitychest +=1
				elif p.position in [4,38]:
					tax+=1
				elif p.position in [12,28]:
					utilities +=1
				else:
					other+=1'''

				if roll[2] == True:
					count+=1
					if count == 3:
						p.in_jail = True
						break
				else:
					break
	

	print('==============================')
	# print(nroll)
	#plot individual squares
	xc = np.arange(3)
	plt.bar(xc, height=[uno,dos, tres, ])
	plt.xticks(xc, ['uno', 'dos', 'tres']);
	plt.show()


	#plot color sets
	x = np.arange(14)
	plt.bar(x, height=[brown,trains, utilities, lblue, rosa, orange, red, yellow, green, blue, chance, communitychest, tax, other])
	plt.xticks(x, ['brown','trains', 'utilities', 'lblue', 'rosa', 'orange', 'red', 'yellow', 'green', 'blue', 'chance', 'communitychest', 'tax', 'other']);
	plt.show()

	#plot money
	xm = np.arange(2)
	plt.bar(xm, height=[unoh, tresh])
	plt.xticks(xm, ['uno', 'tres']);
	plt.show()

	# plots money
	# Monofn.hists()

