# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 16:39:04 2022

@author: user
"""
import numpy as np

class Fluid:
    def __init__(self, grid_x, grid_y, grid_spacing):
        '''
        Creates a stagard grid for fluid simulations. Size of the grid is given by grid_x
        and grid_y. At each boundary there is a ghost cell that extends the grid.
        Horizontal and vertical velocity fields are placed at grid edges, not center.
        -------
        grid_x : int
            Number of x grid components.
        grid_y : int
            Number of y grid components
        grid_spacing : int
            set spacing of grid
            
    
        Returns
        -------
        x_vField : np.array
            returns an array for horizontal velocity field.
        y_vField : np.array
            return an array for vertical velocity field.
        p_Field : np.array
            returns pressure field
    
        '''
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.grid_spacing = grid_spacing
        
        self.x_vField = np.zeros((grid_y + 2, grid_x + 1))
        self.y_vField = np.zeros((grid_y + 1, grid_x + 2))
        self.p_Field = np.zeros((grid_y + 2, grid_x + 2))
        
    def non_ghost_itteration(self):
        for i in range(self.grid_y + 1):
            for j in range(self.grid_x + 1):
                if i != self.grid_y and j != self.grid_x:
                    self.p_Field[i + 1, j + 1] = 1
                else:
                    pass
                
                if i != self.grid_y:
                    self.x_vField[i + 1, j] = 1
                else:
                    pass
                
                if j != self.grid_x:
                    self.y_vField[i, j + 1] = 1
                else:
                    pass
                
                # self.x_vField
                # self.y_vField
                
                
            
    
        

def stagard_grid(grid_x, grid_y):
    '''
    Creates a stagard grid for fluid simulations. Size of the grid is given by grid_x
    and grid_y. At each boundary there is a ghost cell that extends the grid.
    Horizontal and vertical velocity fields are placed at grid edges, not center.
    -------
    grid_x : int
        Number of x grid components.
    grid_y : int
        Number of y grid components


    Returns
    -------
    x_vField : np.array
        returns an array for horizontal velocity field.
    y_vField : np.array
        return an array for vertical velocity field.
    P_Field : np.array
        returns pressure field

    '''
    x_vField = np.zeros((grid_y + 2, grid_x + 1))
    y_vField = np.zeros((grid_y + 1, grid_x + 2))
    P_Field = np.zeros((grid_y + 2, grid_x + 2))
    
    return x_vField, y_vField, P_Field




    
    
    
    