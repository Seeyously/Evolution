#!/usr/bin env python3

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
