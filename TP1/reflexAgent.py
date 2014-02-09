from agent import *
from random import randint

class ReflexAgent(Agent):

    def __init__(self, graph, pos, weight = 10, maxLoad = 5, k = 1):
        Agent.__init__(self, graph, pos, weight, maxLoad, k)

    def chooseAction(self, packageList):
        # ------------------------------------------
        # DROP package if we have to
        # ------------------------------------------

        # Check if we have to drop a packet
        if len(self.load) > 0:
            package = self.load[0]
            i = 1

            while package.destination != self.position and i < len(self.load):
                package = self.load[i]
                i += 1

            # One package to drop
            if i <= len(self.load) and package.destination == self.position:
                return ('drop', package)

        # ------------------------------------------
        # MOVE we have no package to load so find another destination
        # ------------------------------------------
        if len(packageList) == 0:
            posIndex = self.getNextPos()
            return ('move', self.graph.specialNodes[posIndex])

        # ------------------------------------------
        # TAKE maybe there is some package to load
        # ------------------------------------------

        # Retrieve package which is not at this destination
        #package = packageList[0]
        #i = 1

        #while package.destination == self.position and i < len(packageList):
        #  package = packageList[i]
            #i += 1
                
        i = -1;
        for curPackage in packageList:
            if curPackage.destination != self.position and (curPackage.weight + self.loadWeight) <= self.maxLoad:
                i = 1;
                package = curPackage
                if self.IsSameDestInLoad(package):
                    break
                

        if i != -1:
                return ('take', package)
        else:
            posIndex = self.getNextPos()
            return ('move', self.graph.specialNodes[posIndex])



    def updateModel(self, action, packageList):
        pass
    
    def getNextPos(self):
        #posIndex = self.graph.specialNodes.index(self.position) + 1
        posIndex = randint(0, len(self.graph.specialNodes)-1)
        if len(self.graph.specialNodes) <= posIndex: 
            posIndex = 0
        if len(self.load) > 0:
            posIndex = self.graph.specialNodes.index(self.load[0].destination)
        return posIndex
    
# Checks if there is there is a package already loaded that has the same destination as the one
# passed in argument
    def IsSameDestInLoad(self, package):
        for selfPackage in self.load:
            if package.destination == selfPackage.destination:
                return True
        return False