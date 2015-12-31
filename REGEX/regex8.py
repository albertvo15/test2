import re
#line = '172.16.0.3 - - [25/Sep/2002:14:04:19 +0200] "GET / HTTP/1.1" 401 - "" "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.1) Gecko/20020827"'

line = 'ip153.b2.wsnet.com - - [01/Jul/1995:09:59:20 -0400] "GET /history/apollo/apollo.html HTTP/1.0" 200 3258'
#line = '10.10.10.10 - - [01/Jul/1995:09:59:20 -0400] "GET /history/apollo/apollo.html HTTP/1.0" 200 3258'

#line = '127.0.0.1 - stefan [01/Apr/2002:12:17:21 +0200] "GET /sit3-shine.7.gif HTTP/1.1" 200 15811 "localhost/"; "Mozilla/5.0(compatible; Konqueror/2.2.2-2; Linux)"'
#regex = '([(\d\.)]+) - (.*) \[(.*?)\] "(.*?)" (\d+) - "(.*?)" "(.*?)"'
#regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) - "(.*?)" "(.*?)"'
#regex = '(\w+).(\w+).(\w+).(\w+) - - \[(.*?)\] "(.*?)" (\d+) (\d+)'
regex = '(\w+).(\w+).(\w+).(\w+) - - \[(.*?)\] "(.*?)" (\d+) (\d+)'

match =  re.findall(regex, line)
#print match.groups()
host =  match
print 'host ' , host
#date =  match.group(4)
#print 'date ' + date
