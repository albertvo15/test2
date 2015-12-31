

import os,sys

srcstr = 'BCX98321'
path = './WWW/'
dirs = os.listdir(path)

for file in dirs:
  filepath = path + file
  print filepath
  f = open (filepath)
  for line in f:
    print line
    if 'BCX98321' in line:
      print 'FOUND str in ' + file
      cmd = 'ls -al ' + file + '| cut -d " " -f 5,9'
      os.system(cmd)
