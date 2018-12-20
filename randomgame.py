# Tim Oskarsson
# A way over-complicated random number game

import random
import time
import os.path

#Create the random number, start counter, ask for name 
randnr = random.randint(1, 10)
print (randnr, " #this is for debugging")
count = 0
name = input("Input player name: ") 

#Loop after creating random number and variable
while True:
	#give user choice, convert choice to interger
	guess = int(input("Pick a number between 1 and 10: "))
	#add 1 to count per input 
	count += 1
	#If guess (>|<|=) randnr then do x
	if randnr == guess:
		print()
		print ("#########") 
		print ("Correct")
		print ( str(count) + " Guesses" )
		print ("#########")
		time.sleep(1)
		
		#Save scores? If no file, create file + save? if no, quit
		save = input ("Save score? y/n# ")
		if save == "y":
			if os.path.isfile("scores.txt") == True: 
				scores = open("scores.txt", "a+")
				scores.write(name + ": " + str(count) + " Guesses " + ": " + time.strftime("%a %H:%M:%S \n"))
				print ("Score saved*")
				time.sleep(1) #Sleep for 1 second style points
				quit()
			elif os.path.isfile("scores.txt") == False:
				crfile = input("Create scores.txt? y/n# ")
				if crfile == "y":
					scores = open("scores.txt", "a+")
					scores.write(name + ": " + str(count) + " Guesses " + ": " + time.strftime("%a %H:%M:%S \n"))
					print ("scores.txt created, score saved")
					time.sleep(1)
					quit()
				else:
					print("file not created, score not saved.")
					time.sleep(1)
					quit()
		else: 
			print ("Score not saved.")
			time.sleep(1)
			quit()

	elif randnr >= guess:
		print ("Number is higher")
		time.sleep(0.5)
	elif randnr <= guess: 
		print ("Number is lower")
		time.sleep(0.5)