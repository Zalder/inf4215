# -*- coding: utf-8 -*-
from __future__ import division
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
        
        # Premierement traiter chaque paquet chargé
        
        loadedPackagesDests =  []
        for node in self.state.graph.specialNodes:
            loadedPackagesDests.append(node)
        
        for node in loadedPackagesDests:
            curState = self.state.copy()
            curState.executeAction(('moveAndDrop', node))
            curCost = self.state.agent.costMove(self.state.agent.position, node)
            curNode = Node(curState, ('moveAndDrop', node), curCost, self)
            nextStates.append(curNode)
            
        # Maintenant on traite les paquets contenus au bureau
        for package in self.state.getDeskState(self.state.agent.position):
            if package.weight + self.state.agent.loadWeight > self.state.agent.maxLoad:
                continue
            curState = self.state.copy()
            curAction = (('take'), package)
            curState.executeAction(curAction)
            curCost = self.state.agent.cost(curAction)
            curNode = Node(curState, curAction, curCost, self)
            nextStates.append(curNode)
            
        return nextStates
 
    def estimateHeuristic(self):
        # À Implémenter: Vous pouvez rajouter les paramètres 
        # nécessaire pour calculer l'heuristique.
        
        costTake = 0
        packageDestList =  []
        costMD = 0;
        
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
                if package.destination != keys:
                    costTake += package.weight
                    costMD += package.weight
                    if package.destination not in packageDestList:
                        packageDestList.append(package.destination)
                
               
        # On calcule le shortestPath entre la node actuelle et chaque node de destination
        
        maxDist = 0
        curDist = 0
        
        # Calcul du nombre minimal estimé de déplacement
        # On présume que le nombre de minimal de déplacement se fait si tous les 
        # déplacements sont avec une charge maximale
        minMoves = math.ceil(costMD/self.state.agent.maxLoad)
        
        for node in packageDestList:
            curDist = self.state.graph.shortestPathLength(self.state.agent.position, node)
            if curDist > maxDist:
                maxDist = curDist
        
        # Calcul de l'heuristique finale
        heuristique = (costTake + (maxDist*(minMoves*self.state.agent.weight + costMD))) * self.state.agent.k
        
        return heuristique

    ####################
    # Private methods
    ####################                                    
