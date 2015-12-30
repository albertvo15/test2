import re

logstring = '[1242248375] SERVICE ALERT: myhostname.com;DNS: Recursive;CRITICAL;SOFT;1;CRITICAL - Plugin timed out while executing system call'
exp = re.compile('^\[(\d+)\] ([A-Z ]+): ([A-Za-z0-9.\-]+);[^;]+;([A-Z]+);')
m = exp.search(logstring)

match = re.match(r'^\[(\d+)\] (.*?): (.*?);.*?;(.*?);',logstring)

#for s in m.groups():
#    print s

mdate = match.group(1)
malert = match.group(2)
mhost = match.group(3)
mmsg1 = match.group(4)

print match.group(1)

print 'date ' + mdate
print 'alert ' + malert
print 'host ' + mhost
print 'msg1 ' + mmsg1



