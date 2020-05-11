# -*- coding: utf-8 -*-
"""
Created on Wed May  6 19:20:43 2020

@author: Robab
"""
import bs4
import requests
import csv
import matplotlib.pyplot
import framework
import tkinter

elevation = []
in_raster = 1
gradient = []
cell_distance = 25


def calculate():
    #external scripts directly run from tkinter run before tkinter.mainloop()
    framework.gradient.angle(elevation, cell_distance, gradient)
    

def txtWriter():
    #external scripts directly run from tkinter run before tkinter.mainloop()
    framework.fileHandler.txtWriter(gradient) 

  
def csvWriter():
    #external scripts directly run from tkinter run before tkinter.mainloop()
    framework.fileHandler.csvWriter(gradient)


def jsonWriter():
    #external scripts directly run from tkinter run before tkinter.mainloop()
    framework.fileHandler.jsonWriter(gradient)


def fileAdd():
    #external scripts directly run from tkinter run before tkinter.mainloop()
    framework.fileHandler.tkFileAdd(in_raster, elevation)


root = tkinter.Tk()

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)

file_menu = tkinter.Menu(menu_bar)
file_export_menu = tkinter.Menu(menu_bar)
analysis_menu = tkinter.Menu(menu_bar)

menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Import", command=fileAdd)
file_menu.add_cascade(label="Export", menu=file_export_menu)
file_export_menu.add_command(label="Export as TXT", command=txtWriter)
file_export_menu.add_command(label="Export as CSV", command=csvWriter)
file_export_menu.add_command(label="Export as JSON", command=jsonWriter)

menu_bar.add_cascade(label="Analysis", menu=analysis_menu)
analysis_menu.add_command(label="Elevation to gradients", command=calculate)

tkinter.mainloop()

    
