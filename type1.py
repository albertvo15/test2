
def myfunct(num1,num2):
  if not isinstance(num1, (int)):
    raise TypeError('num1 must be integer')
  if not isinstance(num2, (int)):
    raise TypeError('num2 must be integer')

  if num1 < num2:
    return "Less Than"
  if num1 > num2:
    return "Greater Than"
  if num1 == num2:
    return "Equal"


print myfunct(1,2)
print myfunct(3,2)
print myfunct(2,2)
print myfunct(1,2.0)
