# -*- coding: utf-8 -*-
#
# Implementation of A* algorithm
#
# Author: Michel Gagnon
# Date:  31/01/2014

from node import *
import sys
import math

# Basic logging 
import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)


class Search(object):
    """ This is an implementation of the A* search """
    def __init__(self, initState, successTest):
        self.initNode = Node(initState)
        self.successTest = successTest
        self.visitedNodes = []
        self.openNodes = []


    ####################
    # Public functions
    ####################

    def startSearch(self):
        """ This function does the search and returns a plan """
        self.openNodes.append(self.initNode)
        while self.openNodes:
            currentNode = self.openNodes.pop()
            if filter(lambda n: n.state.isEqual(currentNode.state), self.visitedNodes):
                continue
            else:
                self.visitedNodes.append(currentNode)
#                 if currentNode.action == None:
#                     logging.info('START')
#                 else:
#                     logging.info('Expanding node : %s, %s, %s', getActionString(currentNode.action), currentNode.f, currentNode.h)
#                     print 'Expanding node : ', currentNode.f, currentNode.h
                    
                if self.successTest(currentNode.state):
                    return self._extractPlan(currentNode)
                else:
                    # Expand current node and sort the open node list
                    self.openNodes += currentNode.expand()
                    self.openNodes.sort(cmp = lambda n1,n2: -1 if n1.f < n2.f else (1 if n1.f > n2.f else 0), 
                                        reverse = True)
        return None

    ####################
    # Private functions
    ####################


    def _extractPlan(self,node):
        currentNode = node
        plan = [currentNode.action]
        while currentNode.previous != None:
            currentNode = currentNode.previous
            plan.append(currentNode.action)

        plan.pop()
        return plan


