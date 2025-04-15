from game import Agent
from game import Directions
from game import Actions
import random

class DumbAgent(Agent):
     "An agent that goes East until it can't."
     def getAction(self, state):
         "The agent receives a GameState (defined in pacman.py)."
         print("Location: ", state.getPacmanPosition())
         print("Actions available: ", state.getLegalPacmanActions())
         if Directions.EAST in state.getLegalPacmanActions():
             print("Going East.")
             return Directions.EAST
         else:
             print("Stopping.")
             return Directions.STOP

class RandomAgent(Agent):
    "An agent that chooses a random action."
    def getAction(self, state):
        legalAction = state.getLegalPacmanActions()
        currentPosition = state.getPacmanPosition()
        print("Current Location:", currentPosition)
        print("Available Actions:", legalAction)
        chosenAction = random.choice(legalAction)
        print("Randomly chosen action:", chosenAction)
        return chosenAction

class  BetterRandomAgent(Agent):
    "An agent that chooses a random action without stop action include."
    def getAction(self, state):
        legalAction = state.getLegalPacmanActions()
        currentPosition = state.getPacmanPosition()
        noStopActions = [act for act in legalAction if act != Directions.STOP]
        if noStopActions:
            chosenAction = random.choice(noStopActions)
        else:
            #Buộc chọn action stop nếu không còn action nào cho agent lựa chọn
            chosenAction = Directions.STOP
        print("Current Location:", currentPosition)
        print("Available Actions:", legalAction)
        print("Chosen action (avoiding Stop if possible):", chosenAction)
        return chosenAction


class ReflexAgent(Agent):
    def getAction(self, state):
        legalAction = state.getLegalPacmanActions()
        currentPosition = state.getPacmanPosition()
        f = state.getFood()
        foodActions = []
        for act in legalAction:
            if act == Directions.STOP:
                continue
            dx, dy = Actions.directionToVector(act)
            newX = int(currentPosition[0] + dx)
            newY = int(currentPosition[1] + dy)
            if f[newX][newY]:
                foodActions.append(act)
        if foodActions:
            chosenAction = foodActions[0]
            print("Food detected. Taking the next action:", chosenAction)
            return chosenAction
        else:
            nonStopActions = [action for action in legalAction if action != Directions.STOP]
            if nonStopActions:
                chosenAction = random.choice(nonStopActions)
            else:
                chosenAction = Directions.STOP
            print("Not detected food. Taking random action:", chosenAction)
            return chosenAction