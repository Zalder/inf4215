# -*- coding: utf-8 -*-
#
# Implementation of an environment
#
# Author: Michel Gagnon
# Date:  31/01/2014

from graph import *
import copy
import operator

class Environment:
    def __init__(self, graph, agent):
        self.graph = graph
        self.agent = agent
 
        # Initially, desks do not contain any package
        self.desks = {}
        for d in graph.specialNodes:
            self.desks[d] = set()

        self.actionCounter = 0

    def addPackage(self, deskName, package):
        "Add a package at one desk"
        self.desks[deskName].add(package)

    def removePackage(self, deskName, package):
        self.desks[deskName] = set(filter(lambda p: p.id != package.id, self.desks[deskName]))

    def getDeskState(self, deskName):
        "Return the list of packages found at one desk"
        return [p for p in self.desks[deskName]]

    def getEnvironmentState(self):
        "Return the collection of packages for all desks in the office"
        return dict([(desk, self.getDeskState(desk)) for desk in self.desks])

    def allDelivered(self):
        "Return True if all packages have been delivered"
        for d in self.desks:
            if len(self.desks[d]) > 0: return False
        return self.agent.empty()

    def percept(self):
        return self.copy()

    def executeAction(self, (action,arg)):
        "Agent executes the action. World state is changed to reflect this action."
        if action == 'take':
            self.removePackage(self.agent.position, arg)
            self.agent.take(arg)
        elif action == 'moveAndDrop':
            self.agent.moveAndDrop(arg)

    def step(self):
        "Run the environment for one time step. "
        if not self.allDelivered():
            action = self.agent.chooseAction(self.percept())
            self.actionCounter += 1
            self._showAction(action)
            self.executeAction(action)
            self.agent.updateModel(action, self.percept())

    def run(self, steps=1000):
        "Run the Environment for given number of time steps."
        while steps > 0:
            if self.allDelivered(): 
                print 'WASTED ENERGY:', self.agent.wastedEnergy
                return
            self.step()
            steps -= 1

    def copy(self):
        newEnvironment = Environment(self.graph, copy.deepcopy(self.agent))
        newEnvironment.desks = copy.deepcopy(self.desks)
        return newEnvironment

    def isEqual(self, other):
        return (self.agent.position == other.agent.position and 
                len(set([p.id for p in self.agent.load]).symmetric_difference(set([p.id for p in other.agent.load]))) == 0 and
                reduce(operator.and_,
                       [len(set([p.id for p in self.desks[d]]).symmetric_difference(set([p.id for p in other.desks[d]]))) == 0 for d in self.desks]))

    ####################
    # Private methods
    ####################

    def _showAction(self,(action,arg)):
        print self.actionCounter, ':',
        if action == 'take':
            print action, arg.id
        else:
            print action, arg


    def _getPackage(self,id):
        for l in self.desks.values():
            for p in l:
                if p.id == id:
                    return p
        
