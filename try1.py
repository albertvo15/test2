
import os

try:
  fp = open('sample.txt')
except IOError as e:
  print ('Unable to open file:', e)
