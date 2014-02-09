class Agent:
    def __init__(self, graph, pos, weight = 10, maxLoad = 5, k = 1):
        self.graph = graph
        self.position = pos
        self.weight = weight
        self.maxLoad = maxLoad
        self.load = []
        self.loadWeight = 0
        self.wastedEnergy = 0
        self.k = k

    def take(self, package):
        "Add one package to its load, if maximum weight is not reached"
        self.load.append(package)
        if self.loadWeight > self.maxLoad:
            raise RuntimeError
        else:
            self.loadWeight += package.weight

    def drop(self,condition):
        "Remove from load the packages that respect the condition"
        removedPackages =  self.find(condition)   
        self.load = filter(lambda x: not condition(x), self.load)  
        for p in removedPackages:
            self.loadWeight -= p.weight

    def getLoad(self):
        return self.load

    def find(self, condition):
        "Find the packages that respect the condition"
        return filter(condition,self.load)

    def move(self, newPosition):
        distance = self.graph.shortestPathLength(self.position, newPosition)
        self.position = newPosition
        self.wastedEnergy += self.k * distance * (self.loadWeight + self.weight)
 

    def chooseAction(self, packageList):
        abstract

    def updateModel(self, action, packageList):
        abstract




        
    
