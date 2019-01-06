# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 17:58:00 2019

@author: usuario
"""
def suma(a,b):
     return a + b
# suma(1,4) 
#debes colocarlo en la terminal
suma(3,4)

import numpy as np
def function(x):
    return np.sqrt(x+2)
function(23) 
function(34)    
#debes colocarlo en la terminal
    
x=np.array([-1,0,3,5,13,15])
y=function(x)
print(y)

## Uso de pandas
import pandas as pd
tabla = pd.DataFrame(list(zip(x,y)),columns=["x", "f(x)"])
print(tabla)