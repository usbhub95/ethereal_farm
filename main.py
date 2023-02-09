# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 16:40:59 2023

@author: Cooper
"""

import numpy as np

#takes raw blueprint paste from game and turns it into a numpy array
def parse_blueprint(blueprint):
    #split input lines into list
    blueprint = blueprint.split(sep="\n")
    #iterate over now split lines to create a matrix
    for index, item in enumerate(blueprint):
        #split row string into list of characters, thus creating a matrix
        blueprint[index] = list(item)
    
    #return the matrix as a numpy array
    return np.array(blueprint, dtype=str)
    
print("started")
board_matrix = parse_blueprint(input("paste blueprint"))
print(board_matrix)
