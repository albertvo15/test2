import csv
import re
fname = "/var/log/web.log"
with open(fname) as fp: 
    reader = csv.reader(fp, delimiter=' ')
    for row in reader:
        key_val = [col.split('=', 1) for col in row]
#        print(key_val)
#        print(key_val[0], key_val[1], key_val[7], key_val[2] , key_val[3]  )
        myip = key_val[0]
#        str = myip
#        myip = str.strip('[')
#        myip = str.strip(']')
        mydash1 = '-'
        myhits = key_val[7]
        mydash2 = '-'
        mydate = key_val[3]
        print(myip, mydash1, myhits, mydash2 , mydate  )
