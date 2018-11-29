from problem import *

class Graph:
    def __init__(self, data):
            self.problem = Problem(data)
            self.vertex = []
            self.nodes = []
            for i in range (0, self.problem.getNbOpponents, 1):
                self.nodes.append(Node("opponent", self.problem.getOpponent(i)))

    def addNode(opponent, defender):
        self.nodes.append(Node("defender", defender))
        self.vertex.append(Vertex(opponent, defender))
