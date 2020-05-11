# -*- coding: utf-8 -*-
"""
Created on Sun May 10 12:35:25 2020

@author: Robab
"""
import math

class gradient():
       
    def angle(elevation, cell_distance):

        n = 0
        offset = 1
        for row in elevation:
            i = 0
            for value in row:
                """if statements stop the script looking over the edges of the raster
                and sets slope from off the map to 0"""
                if i == len(row)-1:     #if i is the final figure on a row
                    i_add = i           #figure to right is given value of i
                    i_sbtr = i-1        #figure to left can still be found
                    
                elif i == 0:            #if i is the first figure on a row    
                    i_sbtr = i          #figure to left is given the value of i
                    i_add = i+1         #figure to right can still be found
                    
                else:                   #if i is not first or last position of row
                    i_add = i+1         #figure to right can be found
                    i_sbtr = i-1        #figure to left can be found
                    
                if n == len(elevation)-1:   #if n is the final row in the dataset
                    n_add = n               #figure below is given the value of n
                    n_sbtr = n-1            #figure above can still be found
                    
                elif n == 0:                #if n is the first row in the dataset
                    n_sbtr = n              #figure above is given the value of n
                    n_add = n+1             #figure below can still be found
                    
                else:                   #if n i not in the first or last row in dataset
                    n_add = n+1         #figure below can still be found
                    n_sbtr = n-1        #figure above can still be found
                    
            #finding the value of surrounding elevations in R8 form
                g1 = (elevation[n][i_add]) 
                g2 = (elevation[n_sbtr][i_add])
                g3 = (elevation[n_sbtr][i])
                g4 = (elevation[n_sbtr][i_sbtr])
                g5 = (elevation[n][i_sbtr])
                g6 = (elevation[n_add][i_sbtr])
                g7 = (elevation[n_add][i])
                g8 = (elevation[n_add][i_add])
        
                r8 = [g1, g2, g3, g4, g5, g6, g7, g8]
             
                height_difference = value - min(r8)
                
                if height_difference >= 0:     
                    x = math.atan(height_difference / cell_distance)
                    print(math.degrees(x))
        
                else:
                    #pitRemove()
                    #pitHighlight() 
                    break
        
                i += 1
            n += 1
