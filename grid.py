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
        '''
        Test function to iron out the logic of ittereating over fields without
        touching the ghost cells.

        '''
        for i in range(self.grid_y + 1):
            #Itterate over rows, +1 to account for y_vfield stagard positions
            for j in range(self.grid_x + 1):
                #Itterate over collumns, +1 to account for x_vfield stagard positions
                if i != self.grid_y and j != self.grid_x:
                    #Leaves border of p field unchanged
                    self.p_Field[i + 1, j + 1] = 1
                else:
                    pass
                
                if i != self.grid_y:
                    #Leaves top and botton border of x_vfield unchanged
                    self.x_vField[i + 1, j] = 1
                else:
                    pass
                
                if j != self.grid_x:
                    #Leaves left and right border of y_vfield unchanged
                    self.y_vField[i, j + 1] = 1
                else:
                     pass
                 
    def avg_u(self, i, j):
        '''
        Works out the u and averaged v componnent of velocity at a stagard u
        point. U is taken as velocity at grid point, v is averaged over adjecent
        y_vField grid points.

        Parameters
        ----------
        i : int
            Row index of stagard point.
        j : int
            Column index of stagard point.

        Returns
        -------
        averaged_u_field : numpy array
            Contains u and avearged v field at x velocity grid point.

        '''
        
        x_component = self.x_vField[i , j]
        
        y_component = (self.y_vField[i - 1, j] + self.y_vField[i - 1, j + 1] + 
                       self.y_vField[i, j] + self.y_vField[i, j + 1]) / 4
        
        averaged_u_field = np.array([x_component, y_component])
        
        return averaged_u_field
    
    def avg_v(self, i, j):
        '''
        Works out the averaged u and v componnent of velocity at a stagard v
        point. V is taken as velocity at grid point, u is averaged over adjecent
        x_vField grid points.

        Parameters
        ----------
        i : int
            Row index of stagard point.
        j : int
            Column index of stagard point.

        Returns
        -------
        averaged_u_field : numpy array
            Contains u and avearged v field at x velocity grid point.

        '''
        
        x_component = (self.x_vField[i, j-1], self.x_vField[i, j] +
                       self.x_vField[i + 1, j - 1] + self.x_vField[i + 1, j]) / 4
        
        y_component = self.y_vField[i, j]
        
        averaged_v_field = np.array([x_component, y_component])
        
        return averaged_v_field
    

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




    
    
    
    