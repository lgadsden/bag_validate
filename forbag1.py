import os
import bagit 

location = map([r"C:\Users\gadsden\Desktop\haha", r"C:\Users\gadsden\Desktop\rappuin"]) #insert the directory 1 levels above the folders you want to bag

def bag_folders(path): # bags files 1 levels below directory i.e. -Law -> Law1998
	for item in os.listdir(path):
		folder = str(path) + "\\" + str(item)
		datafolder = '%s\data' %(folder)
		if os.path.exists(datafolder) == True: # test if bag exists so that it will not bag over existing bag
			print "Already bagged:" + str(folder)
		else: # if bag does not exist, creates a bag
			bag = bagit.make_bag(folder, {'Contact-Name': 'Lawrence Gadsden'})
			print "completed bag for:" + str(folder)

def validate_bags(path): #validates bags in folders 1 level below path
	for item in os.listdir(path):
		folder = str(path) + "\\" + str(item)
		datafolder = str(folder) + '\data'
		if os.path.exists(datafolder) == False: #skips folders that are not bagged ... leaves comment
			print "Not validated, not a bag:" + str(folder)
		else: #checks if bags are valid
			bag = bagit.Bag(folder)
			if bag.is_valid(): 
				print "Valid Bag:" + str(folder)
			else:
				print "Bag not valid:" + str(folder)

bag_folders(location)
#validate_bags(location)