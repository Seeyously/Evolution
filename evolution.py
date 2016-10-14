
import sys
sys.path.append('/Users/Sophia/Coding/Evolution')

from creature import *
from generation import *
from time import *
from world import *


c1 = Creature(5,1)
c2 = Creature(4,1)
print(c2.numberFingers)
#c2_12 = Creature(min(c1.numberFingers, c2.numberFingers))
#print(c2_12.numberFingers)
    
#%%


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