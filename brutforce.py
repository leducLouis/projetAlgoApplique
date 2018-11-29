import math
import numpy as np
from board import *
from geometry import *
from problem import *

def brutforce():
    problem = Problem(self, data)
    field_center = problem.getFieldCenter
    field_width = problem.getFieldWidth
    field_height = problem.getFieldHeight

#le premier defenseur a pour coordonnées le coin haut à gauche du terrain
    defender = field_height - field_width
#pour tout les adversaires, on regarde si notre defenseur arret un tir
    if (defender[0]>field_limits[0] and defender[1] < field_limits[1]):
        for i in range(0, problem.getNbOpponents)
            if (segmentCircleIntersection(problem.getOpponent(problem, i), problem.field_limits[0], defender, problem.robot_radius) not None):
                graph.addNode(problem.getOpponent(i), defender)
            defender[0] = defender[0] - robot_radius
            defender[1] = defender [1] + robot_radius
