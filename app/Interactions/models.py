import os,sys
from services import createWorkflow,editTime
from defaults import masterModel
from context import IPool,CQueue,table


#----Here we define different interactions between 1 - resource and [n] - agents

class CashierArrival(masterModel):
    def __init__(self,Iid):
        self.name = 'ArrivedAtCashier'
        super().__init__(Iid,self.name)
        #any custom attributes for a interaction model instance

    #This must be a generator
    def _initiate(self,user):

        #can use this for monitoring
        #create a report obect
         #self.monitorData.submitReport(report

        self._user = user
        
        #
        table['Time'].append(editTime(self.env.now + self.clock))
        table['Customer'].append( self._user)
        table['Activity'].append(f"ID - [{self._user.id}] met the cashier on interaction object - {self} ID - [{self.id}]")
        table['Interaction'].append(self.name)
        table['qCount'].append(len(CQueue.cQueue[self.name]))


        table['Time'].append(editTime(self.env.now + self.clock))
        table['Customer'].append( self._user)
        table['Activity'].append(f"ID - [{self._user.id}] cashier checks the appointment")
        table['Interaction'].append(self.name)
        table['qCount'].append(len(CQueue.cQueue[self.name]))

        
        self.delayClock(3)


        table['Time'].append(editTime(self.env.now + self.clock))
        table['Customer'].append(self._user)
        table['Activity'].append(f"ID - [{self._user.id}] agent is verified")
        table['Interaction'].append(self.name)
        table['qCount'].append(len(CQueue.cQueue[self.name]))


        
        table['Time'].append(editTime(self.env.now + self.clock))
        table['Customer'].append(self._user)
        table['Activity'].append(f"ID - [{self._user.id}] Issuing the ticket for {self._user}")
        table['Interaction'].append(self.name)
        table['qCount'].append(len(CQueue.cQueue[self.name]))


        table['Time'].append(editTime(self.env.now + self.clock))
        table['Customer'].append(self._user)
        table['Activity'].append(f"ID - [{self._user.id}] Done at Cashier")
        table['Interaction'].append(self.name)
        table['qCount'].append(len(CQueue.cQueue[self.name]))



class CheckRoom(masterModel):
    def __init__(self,Iid):
        self.name = 'CheckingRoom'
        super().__init__(Iid,self.name)
        #any custom attributes for a interaction model instance

    #This must be a generator
    def _initiate(self,user):

        #can use this for monitoring
        #create a report obect
         #self.monitorData.submitReport(report

        self._user = user
        
        #
        table['Time'].append(editTime(self.env.now + self.clock))
        table['Customer'].append( self._user)
        table['Activity'].append(f"ID - [{self._user.id}] met the room shower on interaction object - {self} ID - [{self.id}]")
        table['Interaction'].append(self.name)
        table['qCount'].append(len(CQueue.cQueue[self.name]))


        table['Time'].append(editTime(self.env.now + self.clock))
        table['Customer'].append( self._user)
        table['Activity'].append(f"ID - [{self._user.id}] start Moving to room")
        table['Interaction'].append(self.name)
        table['qCount'].append(len(CQueue.cQueue[self.name]))

        
        self.delayClock(8)


        table['Time'].append(editTime(self.env.now + self.clock))
        table['Customer'].append(self._user)
        table['Activity'].append(f"ID - [{self._user.id}] arrived at room")
        table['Interaction'].append(self.name)
        table['qCount'].append(len(CQueue.cQueue[self.name]))


        
        table['Time'].append(editTime(self.env.now + self.clock))
        table['Customer'].append(self._user)
        table['Activity'].append(f"ID - [{self._user.id}] attendee giving the room card to {self._user}")
        table['Interaction'].append(self.name)
        table['qCount'].append(len(CQueue.cQueue[self.name]))

        self.delayClock(2)

        table['Time'].append(editTime(self.env.now + self.clock))
        table['Customer'].append(self._user)
        table['Activity'].append(f"ID - [{self._user.id}] check in to room")
        table['Interaction'].append(self.name)
        table['qCount'].append(len(CQueue.cQueue[self.name]))





class PoolArrival(masterModel):
    def __init__(self,Iid):
        self.name = 'ArrivedAtPool'
        super().__init__(Iid,self.name)
        #any custom attributes for a interaction model instance

    #This must be a generator
    def _initiate(self,user):

        #can use this for monitoring
        #create a report obect
         #self.monitorData.submitReport(report

        self._user = user
        
        #
        table['Time'].append(editTime(self.env.now + self.clock))
        table['Customer'].append( self._user)
        table['Activity'].append(f"ID - [{self._user.id}] met the pool on interaction object - {self} ID - [{self.id}]")
        table['Interaction'].append(self.name)
        table['qCount'].append(len(CQueue.cQueue[self.name]))


        table['Time'].append(editTime(self.env.now + self.clock))
        table['Customer'].append( self._user)
        table['Activity'].append(f"ID - [{self._user.id}] pool attendant checks the appointment")
        table['Interaction'].append(self.name)
        table['qCount'].append(len(CQueue.cQueue[self.name]))

        
        self.delayClock(3)


        table['Time'].append(editTime(self.env.now + self.clock))
        table['Customer'].append(self._user)
        table['Activity'].append(f"ID - [{self._user.id}] agent is verified")
        table['Interaction'].append(self.name)
        table['qCount'].append(len(CQueue.cQueue[self.name]))


        
        table['Time'].append(editTime(self.env.now + self.clock))
        table['Customer'].append(self._user)
        table['Activity'].append(f"ID - [{self._user.id}] granting access for {self._user}")
        table['Interaction'].append(self.name)
        table['qCount'].append(len(CQueue.cQueue[self.name]))


        table['Time'].append(editTime(self.env.now + self.clock))
        table['Customer'].append(self._user)
        table['Activity'].append(f"ID - [{self._user.id}] leaves to pool")
        table['Interaction'].append(self.name)
        table['qCount'].append(len(CQueue.cQueue[self.name]))

     
        
WorkFlows = {
    'cashier':['ArrivedAtCashier','CheckingRoom'],
    'pool':['ArrivedAtPool'] #here you must enter interaction model keys in Pool
}



   
#----UPDATING POOL AND CROWD QUEUE ----------------
#self.name in each interaction is very important>>>> 
#TODO: each model instance [interaction,store, anything must be added to the respective poop]
IPool.addToPool('ArrivedAtCashier',CashierArrival,2)
CQueue.addQueue('ArrivedAtCashier')
IPool.addToPool('CheckingRoom',CheckRoom,3)
CQueue.addQueue('CheckingRoom')
IPool.addToPool('ArrivedAtPool',PoolArrival,1)
CQueue.addQueue('ArrivedAtPool')




