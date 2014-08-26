import os
import shutil 

location = r"D:\OCR_FIN\SPEC\MV BULLETINS"
			
def move_sameloc(path): #moves folders that were not bagged (do not have a data folder)
	for item in os.listdir(path):
		ofolder = "%s\\%s" %(location, item)
		imagefolder = ofolder + "\\IMAGES_METADATA"
		datafolder = ofolder + "\\data"
		
		for folder in os.listdir(ofolder):
			old_loc = str(ofolder) + "\\" + str(folder)
			print old_loc
			if old_loc.endswith("IMAGES"):
				 shutil.move(old_loc, imagefolder)
				 print str(old_loc) + " moved to " + str(imagefolder)
			elif old_loc.endswith("IMAGES_CR2"):
				 shutil.move(old_loc, imagefolder)
				 print str(old_loc) + " moved to " + str(imagefolder)
			elif old_loc.endswith("METADATA"):
				 shutil.move(old_loc, imagefolder)
				 print str(old_loc) + " moved to " + str(imagefolder)		
			else:
				print "there is nothing else to do"

# if 2 PDFS exist this will create an access folder and move the access copy there 
def move_pdf(path): 
	for folder in os.listdir(path):
		ofolder = str(path) + "\\" + str(folder)
		for subfolder in os.listdir(ofolder):
			if subfolder == 'PDF':
				pdf_folder = str(ofolder) + "\PDF"
				for PDF in os.listdir(pdf_folder):
					access_loc = str(ofolder) + "\ACCESS_PDF"
					if PDF.endswith("_ST.pdf"):
						small_pdf = str(pdf_folder) +"\\" + str(PDF)
						if os.path.isdir(access_loc):
							shutil.move(small_pdf, access_loc)
						else:
							os.mkdir(access_loc, 0755)
							shutil.move(small_pdf, access_loc)
					elif PDF.endswith("optimized.pdf"):
						small_pdf = str(pdf_folder) +"\\" + str(PDF)
						if os.path.isdir(access_loc):
							shutil.move(small_pdf, access_loc)
						else:
							os.mkdir(access_loc, 0755)
							shutil.move(small_pdf, access_loc)
					elif PDF.endswith("opt.pdf"):
						small_pdf = str(pdf_folder) +"\\" + str(PDF)
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