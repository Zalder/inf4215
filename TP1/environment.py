from graph import *

class Environment:
    def __init__(self, graph, agent):
        self.graph = graph
        self.agent = agent
 
        # Initially, desks do not contain any package
        self.desks = {}
        for d in graph.specialNodes:
            self.desks[d] = []

        self.actionCounter = 0

    def addPackage(self, deskName, package):
        "Add a package at one desk"
        self.desks[deskName].append(package)

    def removePackage(self, deskName, package):
        self.desks[deskName].remove(package)

    def getDeskState(self, deskName):
        "Return the list of packages found at one desk"
        return self.desks[deskName]

    def getEnvironmnentState(self):
        "Return the collection of packages for all desks in the office"
        return dict([(desk, self.getDeskState(desk)) for desk in self.desks])

    def allDelivered(self):
        "Return True if all packages have been delivered"
        for deskName, packageList in self.desks.items():
            for package in packageList:
                if deskName != package.destination:
                    return False

        if len(self.agent.load) > 0:
            return False

        return True

    def percept(self, agent):
        "Return the list of package at current agent position"
        return self.desks[agent.position]

    def executeAction(self, agent, action, arg):
        "Agent executes the action. World state is changed to reflect this action."
        if action == 'move':
            agent.move(arg)
        elif action == 'drop':
            agent.drop(lambda p: p.id == arg.id)
            self.addPackage(agent.position, arg)
        elif action == 'take':
            agent.take(arg)
            self.removePackage(agent.position, arg)
        else:
            raise RuntimeError

    def step(self):
        "Run the environment for one time step. "
        if not self.allDelivered():
            (action, arg) = self.agent.chooseAction(self.getDeskState(self.agent.position))
            self.actionCounter += 1
            self._showAction(action, arg)
            self.executeAction(self.agent, action, arg)
            self.agent.updateModel(action, self.percept(self.agent))

    def run(self, steps=1000):
        "Run the Environment for given number of time steps."
        while steps > 0:
            if self.allDelivered(): return
            self.step()
            steps -= 1

    def _showAction(self,action,arg):
        print self.actionCounter, ':',
 
        if action in ['take','drop']:
            print action, arg.id
        else:
            print action, arg
        
