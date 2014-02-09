from agent import *
from random import randint
from package import *
from copy import deepcopy

class ModelBasedAgent(Agent):
    
    def __init__(self, graph, pos, weight = 10, maxLoad = 5, k = 1):
            Agent.__init__(self, graph, pos, weight, maxLoad, k)
            self.visited = []
            self.unvisited = deepcopy(graph.specialNodes)
            self.scoreAndPackageList = {}
            
    def chooseAction(self, packageList):
        
        #----------------------------------------------------
        # Drop package if at the right position
        #----------------------------------------------------
        
        for loadedPackage in self.load:
            if loadedPackage.destination == self.position:
                return ('drop', loadedPackage)
        
        #----------------------------------------------------
        # Evaluate if a package should be loaded and which one
        #----------------------------------------------------
        
        if self.loadWeight < self.maxLoad:
            bestPackage = self.calculateScores(packageList)
        
            if bestPackage != 0:
                return ('take', bestPackage[0])
        #----------------------------------------------------
        # Evaluate which node to move towards when needed
        #----------------------------------------------------
        
        curBestScore = 0
        curBestNode = "fail"
        curScore = 0
        
        nbOfPackagesArr = {}
        totalWeight = {}
        totalWeight [curBestNode] = 0
        
        loadedDestOccurence =  {}
        
        for node in self.graph.specialNodes:
            loadedDestOccurence[node] = 0
            
        for loadedPackage in self.load:
            #loadedDestOccurence.setdefault(loadedPackage.destination, 0)
            loadedDestOccurence[loadedPackage.destination] += 1
        
        
        for node in self.visited:
            if node == self.position:
                continue
            curScore = self.sumOfScores(self.scoreAndPackageList[node])
            nbOfPackagesArr[node] = len(filter(lambda x:x[1][0] == node, self.scoreAndPackageList[node]))
            filteredNodes = filter(lambda x:x[1][0] != node, self.scoreAndPackageList[node])
            totalWeight[node] = sum(map(lambda x:x[2], filteredNodes))
            
            if curScore > curBestScore:
                curBestScore = curScore
                curBestNode = node
        
        if (totalWeight[curBestNode] < self.maxLoad or nbOfPackagesArr[max(nbOfPackagesArr, key=nbOfPackagesArr.get)] == 0 or len(self.visited) == 0) and len(self.unvisited) > 0:
            rand = randint(0, len(self.unvisited)-1)
            destination = self.unvisited[rand]
        else:
            destination = curBestNode
            
        if destination == 'fail':
            destination = max(totalWeight, key=totalWeight.get)
            
        if curBestScore == 0 and len(self.load) != 0:
            destination = max(loadedDestOccurence, key=loadedDestOccurence.get)
            
            
        return ('move', destination)
            
        
            
    def updateModel(self, action, packageList):
        self.calculateScores(packageList)
        curPackList =  []
    
        if self.visited.count(self.position) == 0 and action == 'move':
            self.visited.append(self.position)
            self.unvisited.remove(self.position)
            self.calculateScores(packageList)
                
        for node in self.visited:
            curPackList =  []
            for score in self.scoreAndPackageList[node]:
                curPackList.append(Package(score[1][0], score[2], score[0]))
            self.calculateScores(curPackList)
        return
            
    
    def sumOfScores(self, scoreArray):
        # The contribution of the current position to the other node's score must be ignored
        # to avoid an exponential growth of the scores
        total = 0
        for score in scoreArray:
            if score[1][0] != self.position:
                total += score[1][1]
        return total
    
    # Update scores and returns the best package to take
    def calculateScores(self, packageList):
        # First count for each desk how many packages are meant to go there
        
        deskDestOccurence = {}
        loadedDestOccurence = {}
        
        for node in self.graph.specialNodes:
            deskDestOccurence[node] = 0
            loadedDestOccurence[node] = 0
               
        for package in packageList:
            if package.destination != self.position:
                #deskDestOccurence.setdefault(package.destination, 0)
                deskDestOccurence[package.destination] += 1
                
        # Now count how many of each are already loaded
        for loadedPackage in self.load:
            #loadedDestOccurence.setdefault(loadedPackage.destination, 0)
            loadedDestOccurence[loadedPackage.destination] += 1
            
        # Calculate a score for each package
        
        scoreList = []
        bestPackage = 0
        bestScore = 0
    
        # The score is calculated according to package weight, the number of
        # packages of same destination loaded and on the desk as well as the score of the node destination (if known)
        for package in packageList:
            if package.destination != self.position and package.weight + self.loadWeight <= self.maxLoad:
                curScore = loadedDestOccurence[package.destination] + deskDestOccurence[package.destination] + (float(1) / package.weight)
                if self.visited.count(package.destination) > 0:
                    destScore = self.sumOfScores(self.scoreAndPackageList[package.destination])
                    curScore += destScore
                
                curPackage = (package.id, (package.destination, curScore), package.weight)
                if curScore > bestScore and package.weight + self.loadWeight <= self.maxLoad:
                    bestPackage = (package, curScore)
                    bestScore = curScore
            else:
                curPackage = (package.id, (package.destination, 0), package.weight)
            scoreList.append(curPackage)
                
        self.scoreAndPackageList[self.position] = scoreList
        
        return bestPackage
                

