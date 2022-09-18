from dbmain import add_recordngs
import numpy as np
import json

matrix = np.zeros((3, 3), dtype=int)
add_recordngs(matrix)
print("added matrix")
