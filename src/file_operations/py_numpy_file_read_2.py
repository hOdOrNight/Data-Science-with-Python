# Import package
import numpy as np
import pandas as pd

from helper import path

# Assign the filename: file
file = 'amis.csv'

# Load the data: data
data = np.loadtxt(path + file, delimiter=',', skiprows=1, usecols=[1, 3])

# Print data
print(data)

# Read flat file to data frame

# Read the first 5 rows of the file into a DataFrame: data
data = pd.read_csv(path + file, nrows=5, header=None)

# Build a numpy array from the DataFrame: data_array
data_array = np.array(data)

# Print the datatype of data_array to the shell
print(type(data_array))
