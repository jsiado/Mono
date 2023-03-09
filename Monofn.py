#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from random import randint
import sys

#players atributes, name, money, properties, etc
# could be improve
# todo ask the user for player names
class Player:
	def __init__(self, name, cash, trains, services, properties, nbrown, nlblue, nrosa, nnaranja, nred, nyellow, ngreen, nblue, position, out_of_jail_cards, in_jail, n_double, n_railroad, n_utility):
		self.name = name
		self.cash = cash
		self.trains = trains
		self.services = services
		self.properties = properties
		self.nbrown = nbrown
		self.nlblue = nlblue
		self.nrosa = nrosa
		self.nnaranja = nnaranja
		self.nred = nred
		self.nyellow = nyellow
		self.ngreen = ngreen
		self.nblue = nblue
		self.position = position
		self.out_of_jail_cards = out_of_jail_cards
		self.in_jail = in_jail
		self.n_double = n_double
		self.n_railroad = n_railroad
		self.n_utility = n_utility
	
	
all_players = [
	#add players here as needed
	Player('Patito', 1500, [], [], [],  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, False, 0, 0, 0),
	Player('Canijo', 1500, [], [], [], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, False, 0, 0, 0),
	Player('Marico', 1500, [], [], [], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, False, 0, 0, 0)
]


#class Properties:
	#def __init__(self, name, color, position, nset, price, mortgage, rent, rent1):
		#self.name = name
		##self.color = color
		#self.position = position
		#self.nset = nset
		#self.price = price
		#self.mortgage = mortgage
		#self.rent = rent
		#self.rent1 = rent1

#define another atribute for player saying ncolor and match it to n sset

#all_properties = [
	#Properties('Baltic', 'Brown', 1, 2, 60, ' xx', 2, 0),
	#Properties('Mediterranean', 'Brown', 3, 2, 60, ' xx', 4, 0),
	#Properties('Park_Place', 'Blue', 37, 2, 350, ' xx', 35, 0),
	#Properties('Boardwalk', 'Blue', 39, 2, 400, ' xx', 50, 0),
#]

class Brown:
	def __init__(self, name, color, position, nset, price, mortgage, h_cost, rent, n_house):
		self.name = name
		self.color = color
		self.position = position
		self.nset = nset
		self.price = price
		self.mortgage = mortgage
		self.h_cost = h_cost
		self.rent = rent
		self.n_house = n_house

all_brown = [
	Brown('Mediterranean', 'Brown', 1, 2, 60, 30, 50, [2, 4, 10, 30,  90, 160, 250], 0),
	Brown('Baltic',        'Brown', 3, 2, 60, 30, 50, [4, 8, 20, 60, 180, 320, 450], 0)
]


class lBlue:
	def __init__(self, name, color, position, nset, price, mortgage, h_cost, rent, n_house):
		self.name = name
		self.color = color
		self.position = position
		self.nset = nset
		self.price = price
		self.mortgage = mortgage
		self.h_cost = h_cost
		self.rent = rent
		self.n_house = n_house

all_lblue = [
	lBlue('Oriental',    'lBlue', 6, 3, 100, 50, 50, [6, 12, 30, 90, 270, 400, 550], 0),
	lBlue('Vermont',     'lBlue', 8, 3, 100, 50, 50, [6, 12, 30, 90, 270, 400, 550], 0),
	lBlue('Conneticut',  'lBlue', 9, 3, 120, 60, 50, [8, 16, 40, 100, 300, 450, 600], 0)
]

class Rosa:
	def __init__(self, name, color, position, nset, price, mortgage, h_cost, rent, n_house):
		self.name = name
		self.color = color
		self.position = position
		self.nset = nset
		self.price = price
		self.mortgage = mortgage
		self.h_cost = h_cost
		self.rent = rent
		self.n_house = n_house

all_rosa = [
	Rosa('St_Charles', 'Rosa', 11, 3, 140, 70, 100, [10, 20, 50, 150, 450, 625, 750], 0),
	Rosa('States',     'Rosa', 13, 3, 140, 70, 100, [10, 20, 50, 150, 450, 625, 750], 0),
	Rosa('Virginia',   'Rosa', 14, 3, 160, 80, 100, [12, 24, 60, 180, 500, 700, 900], 0)
]

