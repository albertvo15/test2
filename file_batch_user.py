
import re
import os
import sys
import fileinput

f = open ('/var/data/aga/users.txt')

users = []
for line in f.readlines():
#  print line
  line = line.rstrip("\r\n")
  users = re.split(r'[;,\s]\s*', line)
  for user in users:  
    passwd = user
    revpasswd = passwd[::-1]
    print user
    print revpasswd
    cmd = 'useradd ' + '-p ' + revpasswd + ' ' + user
#    cmd = 'useradd '  + user
    os.system(cmd)
