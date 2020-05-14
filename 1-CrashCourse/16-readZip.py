import zipfile, os
os.chdir("C:\\") # move to the folder with example.zip
exampleZip = zipfile.ZipFile("example.zip")
exampleZip.namelist()
# ["spam.txt", "cats/", "cats/catnames.txt", "cats/zophie.jpg"]

spamInfo = exampleZip.getinfo("spam.txt")
spamInfo.file_size
# 13908
spamInfo.compress_size
# 3828

"Compressed file is %sx smaller!" % (round(spamInfo.file_size / 
spamInfo.compress_size, 2))
# Compressed file is 3.63x smaller!
exampleZip.close()