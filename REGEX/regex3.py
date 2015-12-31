
import re

pattern = re.compile(r'\bfoo\b')
res = pattern.match("foo bar")

print res
