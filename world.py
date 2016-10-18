#%%

class World():
    def __init__(self, width = 10, height = 10):
        self.width = width
        self.height = height
        self.world = [[0 for h in range(self.height)] for w in range(self.width)]

    def setPosition(self, x, y, value):
        try:
            #x in range(self.width)
            self.world[x][y] = value
        except:
            print("x should be between 0 and " + str(self.width-1))
            print("y should be between 0 and " + str(self.height-1))
        else:
            self.world[x][y] = value

    def show(self):
        print(self.world)
        
if __name__ == '__main__':
    myWorld = World()
    myWorld.setPosition(0,0,10)
    myWorld.show()
         
    