# -*- coding: utf-8 -*-
"""
Created on Sun May 10 12:35:25 2020

@author: Robab
"""
import math
import tkinter
import tkinter.filedialog
import csv
import json
import requests
import bs4


class gradient():
    
    #calculate maximum downhill gradient across elevation dataset
    def angle(elevation, cell_distance, gradient):
        #n is a reference for each row across the 2d array
        n = 0
        for e_row in elevation:
            g_row = []
            #i is reference for each value in row
            i = 0
            for e_value in e_row:
                """if statements stop the script looking over the edges of the raster
                and sets slope from off the map to 0"""
                if i == len(e_row)-1:     #if i is the final figure on a row
                    i_add = i           #imaginary figure to right is given value of i
                    i_sbtr = i-1        #figure to left can still be found
                    
                elif i == 0:            #if i is the first figure on a row    
                    i_sbtr = i          #imaginary figure to left is given the value of i
                    i_add = i+1         #figure to right can still be found
                    
                else:                   #if i is not first or last position of row
                    i_add = i+1         #figure to right can be found
                    i_sbtr = i-1        #figure to left can be found
                    
                if n == len(elevation)-1:   #if n is the final row in the dataset
                    n_add = n               #imaginary figure below is given the value of n
                    n_sbtr = n-1            #figure above can still be found
                    
                elif n == 0:                #if n is the first row in the dataset
                    n_sbtr = n              #imaginary figure above is given the value of n
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
        
                #diagonally located reference cells
                r8_diag = [g2, g4, g6, g8]
                #perpendicular located reference cells
                r8_xy = [g1, g3, g5, g7]
                
                #finding the lowest elevation from each set
                min_r8_diag = min(r8_diag)
                min_r8_xy = min(r8_xy)
                
                #calculating the downhill slope to each of the lowest elevations
                height_difference_diag = float(e_value) - float(min_r8_diag)
                height_difference_xy = float(e_value) - float(min_r8_xy)
                
                #if height difference is negative it means we have a pit
                if height_difference_diag or height_difference_xy >= 0:
                    #calculate maximum perpendicular downhill slope
                    xy_rad = math.atan(height_difference_xy / cell_distance)
                    #convert radians to degrees and round to 1 decimal place
                    xy = round(math.degrees(xy_rad),1)
                    
                    #calculate maximum diagonal downhill slope
                    xd_rad = math.atan(height_difference_diag / (cell_distance*2)**0.5)
                    #convert radians to degrees and round to 1 decimal place
                    xd = round(math.degrees(xd_rad),1)     
                    
                    x = max([xy, xd]) #get largest downhil slope
                    
                #pits cancelled out to 0 gradient.
                else:
                    x = 0    
                #add each maximum downhill angle to row
                g_row.append(float(x))           
                i += 1 
            #add each calculated row to gradient array    
            gradient.append(g_row)    
            n += 1
            
        print(gradient)


class fileHandler():
    
    def tkFileAdd(in_raster, elevation):
        print("loading data from file")
        #read in txt/csv elevation data
        in_raster = tkinter.filedialog.askopenfile(mode="r")
        reader = csv.reader(in_raster)
        for row in reader:
            rowlist = []
            for value in row:
                #append each value to row
                rowlist.append(float(value)) #float - matplotlib conversion error 
            #append row to elevation    
            elevation.append(rowlist)       
        in_raster.close()
        print(elevation)
        
    def tkWebAdd(in_raster, elevation, webaddress):
        print("loading data from webpage")
        r = requests.get(
            webaddress
            )
        content = r.text
        soup = bs4.BeautifulSoup(content, 'html.parser')
        x = soup.find_all()
        print(x)

                                        
    def txtWriter(gradient):
        #write gradient array to .txt file
        print("compile data as .txt document")
        data = gradient
        out_txt = tkinter.filedialog.asksaveasfilename() 
        file = open(out_txt, 'w', newline='')
        writer = csv.writer(file, delimiter=',')
        for row in data:
            writer.writerow(row)
        file.close()
        
        
    def csvWriter(gradient):
        #write gradient array to .csv file
        print("compile data as a .csv document")
        data = gradient
        out_csv = tkinter.filedialog.asksaveasfilename() 
        file = open(out_csv, 'w', newline='')
        writer = csv.writer(file, delimiter=',')
        for row in data:
            writer.writerow(row)
        file.close()
        
        
    def jsonWriter(gradient):
        #write gradient array to .json file
        print("compile data as a .JSON document")
        data = gradient
        out_json = tkinter.filedialog.asksaveasfilename() 
        file = open(out_json, 'w')
        json.dump(data, file)
        file.close()
        
        