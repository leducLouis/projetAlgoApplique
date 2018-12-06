from problem import *
from board import *
from geometry import *
from problem import *
import json
import numpy


class Graph:
    def __init__(self, problem_path):
            #self.problem = Problem(data)
            self.vertex = []
            self.nodes = []
            """for i in range (0, self.problem.getNbOpponents, 1):
                self.nodes.append(Node("opponent", self.problem.getOpponent(i)))
"""
            problem_path = problem_path
            with open(problem_path) as problem_file:
                problem = Problem(json.load(problem_file))

            field_center = problem.getFieldCenter()
            field_width = problem.getFieldWidth()
            field_height = problem.getFieldHeight()
            pos_step = problem.getPosStep()
            theta_step = problem.getThetaStep()
            robot_radius = problem.getRobotRadius()

            array_width = numpy.arange(-(field_width/2) + pos_step, field_width, pos_step)
            array_height = numpy.arange((int(field_height/2)) + pos_step, -field_height, -pos_step)

            for i in array_width:
                for j in array_height:
                    defender = {}
                    defender[0] = i
                    defender[1] = j
                    theta_step_tmp = theta_step
                    for o in range (0, problem.getNbOpponents(), 1):
                        while theta_step_tmp < 1: ############## test pour le while, pas du tout sure de la condition
                            kick = segmentLineIntersection(problem.getOpponent(o)[0],problem.getOpponent(o)[1], problem.field_limits[0], problem.field_limits[1])
                            if kick is not None:
                                if segmentCircleIntersection(self.problem.getOpponent(o), kick, defender, robot_radius) is not None:
                                    with open('graph.json', 'w', encoding='utf-8') as solution_file:
                                        data["defenders"] = defender
                            theta_step_tmp += theta_step


    def addNode(opponent, defender):
        self.nodes.append(Node("defender", defender))
        print(defender)
        self.vertex.append(Vertex(opponent, defender))
