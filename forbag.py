import os
import bagit 

location = r"C:\Users\Lawrence G\Desktop\cheetos" #insert the directory 2 levels above the folders you want to bag

def bag_folders(path): # bags files 2 levels below directory i.e. -Law -> Law1998 -> PDFS(are bagged)
	for item in os.listdir(path):
		folder = '%s\\%s' %(path, item)
		for sub in os.listdir(folder):
			subfolder = '%s\\%s' %(folder, sub)
			datasubfolder = '%s\data' %(subfolder)
			if os.path.exists(datasubfolder) == True: # test if bag exists so that it will not bag over existing bag
				print "Already bagged: %s" %(subfolder)
			else: # if bag does not exist, creates a bag
				bag = bagit.make_bag(subfolder, {'Contact-Name': 'Lawrence Gadsden'})
				print "completed bag for: %s" %(subfolder) 

def validate_bags(path): #validates bags in folders two levels below path
	for item in os.listdir(path):
		folder = '%s\\%s' %(path,item)
		for sub in os.listdir(folder):
			subfolder = '%s\\%s' %(folder, sub)
			datasubfolder = '%s\data' %(subfolder)
			if os.path.exists(datasubfolder) == False: #skips folders that are not bagged ... leaves comment
				print "Not validated, not a bag: %s" %(subfolder)
			else: #checks if bags are valid
				bag = bagit.Bag(subfolder)
				if bag.is_valid(): 
					print "Valid Bag: %s" %(subfolder)
				else:
					print "Bag not valid: %s" %(subfolder)

bag_folders(location)
validate_bags(location)