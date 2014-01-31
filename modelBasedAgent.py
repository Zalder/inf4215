from agent import *
from random import randint

class ModelBasedAgent(Agent):
    
    def __init__(self, graph, pos, weight = 10, maxLoad = 5, k = 1):
            Agent.__init__(self, graph, pos, weight, maxLoad, k)
            self.visited = []
            self.unvisited = graph.specialNodes
            self.scoreAndPackageList = {}
            
    def chooseAction(self, packageList):
        
        #--------------------------------------
        # Drop package if at the right position
        #--------------------------------------
        
        for loadedPackage in self.load:
            if loadedPackage.destination == self.position:
                return ('drop', loadedPackage)
        
        #----------------------------------------------------
        # Evaluate if a package should be loaded and which one
        #----------------------------------------------------
        
        if self.loadWeight < self.maxLoad:
            bestPackage = self.calculateScores(packageList)
        
            if bestPackage != 0:
                return ('take', bestPackage)
        #----------------------------------------------------
        # Evaluate which node to move towards when needed
        #----------------------------------------------------
        
                
    
    def updateModel(self, action, packageList):
        self.calculateScores(packageList)
        return
    
    def sumOfScores(self, scoreArray):
        total = 0
        for key in scoreArray:
            total += scoreArray[key][1]
        return total
    
    # Update scores and returns the best package to take
    def calculateScores(self, packageList):
        # First count for each desk how many packages are meant to go there
        
        deskDestOccurence = []
        for package in packageList:
            if package.destination != self.position:
                deskDestOccurence[package.destination] += 1
                
        # Now count how many of each are already loaded
        
        loadedDestOccurence = []
        for loadedPackage in self.load:
            loadedDestOccurence[loadedPackage.destination] += 1
            
        # Calculate a score for each package
        
        scoreList = []
        bestPackage = 0
        bestScore = 0
    
        # The score is calculated according to package weight, the number of
        # packages of same destination loaded and on the desk as well as the score of the node destination (if known)
        for package in packageList:
            if package.destination != self.position:
                curScore = loadedDestOccurence[package.destination] + deskDestOccurence[package.destination] + (1 / package.weight)
                if self.visited.count(package.destination) > 0:
                    destScore = self.sumOfScores(self.scoreAndPackageList[package.destination])
                    curScore += destScore
                    curPackage = (package.id, (package.destination, curScore))
                if curScore > bestScore and package.weight + self.loadWeight < self.maxLoad:
                    bestPackage = (package, curScore)
                    bestScore = curScore
                scoreList.append(curPackage)
                
        self.scoreAndPackageList[self.position] = scoreList
        
        return bestPackage
                

