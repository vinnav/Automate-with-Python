
# selectiveCopy.py - a program that walks through a folder tree and searches 
# for files with a certain file extension (such as .pdf or .jpg) to copy
# from current folder to a new folder.
import os, shutil

ext = input("Choose the file extension to copy (\".xxx\"): ")
folder = input("Input directory absolute path, or leave blank for cwd: ") or os.getcwd()
destinationFolder = input("Enter destination folder (outside origin folder): ")

# Walk through current folders
for foldername, subfolders, filenames in os.walk(folder):
        #Add all the selected files in the origin folder to destination folder.
    for filename in filenames:
        if filename.endswith(ext):
            print("copying %s..." %(filename))
            #print("origin: " + os.path.join(foldername, filename))
            #print("destination: " + os.path.join(destinationFolder, filename))
            shutil.copy(os.path.join(foldername, filename), os.path.join(destinationFolder, filename))
