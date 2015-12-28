
import os

directory = './TEST'
file = FILE1

grep = subprocess.Popen(['grep','-m1', 'apple',directory+'/file'],stdout=subprocess.PIPE)
found = grep.communicate()[0]
print found
