# population, creature, generation, species

#%%

class Time:
    def __init__(self):
        self.currentTime = 0
    
    def up(self):
        self.currentTime += 1
        
    def down(self):
        if self.currentTime > 0:
            self.currentTime -= 1

class Creature:
    
    def __init__(self, numberFingers, generation):
        self.numberFingers = numberFingers
        self.generation = generation
        self.age = 0
        self.size = 1
    
    def changeAge(self, deltaAge):
        self.age += deltaAge
        
    def rise(self, deltaSize):
        self.size += deltaSize

#numberGenerations = 0        
class Generation:
    #numberGenerations = 0
    
    def __init__(self):
        global numberGenerations
        self.number = numberGenerations
        #print(self.number)
        numberGenerations += 1
        self.creatures = []
    
    def addCreature(self, creature):
        self.creatures.append(creature)

#%%

if __name__ == "__main__":
    c1 = Creature(5)
    c2 = Creature(4)
    c2_12 = Creature(min(c1.numberFingers, c2.numberFingers))
    print(c2_12.numberFingers)
    
#%%

if __name__ == "__main__":
    #creatures = []
    numberGenerations = 0    
    generations = []
    generations.append(Generation())
    generations[numberGenerations-1].creatures.append(Creature(5, numberGenerations-1))
    generations[numberGenerations-1].creatures.append(Creature(6, numberGenerations-1))
    generations[numberGenerations-1].creatures.append(Creature(3, numberGenerations-1))

#%%
    for creature in generations[0].creatures:    
        print (creature.numberFingers)