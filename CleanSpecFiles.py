import os
from os import path
import sys

def deleteFiles(content):
	#GETTING FILE NAMES		
	if content[1][0:8] == 'FILENAME' :
		fileName = content[1][9:]
		fileNameSplitedArray = fileName.split(",")
		for i in range (0,len(fileNameSplitedArray)):
			fileNameSplited = fileNameSplitedArray[i].rstrip("\n")
			os.system("del /f "+fileNameSplited)
	#GETTING EXTENTIONS					
	if content[2][0:9] == 'EXTENSION' :
		extention = content[2][10:]
		extentionSplitedArray = extention.split(",")
		for i in range (0,len(extentionSplitedArray)):
			extentionSplited = extentionSplitedArray[i].rstrip("\n")
			os.system("del /f "+extentionSplited)
			
			
def underFolders(pathSplited,content):
	for o in os.listdir(pathSplited):
		if os.path.isdir(os.path.join(pathSplited,o)):
			folders = os.path.join(pathSplited,o)
			os.chdir(folders)
			deleteFiles(content)
			underFolders(folders,content)
with open(sys.argv[1]) as f:
    content = f.readlines()
if content[0][0:6] == 'FOLDER' :
	paths = content[0][7:]
	pathSplitedArray = paths.split(",")
	#CD FOLDERS ONE BY ONE
	for i in range (0,len(pathSplitedArray)):
		pathSplited = pathSplitedArray[i].rstrip("\n")
		os.chdir(pathSplited)
		deleteFiles(content)
		underFolders(pathSplited,content)
        
		
				
		
			
# The file that contain the paths, filenames and extensions should be like that
# FOLDER firstpath,secondpath,etc... 
# FILENAME *filename*.*,etc..
# EXTENSION *.ext
