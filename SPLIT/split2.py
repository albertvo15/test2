import csv
import re

fname = "./syslog"
with open (fname) as fp:
  reader = csv.reader(fp,delimiter=' ')
  for row in reader:
    key_val = [col.split('=', 1) for col in row]
#    print key_val
#    print key_val[0][0]
    for index, elem in enumerate(key_val):
      print (index,elem) 
