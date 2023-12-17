#---agents Dictionery must be of entity objects with their identifiers as keys () - service ekt
agentList = {}
sampleSize = 50 # change this based on your sample
agentArrivalDelay = 3
from defaults import masterEntity
from services import CreateSample 


class Customer(masterEntity):
    def __init__(self,cid):
        self.name = 'customer'
        super().__init__(cid,self.name)
       

        
    #@self._process
    def leaveWorkflow ():
        pass



CreateSample(agentList,Customer,'customer',sampleSize) #writeable#
print(agentList['customer'])
print("sampleCreated!!")

