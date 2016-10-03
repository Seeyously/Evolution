# population, creature, generation, species

#%%

class Creature:
    def __init__(self, numberFingers, numberGeneration):
        self.numberFingers = numberFingers
        self.numberGeneration = numberGeneration
        

#%%

if __name__ == "__main__":
    paul = Creature(5)
    maggy = Creature(4)
    paggy = Creature(min(paul.numberFingers, maggy.numberFingers))
    print(paggy.numberFingers)
    