class Naranja:
	def __init__(self, name, color, position, nset, price, mortgage, h_cost, rent, n_house):
		self.name = name
		self.color = color
		self.position = position
		self.nset = nset
		self.price = price
		self.mortgage = mortgage
		self.h_cost = h_cost
		self.rent = rent
		self.n_house = n_house

all_naranja = [
	Naranja('St_James', 'Naranja', 16, 3, 180, 90, 100, [14, 28, 70, 200, 550, 750, 950], 0),
	Naranja('Tennesse', 'Naranja', 18, 3, 180, 90, 100, [14, 28, 70, 200, 550, 750, 950], 0),
	Naranja('Newyork',  'Naranja', 19, 3, 200, 100, 100, [16, 32, 80, 220, 600, 800, 1000], 0)
]

class Red:
	def __init__(self, name, color, position, nset, price, mortgage, h_cost, rent, n_house):
		self.name = name
		self.color = color
		self.position = position
		self.nset = nset
		self.price = price
		self.mortgage = mortgage
		self.h_cost = h_cost
		self.rent = rent
		self.n_house = n_house

all_red = [
	Red('Kentucky', 'Red', 21, 3, 220, 110, 150, [18, 36, 90, 250, 700, 875, 1050], 0),
	Red('Indiana',  'Red', 23, 3, 220, 110, 150, [18, 36, 90, 250, 700, 875, 1050], 0),
	Red('Illinois',  'Red', 24, 3, 240, 120, 150, [20, 40, 100, 300, 750, 925, 1100], 0)
]

class Yellow:
	def __init__(self, name, color, position, nset, price, mortgage, h_cost, rent, n_house):
		self.name = name
		self.color = color
		self.position = position
		self.nset = nset
		self.price = price
		self.mortgage = mortgage
		self.h_cost = h_cost
		self.rent = rent
		self.n_house = n_house

all_yellow = [
	Yellow('Atlantic', 'Yellow', 26, 3, 260, 130, 150, [22, 44, 110, 330, 800, 975, 1150], 0),
	Yellow('Ventnor',  'Yellow', 27, 3, 260, 130, 150, [22, 44, 110, 330, 800, 975, 1150], 0),
	Yellow('Marvin',   'Yellow', 29, 3, 280, 140, 150, [24, 48, 120, 360, 850, 1025, 1200], 0)
]

class Green:
	def __init__(self, name, color, position, nset, price, mortgage, h_cost, rent, n_house):
		self.name = name
		self.color = color
		self.position = position
		self.nset = nset
		self.price = price
		self.mortgage = mortgage
		self.h_cost = h_cost
		self.rent = rent
		self.n_house = n_house

all_green = [
	Green('Pacific',         'Green', 31, 3, 300, 150, 200, [26, 52, 130, 390, 900, 1100, 1275], 0),
	Green('North_Carolina',  'Green', 32, 3, 300, 150, 200, [26, 52, 130, 390, 900, 1100, 1275], 0),
	Green('Pensylvania',     'Green', 34, 3, 320, 160, 200, [28, 56, 150, 450, 1000, 1200, 1400], 0)
]

class Blue:
	def __init__(self, name, color, position, nset, price, mortgage, h_cost, rent, n_house):
		self.name = name
		self.color = color
		self.position = position
		self.nset = nset
		self.price = price
		self.mortgage = mortgage
		self.h_cost = h_cost
		self.rent = rent
		self.n_house = n_house

all_blue = [
	Blue('Park_Place', 'Blue', 37, 2, 350, 175, 200, [35, 70, 175, 500, 1100, 1300, 1500], 0),
	Blue('Boardwalk',  'Blue', 39, 2, 400, 200, 200, [50, 100, 200, 600, 1400, 1700, 2000], 0)
]


class Railroads:
	def __init__(self, name, position, price, mortgage, rent):
		self.name = name
		self.position = position
		self.price = price
		self.mortgage = mortgage
		self.rent = rent

