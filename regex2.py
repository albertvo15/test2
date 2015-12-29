import re

pattern = re.compile(r'\d{1,3}')
res = pattern.findall("The number is: 1234567890")

print res
