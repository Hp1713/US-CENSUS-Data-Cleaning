import pandas as pd 
import glob
import csv

states  = []

# .glob reads all files starting with the same name in the same path * (0 or more )
for files in glob.glob('states*.csv'):
    file_content = pd.read_csv(files, index_col= [0])
    states.append(file_content)

# concatenating all the files into a single data frame 
us_census = pd.concat(states, ignore_index=True)
