#Rename Files
import os

#Enter the name of the directory you want to access
path = "F:\\DePauw Digital Library 4 (Backup) STATE LIBRARY\\Daily Banner - 1968-11-01 - 1968-12-31"

os.chdir(path)

#To rename any file, just type in what you want to replace before the comma (inside
#f.replace()), and type in
#what you want to replace it with after the comma
#To rename the whole file, just put 'f' before the comma
[os.rename(f, f.replace(f, 'IDU_Putnam_TDB_' + f)) for f in os.listdir('.') if (not f.startswith('.') and not f.startswith('DePauw') and not f.startswith('System'))]
