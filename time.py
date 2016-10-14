#!/usr/bin env python3

class Time:
    def __init__(self):
        self.currentTime = 0
    
    def up(self):
        self.currentTime += 1
        
    def down(self):
        if self.currentTime > 0:
            self.currentTime -= 1