all_railroads = [
	Railroads('Reading Railroad', 5, 200,  100, [25, 50, 100, 200]),
	Railroads('Pensylvania Railroad',15, 200, 100,  [25, 50, 100, 200]),
	Railroads('B and O Railroad', 25, 200, 100, [25, 50, 100, 200]),
	Railroads('Short Line', 35, 200, 100, [25, 50, 100, 200])
]

class Utility:
	def __init__(self, name, position, price, mortgage, rent):
		self.name = name
		self.position = position
		self.price = price
		self.mortgage = mortgage
		self.rent = rent

all_utilities = [
	Utility('Electric', 12, 150,  75, [4, 10]),
	Utility('Water',28, 150, 75,  [4, 10])
]

def Roll():
	#todo include doubles and counters of double
	roll_double = False
	roll1 = randint(1,6)
	roll2 = randint(1,6)
	if roll1==roll2:
		roll_double = True
	return [roll1, roll2, roll_double]

def plot(x,y):
	plt.bar(x,y)
	plt.show()

def bank_properties():
	unowend_properties = [
		'Baltic',
		#'community
		'Mediterranean',
		#'inctax'
		'Reading Railroad',
		'Oriental',
		#'chance'
		'Vermont',
		'Conneticut',
		#'visit'
		'St_Charles',
		'Electric',
		'States',
		'Virginia',
		'Pensylvania Railroad',
		'St_James',
		#'chance'
		'Tennesse',
		'Newyork',
		#'free'
		'Kentucky',
		#'community'
		'Indiana',
		'Illinois',
		'B and O Railroad',
		'Atlantic',
		'Ventnor',
		'Water',
		'Marvin',
		#'jail'
		'Pacific',
		'North_Carolina',
		#'community'
		'Pensylvania',
		'Short Line' ,
		#'chance' 
		'Park_Place',
		#'luxtax'
		'Boardwalk'
	]
	return unowend_properties

def hists():
	count_roll =[0.]*13
	count_prop =[0.]*41
	count_money = [0.]*41
	
	rent_hotel = [250, 0, 450, 0, 200, 550, 0, 550, 600, 0, 
			  750, 50, 750, 900, 0, 950, 0, 950, 1000, 0, 
			  1050, 0, 1050, 1100, 200, 1150, 1150, 50, 1200, 0, 
			  1275, 1275, 0, 1400, 200, 0, 1500, 0, 2000, 0]
	
	current_position = 0
	nroll =200
	
	for i in range (nroll):
		roll =randint(1,6) +randint(1,6)
		
		count_roll[roll]= count_roll[roll]+1
		
		current_position = current_position + roll
		
		if current_position > 40:
			current_position -=40
			
		if current_position == 30:
			current_position = 10
			
		count_prop[current_position] = count_prop[current_position] +1
		count_money[current_position] = count_money[current_position]+rent_hotel[current_position-1]

	plot(range(len(count_prop)), count_prop)
	plot(range(len(count_roll)), count_roll)
	plot(range(len(count_money)), count_money)

def chance_cards():
	Chance = ['Go to jail', 
		'Advance to Boarwalk', 
		'Advance to the nearest railroad', 
		'Advance to St Charles Place', 
		'Advance to Illinois avenue',
		'Advance to Go',
		'Bank pays you 50',
		'Advance to the nearest railroad',
		'Go back three spaces',
		'Free get out of jail card',
		'Make repairs',
		'Your building loan matures. collect 150',
		'Advance to the nearest utility',
		'speeding fine',
		'Pay each player 50',
		'Take a trip to reading railroad']
	return Chance 

def Community_chest_cards():
	Chest = ['Go to jail', 
		'Doctor fee. Pay 50',
		'You inherit 100', 
		'recive 25', 
		'From your sale of stocks you get 50',
		'Advance to Go',
		'Hollyday fund receive 100',
		'Income tax refund. Collect 20',
		'Life insurance matures. Collect 100',
		'Free get out of jail card',
		'Make repairs',
		'Bank error. Collect 200',
		'Hospital fees. Pay 100',
		'School Fees. Pay 50',
		'Beauty contest. Collect 10',
		'Your Birthday. Collect 10 from each player']
	return Chest 

	pass