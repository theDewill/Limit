import simpy as sp
from collections import deque
env = sp.Environment()
Monitorings = {'int':[],'ext':[]}
table = {'Time':[],'Customer':[],'Activity':[],'Interaction':[],'qCount':[]}

class InteractionPool():
    def __init__(self):

        #{'cashier':[- interactionInstances acording to count given -]}
        self.pool = {}
        self.entityPool = {}
    
    def addToPool(self,key,interactionClass,count): #TODO:
        self.pool.setdefault(key)
        self.pool[key] = []
        for I in range(count):
            self.pool[key].append(interactionClass(I))

    def createAgentPool(self,agentType,agentClass,count):
        self.entityPool.setdefault(agentType)
        self.entityPool[agentType] = []
        for agent in range(count):
            self.entityPool[agentType].append(agentClass(agent))

    
    def requestInteraction(self,user,key):
        CQueue.addToQueue(user,key) #agent is added to the repective interactions queue
        
        for interaction in  self.pool[key]:
            if interaction.state == 0:
                interaction.state = 1
                CQueue.DeQueue(key)
                return interaction
            #this logic is for first initializaton upto pool max out giving interactions to users
        

class CrowdQueue():
    def __init__(self):
        self.cQueue = {}

    def addQueue(self,key): #TODO:
        self.cQueue.setdefault(key)
        self.cQueue[key] = []
    
    def DeQueue(self,key):
        return self.cQueue[key].pop(0)
    
    def addToQueue(self,user,key):
        self.cQueue[key].append(user)
        

    

#Global Queue for each interaction
CQueue = CrowdQueue()
#pool of interaction model objects
IPool = InteractionPool()  
