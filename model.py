# -*- coding: utf-8 -*-
"""
Created on Wed May  6 19:20:43 2020

@author: Robab
"""
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import framework
import tkinter


elevation = []
in_raster = 1
gradient = []



def test():
    print("dog, cat, fish, goat")


def calculate():

    #external scripts directly run from tkinter run before tkinter.mainloop()
        #set matplotlib window
        #run gradient calculation
        #show calculated gradients in matplotlib window
    fig = matplotlib.pyplot.figure(figsize=(7, 7))
    framework.gradient.angle(elevation, cell_distance, gradient)
    matplotlib.pyplot.title("Gradient")
    matplotlib.pyplot.imshow(gradient)


def txtWriter():
    #external scripts directly run from tkinter run before tkinter.mainloop()
    #pass gradient dataset to .txt file writer
    framework.fileHandler.txtWriter(gradient) 

  
def csvWriter():
    #external scripts directly run from tkinter run before tkinter.mainloop()
    #pass gradient dataset to .csv file writer    
    framework.fileHandler.csvWriter(gradient)


def jsonWriter():
    #external scripts directly run from tkinter run before tkinter.mainloop()
    #pass gradient dataset to .json file writer    
    framework.fileHandler.jsonWriter(gradient)


def fileImport():
    
    def enter_resolution():
        #assign popup window entry to cell_distance global variable
        global cell_distance
        cd = v1.get()
        cell_distance = int(cd)
        print(cell_distance)
        v1.quit()
        #create matplotlib window and display imported elevation data
        framework.fileHandler.tkFileAdd(in_raster, elevation)
        fig = matplotlib.pyplot.figure(figsize=(7, 7))
        matplotlib.pyplot.title("Elevation")
        matplotlib.pyplot.imshow(elevation)    
        
    #external scripts directly run from tkinter run before tkinter.mainloop()
    #create pop up window for user input of data resolution
    root = tkinter.Tk()
    tkinter.Label(root, text="input resolution (m)").grid(row=0)
    v1 = tkinter.Entry(root)
    v1.grid(row=0, column=1)
    tkinter.Button(root, 
                   text='Enter', 
                   command=enter_resolution).grid(row=0, column=2)
    tkinter.mainloop()


#tkinter GUI setup
root = tkinter.Tk()

#set tkinter canvas extent
canvas = tkinter.Canvas(root, bg="blue", height=300, width=500)
canvas.pack()

#add menu bar
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)

#assign canvas menus options
file_menu = tkinter.Menu(menu_bar)
file_import_menu = tkinter.Menu(menu_bar)
file_export_menu = tkinter.Menu(menu_bar)
analysis_menu = tkinter.Menu(menu_bar)

#file >> import cascade options and commands
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_cascade(label="Import", menu=file_import_menu)
file_import_menu.add_command(label="Import from file", command=fileImport)

#file >> export cascade options and commands
file_menu.add_cascade(label="Export", menu=file_export_menu)
file_export_menu.add_command(label="Export as TXT", command=txtWriter)
file_export_menu.add_command(label="Export as CSV", command=csvWriter)
file_export_menu.add_command(label="Export as JSON", command=jsonWriter)

#analysis cascade options and commands
menu_bar.add_cascade(label="Analysis", menu=analysis_menu)
analysis_menu.add_command(label="Elevation to gradients", command=calculate)

tkinter.mainloop()

    
