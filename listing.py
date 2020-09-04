from os import listdir
from os.path import isfile, join
import os
path = os.getcwd() + "/03_eunbin"
files = [f for f in listdir(path) if isfile(join(path, f))]
files = [x for x in files if x.find(".jpg") != -1]
#print(files)
files = sorted(files)
f = open(path + ".txt",'w')
for i in files:
    data = path +"/"+ i
    #print(data)
    f.write(data)
    f.write("\n")
f.close()
