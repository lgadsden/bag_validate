import os
import shutil
location = r"C:\Users\gadsden\Desktop\YEARBOOKS"

def copy_pdfs(path):
	for item in os.listdir(path):
		ofolder = location + '\\' + item 
		pdf_folder = ofolder + '\\data\\PDF'
		for file in os.listdir(pdf_folder):
			pdf_len = len(str(file))
			last_let = pdf_len
			first_let = pdf_len - 7
			if str(file)[first_let:last_let] !=  "_ST.pdf":
				old_file = pdf_folder + "\\" + file
				new_loc = "C:\Users\gadsden\Desktop\Bell_Cote_Access"
				shutil.copy(old_file,new_loc)
				print file + " moved " + new_loc
				
		
		
		
		
copy_pdfs(location)

	