# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 16:39:04 2022

@author: user
"""
import numpy as np
import math

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
                    self.x_vField[i + 1, j] = 0.3 - 0.02 * j
                else:
                    pass
                
                if j != self.grid_x:
                    #Leaves left and right border of y_vfield unchanged
                    self.y_vField[i, j + 1] = -0.1
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
        
        x_component = (self.x_vField[i, j-1] + self.x_vField[i, j] +
                       self.x_vField[i + 1, j - 1] + self.x_vField[i + 1, j]) / 4
        
        y_component = self.y_vField[i, j]
        
        averaged_v_field = np.array([x_component, y_component])
        
        return averaged_v_field
    
    def sample_field(self, x_coordinate, y_coordinate, field):
        '''
        Take

        Parameters
        ----------
        x_coordinate : float
            x coordinate of the field that will be sampled.
        y_coordinate : T
            y coordinate of the field that will be sampled.
        field : np.array
            Field that will be sampled.

        Returns
        -------
        sampled_field_value: float
            value of the field at sample position.
        '''
        max_y_coordinate, max_x_coordinate = field.shape
        #Makes sure coordinate is within array, clips to closest edge if not
        x_coordinate = np.minimum(max_x_coordinate, np.maximum(x_coordinate, 0))
        y_coordinate = np.minimum(max_y_coordinate, np.maximum(y_coordinate, 0))
        
        #split the float coordinate positions into integer coordinate positions
        #and fractioninal displacment from integer coordinate positions
        
        x_frac, column_index = math.modf(x_coordinate)
        y_frac, row_index = math.modf(y_coordinate)
        
        column_index = int(column_index)
        row_index = int(row_index)
        
        #Fractional displacment is used to calculate weighted average of neighbouring
        #grid points
        sample_field_value = ((1 - x_frac) * (1 - y_frac) * field[row_index, column_index] +
                              x_frac * (1 - y_frac) * field[row_index, column_index + 1] +
                              (1 - x_frac) * y_frac * field[row_index + 1, column_index] +
                              x_frac * y_frac * field[row_index + 1, column_index + 1])
        
        return sample_field_value
    
    def advect_velocity():
        pass
        
        

        
    

simulation = Fluid(5, 4, 0.1)
simulation.non_ghost_itteration()
timestep = 1
h = simulation.grid_spacing
field = simulation.x_vField

print(simulation.x_vField)

i = 3
j = 4

velocity = simulation.avg_u(i, j)
print(velocity)

x_mid_point = j - 0.5 * timestep * velocity[0] / h
y_mid_point = i + 0.5 * timestep * velocity[1] / h
                                            
midpoint_x_velocity = simulation.sample_field(x_mid_point, y_mid_point, field)
midpoint_y_velocity = simulation.sample_field(x_mid_point, y_mid_point, simulation.y_vField)
#! Need to consider if sampling the y field at the same point as the x field
#will introduce any error into the working.

print(x_mid_point)
print(y_mid_point)

print(midpoint_x_velocity)
print(midpoint_y_velocity)


x_position = j - timestep * midpoint_x_velocity / h
y_position = i + timestep * midpoint_y_velocity / h

print(x_position)
print(y_position)


y, i_new = math.modf(y_position)
x, j_new = math.modf(x_position)

i_new = int(i_new)
j_new = int(j_new)

sampled_field_value = ((1 - x) * (1 - y) * field[i_new, j_new] +
                      (x) * (1 - y) * field[i_new, j_new + 1] +
                      (1 - x) * (y) * field[i_new + 1, j_new] +
                      (x) * (y) * field[i_new + 1, j_new + 1])
                      
print(sampled_field_value)


# for i in range(simulation.grid_y + 1):
#     #Itterate over rows, +1 to account for y_vfield stagard positions
#     for j in range(simulation.grid_x + 1):
#         #Itterate over collumns, +1 to account for x_vfield stagard positions

#         if i != simulation.grid_y:
#             #Leaves top and botton border of x_vfield unchanged
#             empty_array_x[i + 1, j] = simulation.avg_u(i + 1, j)[1]
#         else:
#             pass
        
#         if j != simulation.grid_x:
#             #Leaves left and right border of y_vfield unchanged
#             empty_array_y[i, j + 1] = simulation.avg_v(i, j + 1)[0]
#         else:
#              pass

# u = empty_array_x
# v = empty_array_y

# print(u)
# print(v)

    
    
    
    