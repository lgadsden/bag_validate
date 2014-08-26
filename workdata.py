import os
import shutil 

location = r"D:\OCR_FIN\SPEC\MV BULLETINS"

#deletes the txt files that bagger creates inside the main folder
def delbaginfo(path): # replace path with project folder location
    for root, dirs, files in os.walk(path): 
        for currentFile in files: #iterates through all of the files. finds and deletes bagger files. 
			if currentFile == "bagit.txt":
				os.remove("%s\\bagit.txt")%(root)
				print "bag file removed"
			elif currentFile == "bag-info.txt":
				os.remove("%s\\bag-info.txt")%(root)
				print "bag file removed"
			elif currentFile == "manifest-md5.txt":
				os.remove("%s\\manifest-md5.txt")%(root)
				print "bag file removed"
			elif currentFile == "tagmanifest-md5.txt":
				os.remove("%s\\tagmanifest-md5.txt")%(root)
				print "bag file removed"
				
# creates an a folder that combines images and metadata
def create_imagefolder(path):
	for item in os.listdir(path):
		newp = "%s\\%s\\IMAGES_METADATA" %(path,item)
		if os.path.isdir(newp):
			print "it already exist"
		else:
			os.mkdir(newp, 0755)
			
# moves the image and metadata folders together and the PDF folder up once				
def move_folderup(path):
	for item in os.listdir(path):
		ofolder = "%s\\%s" %(location,item)
		imagefolder = "%s\\IMAGES_METADATA" %(ofolder)
		datafolder = "%s\\data" %(data)
		if os.path.isdir(datafolder):
			for folder in os.listdir(datafolder):
				old_loc = "%s\\%s" %(datafolder,folder)
				if old_loc.endswith("IMAGES"):
					 shutil.move(old_loc, imagefolder)
					 print "%s moved to %s" %(old_loc, imagefolder)
				elif old_loc.endswith("IMAGES_CR2"):
					 shutil.move(old_loc, imagefolder)
					 print "%s moved to %s" %(old_loc, imagefolder)
				elif old_loc.endswith("METADATA"):
					 shutil.move(old_loc, imagefolder)
					 print "%s moved to %s" %(old_loc, imagefolder) 		
				elif old_loc.endswith("PDF"):
					shutil.move(old_loc, ofolder)
					print "%s moved to %s" %(old_loc, ofolder)
				else:
					print "there is nothing else to do"
		else:
			print "data folder does not exist"
			
# deletes the data folder (if it is empty)
def deletedata(path):
    for item in os.listdir(path):
		dfolder = "%s\\%s\\data" %(path, item)
		if os.path.isdir(dfolder):
			os.rmdir(dfolder)
			print "%s has been removed" %(dfolder)
		else:
			print "there was nothing there"
	
# if 2 PDFS exist this will create an access folder and move the access copy there 
def move_pdf(path): 
	for folder in os.listdir(path):
		ofolder = "%s\\%s" %(path, folder)
		for subfolder in os.listdir(ofolder):
			if subfolder == 'PDF':
				pdf_folder = "%s\\PDF" (ofolder)
				for PDF in os.listdir(pdf_folder):
					access_loc = "%s\\ACCESS_PDF" %(ofolder)
					if PDF.endswith("_ST.pdf"):
						small_pdf = "%s\\%s" %(pdf_folder, PDF)
						if os.path.isdir(access_loc):
							shutil.move(small_pdf, access_loc)
						else:
							os.mkdir(access_loc, 0755)
							shutil.move(small_pdf, access_loc)
					elif PDF.endswith("optimized.pdf"):
						small_pdf = "%s\\%s" %(pdf_folder, PDF)
						if os.path.isdir(access_loc):
							shutil.move(small_pdf, access_loc)
						else:
							os.mkdir(access_loc, 0755)
							shutil.move(small_pdf, access_loc)
					elif PDF.endswith("opt.pdf"):
						small_pdf = "%s\\%s" %(pdf_folder, PDF)
						if os.path.isdir(access_loc):
							shutil.move(small_pdf, access_loc)
						else:
							os.mkdir(access_loc, 0755)
							shutil.move(small_pdf, access_loc)								
					else:
						print "There are no access PDFs in the folder"
			else:
				print "There are no PDF folders here"
				
	
			
				




#delbaginfo(location)
#create_imagefolder(location)
#move_folderup(location)
#deletedata(location)
#move_pdf(location)

