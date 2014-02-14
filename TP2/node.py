# -*- coding: utf-8 -*-
from __future__ import division
import sys
import math
import copy
from agent import *
from copy import deepcopy

import logging


class Node(object):
    def __init__(self, state, action = None, cost = 0, previous = None):
        self.state = state
        self.previous = previous
        self.g = cost
        self.h = self.estimateHeuristic()
        self.f = self.g + self.h
        self.action = action 
        
#         if action != None:
#             logging.info("Creating node : %s with score %s and %s from goal", getActionString(self.action), self.f, self.h)

    ####################
    # Public methods
    ####################

    def expand(self):
        nextStates = []
        # À Implémenter
        # Doit retourner une liste d'état successeurs
        # Pour chaque état, on doit fixer la valeur f(n) = g(n) + h(n)
        
        # Premierement traiter chaque paquet chargé
        
        # Si la charge est complète il faut absolument dropper un paquet (sinon gaspillage)
        loadedPackageDests = []
        if self.state.agent.loadWeight == self.state.agent.maxLoad:
            loadedPackagesDests =  []
            for package in self.state.agent.load:
                if package.destination not in loadedPackageDests:
                    loadedPackageDests.append(package.destination)
        else:
            loadedPackageDests = deepcopy(self.state.graph.specialNodes)
            
            ## CODE POUR LOCAL SEARCH A MODIFIER
            if self.state.agent.position in loadedPackageDests:
                loadedPackageDests.remove(self.state.agent.position)
        
        for node in loadedPackageDests:
            curState = self.state.copy()
            curState.executeAction(('moveAndDrop', node))
            curCost = self.state.agent.costMove(self.state.agent.position, node)
            curNode = Node(curState, ('moveAndDrop', node), curCost + self.g, self)
            nextStates.append(curNode)
            

                
            
        # Maintenant on traite les paquets contenus au bureau
        
        for package in self.state.getDeskState(self.state.agent.position):
            if package.weight + self.state.agent.loadWeight > self.state.agent.maxLoad:
                continue
            curState = self.state.copy()
            curAction = (('take'), package)
            curState.executeAction(curAction)
            curCost = self.state.agent.cost(curAction)
            curNode = Node(curState, curAction, curCost + self.g, self)
            nextStates.append(curNode)
            
        return nextStates
 
    def estimateHeuristic(self):
        # À Implémenter: Vous pouvez rajouter les paramètres 
        # nécessaire pour calculer l'heuristique.
        
        costTake = 0
        packageDestList =  []
        costMD = 0
        
        totalWeight = 0
        
        # On ajoute les destinations des paquets non-livrés a une liste
        # pour les paquets déja chargés
        for package in self.state.agent.getLoad():
            costMD += package.weight 
            if package.destination not in packageDestList:
                packageDestList.append(package.destination)
        
        
        # Ensuite on ajoute à l'heuristique le poids de tous les
        # paquets non-livrés de chaque node
        for (keys, values) in self.state.getEnvironmentState().items():
            for package in values:
                costTake += package.weight
                costMD += package.weight * self.state.graph.shortestPathLength(keys, package.destination)
                totalWeight += package.weight
                if package.destination not in packageDestList:
                    packageDestList.append(package.destination)
                
               
        # On calcule le shortestPath entre la node actuelle et chaque node de destination
        
#         maxDist = 0
#         curDist = 0
        
        # Calcul du nombre minimal estimé de déplacement
        # On présume que le nombre de minimal de déplacement se fait si tous les 
        # déplacements sont avec une charge maximale
        minMoves = math.ceil(totalWeight/self.state.agent.maxLoad)
        
#         for node in packageDestList:
#             curDist = self.state.graph.shortestPathLength(self.state.agent.position, node)
#             if curDist > maxDist:
#                 maxDist = curDist
        
        # Calcul de l'heuristique finale
        #print maxDist
        heuristique = (costTake + ((minMoves*self.state.agent.weight + costMD))) * self.state.agent.k
        
        return heuristique

    ####################
    # Private methods
    ####################          
    
    
    
# FOR LOGGING PURPOSES
def getActionString((action,arg)):
    if action == 'take':
        string = '(' + action + ',' + arg.id +  ')'
    else:
        string = '(' + action + ',' + arg +  ')'
    return string                          
