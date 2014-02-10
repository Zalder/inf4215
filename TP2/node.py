# -*- coding: utf-8 -*-
import sys
import math
import copy
from agent import *


class Node(object):
    def __init__(self, state, action = None, cost = 0, previous = None):
        self.state = state
        self.previous = previous
        self.g = cost
        self.h = self.estimateHeuristic()
        self.f = self.g + self.h
        self.action = action 

    ####################
    # Public methods
    ####################

    def expand(self):
        nextStates = []
        # À Implémenter
        # Doit retourner une liste d'état successeurs
        # Pour chaque état, on doit fixer la valeur f(n) = g(n) + h(n)
 
    def estimateHeuristic(self):
        # À Implémenter: Vous pouvez rajouter les paramètres 
        # nécessaire pour calculer l'heuristique.
               
                

    ####################
    # Private methods
    ####################

                                    
