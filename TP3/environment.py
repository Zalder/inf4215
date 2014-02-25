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
        self.packages = []
 
        # Initially, desks do not contain any package
        self.desks = {}
        for d in graph.specialNodes:
            self.desks[d] = set()

        self.packageSchedule = {}
        self.actionCounter = 0

    def addPackage(self, package, step):
        "Add a package at one desk"
        if step in self.packageSchedule:
            self.packageSchedule[step].append((package.origin,package))
        else:
            self.packageSchedule[step] = [(package.origin,package)]

    def removePackage(self, deskName, package):
        self.desks[deskName] = set(filter(lambda p: p.id != package.id, self.desks[deskName]))
        self.packages.remove(package)

    def findPackage(self, position, packageId):
        for p in self.getDeskState(position):
            if p.id == packageId:
                return p
        return None

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
        if action == 'wait':
            pass
        if action == 'drop':
            self.agent.drop(arg)
        if action == 'take':
            package = self.findPackage(self.agent.position, arg)
            self.removePackage(self.agent.position, package)
            self.agent.take(package)
        elif action == 'move':
            self.agent.move(arg)

    def step(self):
        "Run the environment for one time step. "
        if self.actionCounter in self.packageSchedule:
            for (desk,package) in self.packageSchedule[self.actionCounter]:
                self.packages.append(package)
                self.desks[desk].add(package)
        action = self.agent.chooseAction(self.percept())
        self.actionCounter += 1
        self._showAction(action)
        self.executeAction(action)
        self.agent.updateModel(action, self.percept())

    def run(self, steps=500):
        "Run the Environment for given number of time steps."

        if 0 in self.packageSchedule:
            for (desk,package) in self.packageSchedule[0]:
                self.desks[desk].add(package)

        while steps > 0:
            self.step()
            steps -= 1
        print 'DISTANCE:', self.agent.distance
        

    def copy(self):
        newEnvironment = Environment(self.graph, copy.deepcopy(self.agent))
        newEnvironment.desks = copy.deepcopy(self.desks)
        newEnvironment.packages = copy.deepcopy(self.packages)
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
            print action, arg
        elif action == 'wait':
            print action
        else:
            print action, arg


    def _getPackage(self,id):
        for l in self.desks.values():
            for p in l:
                if p.id == id:
                    return p
        
