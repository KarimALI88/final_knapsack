import random
from random import randint
import math
import matplotlib.pyplot as plt
import numpy as np

newlist=[]

class UnboundedKnap_GA():
   
    def __init__(self):
        self.knapsack_weight= 0
        self.optimal_value = 0
        self.count = 0
        self.items =[()]

    def individual(self, lenght):
        return [randint(0, 5) for x in range(lenght)]

    def population(self ,count):
        return [self.individual(len(self.items)) for x in range(count)]

    def fitness(self,individual, items):
        total_weight = total_value = 0
        for x in range(len(individual)):
           if individual[x] == 0:
              pass
           else:
              total_weight =(total_weight + items[x][0]*individual[x])
              total_value =(total_value+ items[x][1]*individual[x])
        if total_weight > self.knapsack_weight:
             total_value = 0
        return total_value

    def evolve(self ,pop, retain=0.2, random_select=0.05,mutate=0.01):

       graded = [(self.fitness(x, self.items), x) for x in pop]
       graded = [x[1] for x in sorted(graded, reverse=True)]
       retain_length = math.ceil(int(len(graded) * retain))
       parents = graded[:retain_length]

       for individual in graded[retain_length:]:
          if random_select > random.random():
             parents.append(individual)

       for individual in parents:
            if mutate > random.random():
              index_to_mutate = randint(0, len(individual) - 1)
              individual[index_to_mutate] == randint(0,5)

       parents_len = len(parents)
       remind_len = len(pop) - parents_len
       children = []
       while len(children) < remind_len:
        male = randint(0, len(parents) - 1)
        female = randint(0, len(parents) - 1)
        if male != female:
            male = parents[male]
            female = parents[female]
            half = round(len(male) / 2)
            child = male[:half] + female[half:]
            children.append(child)

       parents.extend(children)
       return parents

    def run ( self,items ,knapsack_weight , count):
       self.items = items
       self.knapsack_weight = knapsack_weight
       self.count = count

       pop = self.population(count)
       for x in range(1000):
         pop=self.evolve(pop)

       print("the optimal solution after 1000 iteration is ",self.fitness(pop[0],items))
       newlist.append(self.fitness(pop[0], items))
       ypoints = np.array(newlist)
       # naming the x axis
       plt.xlabel('solution')
       # naming the y axis
       plt.ylabel('values')
       plt.plot(ypoints, marker='o', ms=20, mec='r', mfc='r')
       plt.show()
       return pop[0]