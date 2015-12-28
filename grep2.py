
import os

directory = './TEST/'

for file in os.listdir(directory):
  filepath = directory+file
  print filepath
  f = open(filepath)
  for line in f:
    if 'apple' in line:
      print "FOUND in " + file
  f.close()
