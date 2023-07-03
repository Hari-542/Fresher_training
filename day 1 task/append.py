import os
import glob
data=""
source_path=input("Enter the source path:")
destination_path=input("Enter the destination path:")
f=glob.glob(source_path+"/*.txt")
for i in f:
    with open(destination_path,'a') as f:
        with open(i,'r') as a:
            f.write(a.read())

