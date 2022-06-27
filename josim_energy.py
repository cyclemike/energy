#Author: Michael Johnston
#Credit: Yohsikawa Lab
#Date: 21 June 2022
#
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# read a csv file as pandas dataframe
csvpath = "C:/Users/Michael/Documents/python/energy/out.csv"
df = pd.read_csv(csvpath, index_col=0)

#heading in csv file
current_column = "I(LX|XA4)"
voltage_column = "V(LX|XA4)"

# extract IV columns
iv_df = df[[voltage_column, current_column]]

f = 5e9
T = 1/f
print (T)
start = 1000E-12
N = 4
end = start + 8*T
dt = 0.1E-12 #timestep - must be identical to voltage and current timestep in csv

new_df = iv_df.query(f"{start} <= time <= {end}")
new_df["IV"] = new_df[current_column] * new_df[voltage_column]*dt

energy = new_df["IV"].sum() #summation resulting in total energy..
#
print("----------------------------------------")
print("Energy: ",energy/N)
print("----------------------------------------")
#
print(new_df)
plt.plot(new_df["I(LX|XA4)"])
plt.plot(new_df["V(LX|XA4)"])
plt.plot(new_df["IV"])

new_df["IV"].sort_values()
print(new_df)
