# -*- coding: utf-8 -*-
#
# Implementation of A* algorithm
#
# Author: Michel Gagnon
# Date:  31/01/2014

from node import *
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
        self.problemFile.write(")\n")

        self.problemFile.write("   (:init \n")

        # Package list
        for  p in self.environment.packages:
            self.problemFile.write("      (package {})\n".format(p.id))
        

        # Vous devez compléter ici...
        
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
            plan.append((line[-2],line[-1]))

        plan.reverse()
        return plan                


