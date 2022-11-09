import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data

#print(london_data.head())

print(len(london_data))
temp = london_data.TemperatureC
#print(temp)

average_temp = np.mean(temp)
print(average_temp)
temperature_var = np.var(temp)
print(temperature_var)
temperature_standard_deviation = np.std(temp)
print(temperature_standard_deviation)

print(london_data.head())

june = london_data.loc[london_data['month'] == 6].TemperatureC
july = london_data.loc[london_data['month'] == 7].TemperatureC

print(np.mean(june))
print(np.mean(july))

print(np.std(june))
print(np.std(july))

for i in range(1, 24):
  month = london_data.loc[london_data["hour"] == i].dailyrainMM
  print("The mean rain in hour "+str(i) +" is "+ str(np.mean(hour)))
  print("The standard deviation of rain in hour "+str(i) +" is "+ str(np.std(hour)) +"\n")










