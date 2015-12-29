
import subprocess

myfilename = 'FILE1'
cmd = 'ls -al ' +  myfilename

#with open ('output.txt', 'w') as out:
#   return_code = subprocess.call(cmd, stdout=out)


filename = 'FILE1'
dest_filename = 'FILE2'
logfile = 'FILE2'
#subprocess.call(['ls', '-al', filename, '>', dest_filename])
#proc = subprocess.Popen(["ls", "-al", filename, ">", dest_filename])
#proc = subprocess.Popen(['ls', '-l', filename], stdout =subprocess.PIPE,shell=True)
#proc = subprocess.Popen(['ls', '-l', filename],shell=True)
print cmd
proc = subprocess.Popen(cmd, shell=True)
(out,err) = proc.communicate()
print "program output:", out

