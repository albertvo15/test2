
class Animal():
  def play():
    print "Animal class play"
    return


class Pet(Animal):
  def __init__(self, name):
    self.name = name
  def play():
    print "Pet subclass play"
    pass



fluffy = Pet('Fluffy the cat')
