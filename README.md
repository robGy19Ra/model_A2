# Elevation to gradient calculation tool
A tool for importing elevation data, calculating the downhill slope, viewing, and exporting the results.

## Prerequisites
the gradient calculator makes use of several third-party python libraries and utilises the framework.py script supplied.
other used python libraries include:
tkinter, matplotlib, csv, json, math and bs4.

### Usage
The model is used to import raw elevation data and manually define the resolution/cell size. This in turn affects gradient calculations.
A downhill gradient is calculated against immediately adjacent elevations with the greatest downhill gradient assigned.
Cells where no adjoining cell has a lower elevation, known as pits, have no downhill slope. Pits are artificially filled on the resultant layer with a zero (0) figure.
An array of the landscape's gradients can be exported in .csv, .txt or .json formats.
the initial import and the resultant array are viewed in external matplotlib windows for easy comparison
