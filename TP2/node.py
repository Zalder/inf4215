# -*- coding: utf-8 -*-
from __future__ import division
import sys
import math
from agent import *

# debug imports
import logging
from time import *

counter = 0;


class Node(object):
    def __init__(self, state, action = None, cost = 0, previous = None):
        self.state = state
        self.previous = previous
        self.g = cost
        self.h = self.estimateHeuristic()
        self.f = self.g + self.h
        self.action = action 
        
        #if action != None:
            #logging.info("Creating node : %s with score %s and %s from goal", getActionString(self.action), self.f, self.h)

    ####################
    # Public methods
    ####################

    def expand(self):
        nextStates = []
        # À Implémenter
        # Doit retourner une liste d'état successeurs
        # Pour chaque état, on doit fixer la valeur f(n) = g(n) + h(n)
        #global counter 
        #counter += 1
        #print counter
        
        # Liste des destination des paquets chargés
        destinations = [x.destination for x in self.state.agent.load]
        
        # Premierement traiter chaque paquet chargé
        
        # Si la charge est complète il faut absolument dropper un paquet (sinon gaspillage)
        loadedPackageDests = []
        
        # Ajouter tous les endroits ou un drop est possible
        for (keys, values) in self.state.getEnvironmentState().items():
            for package in values:
                if package.weight + self.state.agent.loadWeight <= self.state.agent.maxLoad:
                    loadedPackageDests.append(keys)
                    break; 
                
        # Ajouter ensuite tous les endroits ou un take est possible
        # Les nodes ou l'on ne peut faire avancer le problème ne sont pas considérées
        for destination in destinations:
            if destination not in loadedPackageDests:
                loadedPackageDests.append(destination)
            
        ## CODE POUR LOCAL SEARCH A MODIFIER
       # if self.state.agent.position in loadedPackageDests:
            #loadedPackageDests.remove(self.state.agent.position)
        
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
        costMD = 0
         
        totalWeight = 0
         
        # On ajoute les destinations des paquets non-livrés a une liste
        # pour les paquets déja chargés
            
         
        nodeWeights = {}
        minimalMoves = 0
         
        # Ensuite on ajoute à l'heuristique le poids de tous les
        # paquets non-livrés de chaque node
        for (keys, values) in self.state.getEnvironmentState().items():
            for package in values:
                costTake += package.weight
                costMD += package.weight * self.state.graph.shortestPathLength(keys, package.destination)
                totalWeight += package.weight
                
                # Calcul du nombre minimum de mouvements
                # en utilisant le nombre minimal de mouvement entre chaque node
                if (keys, package.destination) in nodeWeights:
                    nodeWeights[(keys, package.destination)] += package.weight
                else:
                    nodeWeights[(keys, package.destination)] = package.weight
        
        for package in self.state.agent.getLoad():
            costMD += package.weight * self.state.graph.shortestPathLength(self.state.agent.position, package.destination) 
            if (self.state.agent.position, package.destination) in nodeWeights:
                nodeWeights[(self.state.agent.position, package.destination)] += package.weight
            else:
                nodeWeights[(self.state.agent.position, package.destination)] = package.weight
        
        for link in nodeWeights:
            curDiv = math.ceil(nodeWeights[link]/self.state.agent.maxLoad)
            minimalMoves += self.state.graph.shortestPathLength(link[0], link[1]) * self.state.agent.weight * curDiv
                 
         
        # Calcul du nombre minimal estimé de déplacement
        # On présume que le nombre de minimal de déplacement se fait si tous les 
        # déplacements sont avec une charge maximale
        minMoves = math.ceil(totalWeight/self.state.agent.maxLoad)
         
        # Calcul de l'heuristique finale
        heuristique = (costTake + ((minimalMoves + costMD))) * self.state.agent.k
        
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
