import math
import numpy as np
from board import *
from geometry import *
from problem import *

def brutforce():
    problem = Problem(self, data)
    opponents = problem.getOpponent(problem)
    field_center = problem.getFieldCenter
    field_width = problem.getFieldWidth
    field_height = problem.getFieldHeight

#le premier defenseur a pour coordonnées le coin haut à gauche du terrain
    defender = field_height - field_width
#pour tout les adversaires, on regarde si notre defenseur arret un tir
    if
    for opponent in opponents :
        if (segmentCircleIntersection(opponent, problem.field_limits[0], defender, problem.robot_radius) not None):
            graph.addDefender(defender)
        defender[0] = defender[0] - robot_radius
        defender[1] = defender [1] + robot_radius
