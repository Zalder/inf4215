# -*- coding: utf-8 -*-
#
# Implementation of an agent
#
# Author: Michel Gagnon
# -*- coding: utf-8 -*-
#
# Implementation of A* algorithm
#
# Author: Michel Gagnon
# Date:  31/01/2014
from LocalSearch import *
import sys



class LocalSearchAgent:
    def __init__(self, graph, pos, weight = 10, maxLoad = 5, k = 1):
        self.graph = graph
        self.position = pos
        self.weight = weight
        self.maxLoad = maxLoad
        self.load = set()
        self.loadWeight = 0
        self.wastedEnergy = 0
        self.k = k
        self.plan = []

    def take(self, package):
        "Add one package to its load, if maximum weight is not reached"
        self.load.add(package)
        self.loadWeight += package.weight
        self.wastedEnergy += self.cost(('take',package))
        if self.loadWeight > self.maxLoad:
            raise RuntimeError

    def getLoad(self):
        return self.load

    def empty(self):
        return len(self.load) == 0

    def find(self, condition):
        "Find the packages that respect the condition"
        return filter(condition,self.load)

    def moveAndDrop(self, newPosition):
        "Move to the new position drop the packages whose destination is this position"
        self.wastedEnergy += self.cost(('moveAndDrop',newPosition))
        self.position = newPosition

        "Remove from load the packages that are at destination"
        removedPackages =  self.find(lambda x: x.destination == newPosition)   
        for p in removedPackages:
            self.load.remove(p)
            self.loadWeight -= p.weight

    def chooseAction(self, environment):
        if not self.plan:
            self.plan = LocalSearch(environment, lambda x:x.allDelivered()).startSearch()
        return self.plan.pop()    


    def updateModel(self,action,environment):
        pass

    def cost(self,(action,arg)):
        if action == 'moveAndDrop':
            return self.costMove(self.position,arg)
        elif action == 'take':
            return self.k * arg.weight
        else:
            return 0


    def costMove(self,source,dest):
        distance = self.graph.shortestPathLength(source,dest)
        return self.k * distance * (self.loadWeight + self.weight)

        
    
