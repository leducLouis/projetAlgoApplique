from Node import *

    class Vertex:
        def __init__(self, opponent, defender):
            self.opponent = opponent
            self.defender = defender


        def getOpponent(self):
            return self.opponent
        def getDefender(self):
            return self.defender
