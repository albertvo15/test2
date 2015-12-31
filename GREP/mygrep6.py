

import os,sys
import subprocess

srcstr = 'BCX98321'
path = './TEST/'
dirs = os.listdir(path)

file3 = '~bodl/TRUE2/GIT/test2/TEST/FILE3'

for file in dirs:
  filepath = path + file
  print filepath
  f = open (filepath)
  for line in f:
    print line
    if 'apple' in line:
      print 'FOUND str in ' + file
      cmd = 'ls -al ' + file + '| cut -d " " -f 4,5,6,7,9'
      proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True)
      (out,err) = proc.communicate()

      print 'output ' + out
