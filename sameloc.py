import os
import shutil 

location = r""
			
def move_sameloc(path): #moves folders that were not bagged (do not have a data folder)
	for item in os.listdir(path):
		ofolder = "%s\\%s" %(location, item)
		imagefolder = "%s\\IMAGES_METADATA" %(ofolder)
		datafolder = "%s\\data" %(ofolder)
		
		for folder in os.listdir(ofolder):
			old_loc = "%s\\%s" %(ofolder,folder)
			print old_loc
			if old_loc.endswith("IMAGES"):
				 shutil.move(old_loc, imagefolder)
				 print "%s moved to %s" %(olf_loc,imagefolder)
			elif old_loc.endswith("IMAGES_CR2"):
				 shutil.move(old_loc, imagefolder)
				 print "%s moved to %s" %(old_loc,imagefolder)
			elif old_loc.endswith("METADATA"):
				 shutil.move(old_loc, imagefolder)
				 print "%s moved to %s" %(old_loc,imagefolder)		
			else:
				print "there is nothing else to do"

# if 2 PDFS exist this will create an access folder and move the access copy there 
def move_pdf(path): 
	for folder in os.listdir(path):
		ofolder = "%s\\%s" %(path,folder)
		for subfolder in os.listdir(ofolder):
			if subfolder == 'PDF':
				pdf_folder = "%s\PDF" %(ofolder)
				for PDF in os.listdir(pdf_folder):
					access_loc = "%s\\ACCESS_PDF" %(ofolder) #check on the number of "\" here
					if PDF.endswith("_ST.pdf"):
						small_pdf = "%s\\%s" %(pdf_folder,PDF)
						if os.path.isdir(access_loc):
							shutil.move(small_pdf, access_loc)
						else:
							os.mkdir(access_loc, 0755)
							shutil.move(small_pdf, access_loc)
					elif PDF.endswith("optimized.pdf"):
						small_pdf = "%s\\%s" %(pdf_folder,PDF)
						if os.path.isdir(access_loc):
							shutil.move(small_pdf, access_loc)
						else:
							os.mkdir(access_loc, 0755)
							shutil.move(small_pdf, access_loc)
					elif PDF.endswith("opt.pdf"):
						small_pdf = "%s\\%s" %(pdf_folder,PDF)
						if os.path.isdir(access_loc):
							shutil.move(small_pdf, access_loc)
						else:
							os.mkdir(access_loc, 0755)
							shutil.move(small_pdf, access_loc)								
					else:
						print "There are no access PDFs in the folder"
			else:
				print "There are no PDF folders here"
				
	
			

move_sameloc(location)
move_pdf(location) 
