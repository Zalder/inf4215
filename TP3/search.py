# -*- coding: utf-8 -*-
#
# Implementation of A* algorithm
#
# Author: Michel Gagnon
# Date:  31/01/2014

import sys
import math
import subprocess
from itertools import *


class Search(object):
    """ This is an implementation of the A* search """
    def __init__(self, environment):
        self.environment = environment



    ####################
    # Public functions
    ####################

    def startSearch(self):
        """ This function does the search and returns a plan """
        self._createProblemFile()
        self.result = subprocess.Popen('./ff -o domain.pddl -f problem.pddl > result.txt',shell=True)
        self.result.wait()
        return self._extractPlan()


    ####################
    # Private functions
    ####################


    def _createProblemFile(self):
        self.problemFile = open('problem.pddl','w')
        self.problemFile.write("""
(define (problem prob1)
   (:domain store)
""")

        # Object list
        self.problemFile.write("   (:objects")
        for d in self.environment.graph.nodes:
            self.problemFile.write(" " + d)
        for p in self.environment.packages:
            self.problemFile.write(" " + p.id)
        for p in self.environment.agent.load:
            self.problemFile.write(" " + p.id)
        self.problemFile.write(")\n")

        self.problemFile.write("   (:init \n")
        
        # Cost initialization
        self.problemFile.write("   (= (cost agent) 0)\n")

        # Package list
        for  p in self.environment.packages:
            self.problemFile.write("      (package {})\n".format(p.id))
            self.problemFile.write("      (= (poids {}) {})\n".format(p.id, p.weight))
            self.problemFile.write("      (at {} {})\n".format(p.id, p.origin))
            self.problemFile.write("      (to {} {})\n\n".format(p.id, p.destination))
            
        # Loaded packages list
        for p in self.environment.agent.load:
            self.problemFile.write("      (package {})\n".format(p.id))
            self.problemFile.write("      (= (poids {}) {})\n".format(p.id, p.weight))
            self.problemFile.write("      (loadedOn {})\n".format(p.id))
            self.problemFile.write("      (to {} {})\n\n".format(p.id, p.destination))

        for d in self.environment.graph.nodes:
            self.problemFile.write("      (node {})\n".format(d))
        
        self.problemFile.write("\n      (= (maxLoad agent) {})\n".format(self.environment.agent.maxLoad))
        self.problemFile.write("      (= (loadWeight agent) {})\n".format(self.environment.agent.loadWeight))
        self.problemFile.write("      (pos agent {})\n\n".format(self.environment.agent.position))

        for (A, B, cost) in self.environment.graph.edges:
            self.problemFile.write("      (connected {} {})\n".format(A, B))
            self.problemFile.write("      (connected {} {})\n".format(B, A))
            self.problemFile.write("      (= (costNode {} {}) {})\n".format(B, A, cost))
            self.problemFile.write("      (= (costNode {} {}) {})\n\n".format(A, B, cost))
        
        self.problemFile.write("   )\n")
        self.problemFile.write("""
   (:goal (forall (?x) (imply (package ?x) (delivered ?x))))
   (:metric minimize (cost agent)))
""") 
        self.problemFile.flush()                             

    def _extractPlan(self):
        result = open('result.txt')
        lines = result.readlines()
        lines = [l for l in dropwhile(lambda s: not s.startswith('ff: found legal plan'),lines)]
        lines = lines[1:]
        lines = [l for l in takewhile(lambda s: not s.startswith('plan cost'),lines)]

        plan = []
        for line in [l.split() for l in lines]:
            plan.append((line[-3],line[-2]))

        plan.reverse()
        return plan                


