import os
import types
import fnmatch

def list_directory(path):
  try: 
    type(path) is str
 
  except TypeError:
    print 'Path argument must be a string'


  try:
    os.path.exists(path)
  except IOError:
    print 'Directory does not exist'

  try:
    os.path.isfile(path)
  except IOError:
    print 'Path exists, but is not a directory'

  try:
    if os.path.isdir(path):
#      dir = os.listdir(path)
#      print dir
       for root,dir, files in os.walk(path):
         print root
         print ""
         for items in fnmatch.filter(files, "*"):
           print "..." + items
         print ""
  except IOError:
    print 'could not list directory'


#list_directory('./TEST')
list_directory('./TEST')
