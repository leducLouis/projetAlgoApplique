import math
import numpy as np
import json
import sys
from board import *
from geometry import *
from problem import *

problem_path = sys.argv[1]
with open(problem_path) as problem_file:
    problem = Problem(json.load(problem_file))
field_center = problem.getFieldCenter()
field_width = problem.getFieldWidth()
field_height = problem.getFieldHeight()
pos_step = problem.getPosStep()
theta_step = problem.getThetaStep()
goal_top = problem.getGoalTop()
goal_bottom = problem.getGoalBottom()
robot_radius = problem.getRobotRadius()

for i in range (-(field_width/2) + pos_step, field_width, pos_step):
    for j in range((field_height/2) + pos_step, -field_height, -pos_step):
        defender = {}
        defender[0] = i
        defender[1] = j
        for o in range (0, problem.getNbOpponents, 1):
## TO DO : on verifie l'intersection opposant / chaque tir possible avec thetastep
            for s_x in range (goal_top[0], goal_bottom[0], theta_step):
                for s_y in range (goal_top[1], goal_bottom, theta_step):
                    seg_end = []
                    seg_end[0] = s_x
                    seg_end[1] = s_y
                    if segmentCircleIntersection(self.problem.getOpponent(o), seg_end, defender, robot_radius) is not None:
                        with open('brutforceSolution.json', 'w', encoding='utf-8') as solution_file:
                            data["defenders"] = defender


"""
#le premier defenseur a pour coordonnees le coin haut a gauche du terrain
defender = {}
defender[0] = -(field_width/2) + pos_step
defender[1] = (field_height/2) + pos_step
#pour tous les adversaires, on regarde si notre defenseur arrete un tir
if (defender[0]>field_width[0] and defender[1] < field_height[1]):
    data = {}
    for i in range(0, problem.getNbOpponents):
        if segmentCircleIntersection(problem.getOpponent(problem, i), problem.field_limits[0], defender, problem.robot_radius) is not None:
            graph.addNode(problem.getOpponent(i), defender)
            with open('brutforceSolution.json', 'w', encoding='utf-8') as f:
                data["defenders"] = defender
                json.dump(data)
        defender[0] = defender[0] - robot_radius
        defender[1] = defender [1] + robot_radius
"""
