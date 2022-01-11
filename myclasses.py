class Person:
    def __init__(self,n,a):
        self.name = n
        self.age = a
        self.healthLevel = 100.0

        def getAge(self):	
            return self.age

        def increaseAge(self):
            self.age = self.age + 1

        def healFull(self):   
            self.health = 100.0

        def takeInjury(self, damage):
          self.healthLevel = self.healthLevel - damage