# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 19:44:53 2024

@author: Owl
"""
import numpy as np

matrix = np.zeros((10, 10))

matrix[0, :] = 1         
matrix[-1, :] = 1        
matrix[:, 0] = 1         
matrix[:, -1] = 1        


print(matrix)
