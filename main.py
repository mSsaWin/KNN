import csv
import pandas as pd
from knn import *
reader = pd.read_csv("data_raw.csv",delimiter = ';')
reader = pd.DataFrame(reader)

earthquakes = list()
header = 0
for latitude, longitude, magnitude in zip(reader['Latitude'],reader['Longitude'],reader['Magnitude']):
  earthquakes.append(([latitude,longitude],magnitude))

for k in range(1,7):
  n_correct = 0
  for earthquake in earthquakes:
    values, actual_br = earthquake
    other_earthquake = [other_earthquake for other_earthquake in earthquakes if other_earthquake != earthquake]
    predicted_br = knn_classify(k, other_earthquake, values)
    if predicted_br == actual_br:
      n_correct +=1
  print(k, "соседей:",n_correct,"правильных из",len(earthquakes))

k = 3
coords = input("\n\nInput the latitude and longitude[delimeter - ,]").split(', ')
coords = [float(coord) for coord in coords]
predicted_br = knn_classify(k, earthquakes, coords)
print(f'An earthquake at a {coords[0]},{coords[1]} will have a magnitude: {predicted_br}')