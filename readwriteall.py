from os import listdir
import csv

mypath = 'E:/backup/entertainment/anime'
folders = [d for d in listdir(mypath)]

mypath2 = 'F:/anime'
folders2 = [d for d in listdir(mypath2) if d not in folders]

nameofFolders = open("C:/Users/Nushrat Humaira/anime_names_merged.csv","wb")
writer = csv.writer(nameofFolders,dialect='excel')
writer.writerows([folders])
