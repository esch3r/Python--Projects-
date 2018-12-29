# self is a temporary placeholder for the object
class className:
    def createName(self,name):
          self.name = name

    def displayName(self):
          return self.name
    def saying(self):
           print ( "hello" % self.name)
         

first =className()
second =className()

first.createName('Tony')
second.createName('bucky')


first.displayName()
second.displayName()
