from context import Monitorings
import matplotlib.pyplot as plt
from services import CreateInteractionList
from models import WorkFlows

#this must be made dynamic
def generateInteractionDelayPlot():
    dataset = []
    for interaction in CreateInteractionList(WorkFlows):
        for agent in Monitorings['ext']:
            cordinate = []
            cordinate.append(agent.id)
            if interaction in agent._data['delays']:
                cordinate.append(agent._data['delays'][interaction])
                dataset.append(cordinate)
        x, y = zip(*dataset)
        plt.plot(x, y, marker='o', linestyle='', color='b')
        plt.xlabel('Agent ID')
        plt.ylabel('waiting time')
        plt.title(f'{interaction}_Interaction')
        #plt.savefig(f'{interaction}_plot.png')
        plt.show()



