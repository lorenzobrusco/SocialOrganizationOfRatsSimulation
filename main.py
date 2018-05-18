import numpy
from random import randint
import random
import matplotlib.pyplot as plt



TOTAL_STEP = 1000
FOOD_PROBABILITY= 0.8
HUNGER_THRESHOLD = 10

FOOD_SIZE = 1.0

NUMBER_OF_SIMULATIONS = 100


class Rat:

    def __init__(self, _hitProbability):
        self.hunger = 1.0
        self.learn = 0
        self.unlearn = 0
        self.hitProbability = _hitProbability
        self.search = False
        self.trials = 0

    def __str__(self):
        s="hunger = "+str(self.hunger)
        s+= " learn = "+str(self.learn)
        s+=" unlearn = "+str(self.unlearn)
        s+= " search = "+str(self.search)
        return s

    def simulation(self):

        for STEP in range(TOTAL_STEP):
            if not self.search and rat.hunger > HUNGER_THRESHOLD:
                rat.search = True
                self.hitProbability = 0.7


            n = random.uniform(0.1,1.0)
            if self.search and n<= self.hitProbability :
                n = random.uniform(0.1,1.0)

                self.trials += 1

                if n <= FOOD_PROBABILITY:
                    self.hunger -= FOOD_SIZE
                    self.learn += 1
                    self.unlearn -= 1
                else:
                    self.learn -= 1
                    self.unlearn += 1


            else:
                self.hunger += FOOD_SIZE

            if self.search and self.hunger == 0:
                self.search = False

        return self.trials
             



myList =[]

for id in range(NUMBER_OF_SIMULATIONS):
    rat = Rat(0.3)
    rat.simulation()
    myList.append(rat.simulation())
    



 

print(myList)

plt.plot(range(NUMBER_OF_SIMULATIONS), myList )

plt.show()
