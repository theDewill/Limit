# This engine here imports all the entities,workflows and initate the simulation 
import simpy as sp
import pandas as pd
import os,sys,random as rnd


# from utility import loadConfigs
# Here is the initial configurations for file imports by adding them to sys path
utility_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utility'))
sys.path.append(utility_path)

import Configs #this will load all the paths to system path
from context import env,table,Monitorings,IPool
from models import WorkFlows #TODO: make it such exports Workflows
from services import getRandomWorkflow
from agents import agentList,agentArrivalDelay
from metrics import generateInteractionDelayPlot



class Engine ():
    def __init__(self):
        pass
            
    def _ignite (self):
        #TODO: have to make this dynamic if had more than 1 type of agents
        
        for agent in list(agentList['customer'].values()): 
            # self._startWorkflow(agent)
            agent.workflow = getRandomWorkflow(len(WorkFlows),WorkFlows)
            print(f"Now the agent :[ {agent} ] is loaded with ID - [{agent.id}]")
            print(f"Agent Workflow - {agent.workflow}")

            #process Event Creation
            for interaction in agent.workflow:
                agent.Events['process'].setdefault(interaction)
                agent.Events['process'][interaction] = sp.Event(env)
            
            for event in range(len(WorkFlows)-1): #TODO: check here this doen not function
            #these user unique set of events to synchronize interaction models
                agent.Events['control'].append(sp.Event(env)) 

            # print(f"user {agent} has events - {agent.Events}")
            env.process(agent.go())
            #agent Arrival Randomness
            yield env.timeout(rnd.randint(0,agentArrivalDelay))

engine = Engine() 
env.process(engine._ignite())
env.run()

print(f"Pool - {IPool.pool}")
#TODO: error is only here following code
SimulationSheet = pd.DataFrame(table)
#csv_path = os.path.join(os.path.dirname(__file__), '..' ,'Interface', 'Send','Sim_001','output.csv')
SimulationSheet.to_csv('./output.csv', index=False)
print(f"Monitorings - {Monitorings}")
print(SimulationSheet)

#PlotGenerator
generateInteractionDelayPlot()