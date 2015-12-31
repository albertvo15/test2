import re

line = ' [this	 is a         line ] \n'

line = line.strip('\n')
line = line.strip('\t')

line = line.replace('\n','')
line = line.replace('\t','')

#line = line.replace('\w+','')
#line = line.strip('\w+')
line = line.strip()
print line
#line = line.replace(" ","")

line = re.sub(r"\s+", " ", line)
line = re.sub(r"\[", "", line)
line = re.sub(r"\]", "", line)
print line
