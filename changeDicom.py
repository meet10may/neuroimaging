# Script to replace the PHI from the DICOM with a fake value
# Requires dicom  
import os
import dicom
import glob
baseDir='/Users/natht02/Documents/dicom'

#function to change the dicom header information. 
def dicomhdr(fname):
	#Read the dicom files
	dcm = dicom.read_file(fname,force=True)
	#print fname
	#Changing the DOB, Age and Weight and assign a fake value
	dcm.PatientBirthDate='19000909'
	dcm.PatientAge='100Y'
	dcm.PatientWeight='100'
	dcm.save_as(fname)
	return dcm


for root, dirs, files in os.walk(baseDir):
	for x in files:
		#finding all the files with extension as .dcm
		if x.endswith(".dcm"):
    			name =(os.path.join(root, x))
    			print name
    			


