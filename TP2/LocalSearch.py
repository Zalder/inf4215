# -*- coding: utf-8 -*-
#
# Implementation of A* algorithm
#
# Author: Michel Gagnon
# Date:  31/01/2014

from node import *
from operator import attrgetter
import sys
import random


# Implementation de l'algorithme d'exploration par escalade

class LocalSearch(object):
    """ This is an implementation of the A* search """
    def __init__(self, initState, successTest):
        self.initNode = Node(initState)
        self.successTest = successTest

    ####################
    # Public functions
    ####################

    def startSearch(self):
        """ This function does the search and returns a plan """
        current = self.initNode
        bestScore = float("inf")
        for i in range(0,100):
            current = self.initNode
            while True:
                neighbors = current.expand()
                if not neighbors:
                    break
                current = min(neighbors, key=attrgetter("h"))
                
                # Random minimum
                listOfMins =  [x for x in neighbors if current.h == x.h]
                index = random.randint(0, len(listOfMins)-1)
                current = listOfMins[index]
                
                if self.successTest(current.state):
                    if current.g < bestScore:
                        bestScore = current.g
                        bestOne = current
                        break
        return self._extractPlan(bestOne)
    
    
    def _extractPlan(self,node):
        currentNode = node
        plan = [currentNode.action]
        while currentNode.previous != None:
            currentNode = currentNode.previous
            plan.append(currentNode.action)
        
        plan.pop()
        return plan


