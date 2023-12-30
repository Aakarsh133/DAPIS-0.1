import pandas as pd 
import numpy as np 
import random as r
from Frontend import Welcome_screen, Menu1
#from Backend import dataset_importer

Welcome_screen.animation()
df= Menu1.men1()
print("\nThe presented database is:- \n")
print(df.head())

