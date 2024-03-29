from problem import *
from board import *
from geometry import *
from problem import *
import io
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

            #toutes les positions de defenseurs
            array_width = numpy.arange(-(field_width/2) + pos_step, field_width, pos_step)
            array_height = numpy.arange((int(field_height/2)) + pos_step, -field_height, -pos_step)
            data = {}
            with io.open('graph.json', 'w', encoding='utf-8') as solution_file:
                solution_file.write(unicode("{ edges : "))
                for i in array_width:
                    for j in array_height:
                        defender = [i, j]
                        theta_step_tmp = theta_step
                        for o in range (0, problem.getNbOpponents(), 1):
                            #while theta_step_tmp < 1: ############## test pour le while, pas du tout sure de la condition
                                #print (problem.field_limits)
                                #kick = segmentLineIntersection(problem.getOpponent(o), problem.field_limits[0][0],problemproblem.field_limits[0][1])
                                #if kick is not None:
                                #i = 0
                                #for j in range (0,5,1)
                            if segmentCircleIntersection(problem.getOpponent(o),problem.field_limits[0], defender, robot_radius) is not None:
                                    defender[0] = round (defender [0], 2)
                                    defender [1] = round(defender [1], 2)
                                    data ["defender"] = defender
                                    data ["opponent"] = problem.getOpponent(o).tolist()
                                    solution_file.write(unicode(json.dumps(data, ensure_ascii=False)))
                            #theta_step_tmp += theta_step
                solution_file.write(unicode("}"))

    def addNode(opponent, defender):
        self.nodes.append(Node("defender", defender))
        print(defender)
        self.vertex.append(Vertex(opponent, defender))
