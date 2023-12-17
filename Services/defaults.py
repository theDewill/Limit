import simpy as sp
from services import ResultMonitor
from context import env,IPool,CQueue

class masterResource:
    def __init__(self,rid):
        self.env = env
        self._root = None
        self._store = "" #TODO: here apply the container or any simpy container part
        self.monitorData = ResultMonitor(rid,'int')
    

    def AllocateResource(self,capacity=1):
        
        self._root = sp.Resource(self.env,capacity)


    def RequestResource(self): #process in interaction object must go through this first reserving a resource
        
        with self._resource.request() as res:
            yield res
        
class masterEntity():
    def __init__(self,cid,Aname):
        self.id = cid
        self.Events = {'process':{},'control':[]}
        self.interactionObject = None
        self.state = 0
        self.workflow = None
        self.monitorData = ResultMonitor(cid, Aname,'ext')
        self.env = env

    #this must be a generator
    def go(self):
        for interaction in self.workflow:
            #yield self.env.process(interaction._initate(self))
            #TODO: interaction object is not recieving
            self.interactionObject = IPool.requestInteraction(self,interaction) #key is passed

            startTime = self.env.now
            if self.interactionObject is not None:
                endTime = self.env.now
                self.interactionObject._initiate(self)
            else:
                yield self.Events['process'][interaction] #TODO: must configure EVENTS # this is the event
                print(f"Agent {self.id} got the {interaction} object : {self.interactionObject}")
                endTime = self.env.now
                if self.interactionObject is None:
                    print(f"Error: interaction object is not recieved for agent {self.id} for {interaction} ")
                self.interactionObject._initiate(self)

            #recording delays of the agent in each interaction queue
            self.monitorData._data['delays'].setdefault(self.interactionObject.name)
            self.monitorData._data['delays'][self.interactionObject.name] = endTime-startTime

            #total accumulated custom delay in interaction clock will added
                
            yield self.env.timeout(self.interactionObject.clock)
            self.interactionObject.release(interaction)
            # #interaction change delay
            

        #next agent enter delay
        #yield self.env.timeout(3)

        
    #this can be used to manipulate the entity behaviour on runtime conditions
    def Control(self):
        pass


class masterModel():

    def __init__(self,Iid,Iname):
        self.id = Iid
        self.env = env
        self.state = 0 #
        self._user  = None
        self.clock = 0
        self.monitorData = ResultMonitor(Iid,Iname,'int')

    def delayClock(self,time):
        self.clock+=time

    def release(self,key):
        #self.state = 0
        self.clock = 0
        if len(CQueue.cQueue[key]) == 0:
            self.state = 0
            
        else:
            
            self._user = CQueue.cQueue[key].pop(0)
            self._user.interactionObject = self
            print(f"interaction object {key} is released for {self._user} with id - {self._user.id}")
            self._user.Events['process'][key].succeed() #simply triggering TODO: have to configure EVENTS in a AGENt
            print(f"{key} process event {self._user.Events['process']} for Agent {self._user.id} is triggered")



        