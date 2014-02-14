# -*- coding: utf-8 -*-
#
# Implementation of A* algorithm
#
# Author: Michel Gagnon
# Date:  31/01/2014

from node import *
from operator import attrgetter
import sys
import math


# Implementation de l'algorithme d'exploration par escalade

class AgentLocalSearch(object):
    """ This is an implementation of the A* search """
    def __init__(self, initState, successTest):
        self.initNode = Node(initState)
        self.successTest = successTest

    ####################
    # Public functions
    ####################

    def startSearch(self):
        """ This function does the search and returns a plan """
        current = self.initNode;
        while True:
            neighbors = current.expand()
            if not neighbors:
                break
            current = min(neighbors, key=attrgetter("h"))
            print current.h
            print current.action
            if self.successTest(current.state):
                return self._extractPlan(current)
    
    
    def _extractPlan(self,node):
        currentNode = node
        plan = [currentNode.action]
        while currentNode.previous != None:
            currentNode = currentNode.previous
            plan.append(currentNode.action)
        
        plan.pop()
        return plan


