#This module will be loaded on start thorugh engine
import random as rnd
from context import Monitorings
#----Monitoring Department-------

class ResultMonitor:
    def __init__(self,oid,Iname,entityType): #either resource or entity its oid [object id], and type -['ext','int']...]
        self.id = oid
        self.name = Iname
        self._report = ""
        self._data = {'delays':{}} #this will be mostly used for Agents
        Monitorings[entityType].append(self)
    
    def submitReport (self,report): #you must pass the report object created acording to your defined schema
        self._report = report
#prepare monitoring set


#----- Sample Creator-----

def CreateSample(writable,agentClass,identity,size):
    #print(writable)
    for count in range(0,size):
        writable.setdefault(identity, {})
        writable[identity][count] = agentClass(count)


#------Creating interaction List------
def CreateInteractionList(workflows):
    interactionList = []
    for one in workflows.values():
        for two in one:
            if two not in interactionList:
                interactionList.append(two)
    return interactionList
       




#----- Workflow Creator-----
def WorkflowCreator(*args):
    workflow = [] #args will get arrays if interaction model objects 
    for arg in range(0,len(args)):
        workflow.append(arg)
    return workflow
#interaction.order-1 TODO: replace this with following 0
def createWorkflow(workflows,interaction):
        workflows.setdefault(interaction.workflow, [])
        workflows[interaction.workflow].insert(interaction.order,interaction)

def getRandomWorkflow(count, workflows):
    workFlowList = list(workflows.values())
    return workFlowList[rnd.randint(0,count-1)]

def editTime(time):
    if len(str(time)) == 1:
        return f'0{time}.00'
    else:
        return f'{time}.00'

#------ EVENT HANDLing Deaprtment -----------

class Event():
    def __init__(self,event_list = []):
        self.event_list = event_list
        self.event_handlerArray = {
            event_list[0]: lambda: self.handleExampleEvent(),
            event_list[1]: lambda: self.handleExampleEvent_2() #todo - parse to generator 
                
        }
    
    def Emit(self,event):
        self.event_handlerArray[event]()

    #Custom declaration of eventHandlers.... [by using dev]

    def handleExampleEvent_1(self):
        pass

    def handleExampleEvent_2(self):
        pass


#-------- Result Exporter --------