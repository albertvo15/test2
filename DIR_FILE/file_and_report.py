#!/usr/bin/python

import os

path = '/var/data/agk/'

srcstr = 'BCX98321'

files = os.listdir(path)


for myfile in files:
  cmd = 'grep BCX98321 ' + path + myfile + ' | wc -l' 
  if   ( `os.system(cmd )`):
    print  myfile
    cmd2 = 'ls -al ' + path + myfile + ' | cut -d " " -f 5-9' 
    res2 = os.system(cmd2 )
    print res2
  else:
     continue
