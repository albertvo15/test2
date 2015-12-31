import csv
import re

fname = "./syslog"
with open (fname) as fp:
  for line in fp:
    (host,d1,d2,date, tz, http1, uri, http2, stat, hitcount) = re.split(' ', line)
    hitcount = hitcount.strip('\n')
    date = date.strip('[')
    date2,time = date.split(':',1)
    print host,time,date2,uri,hitcount
