#!/usr/bin/env python
import subprocess
import os
import re
from multiprocessing import Pool 

def gen(directory):
  dir=[]
  for root, dirs, files in os.walk(directory, topdown=True):
    for name in dirs:
      dir.append(os.path.join(root,name))
  return dir

def sync(directory):
  src = "/home/student-04-ac56dcd078cc/data/prod/"

  dest = "/home/student-04-ac56dcd078cc/data/prod_backup/"
  print ("Copying data from {} to {}".format(src,dest))
  subprocess.call(["rsync", "-arq", src, dest])

#sync("/home/student-04-ac56dcd078cc/data")
#gen("/home/student-04-ac56dcd078cc/data/prod")
if __name__ == "__main__":
  d=gen("/home/student-04-ac56dcd078cc/data/prod")
  p=Pool(len(d))
  p.map(sync,d)

