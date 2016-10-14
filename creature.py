#!/usr/bin/env python3

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