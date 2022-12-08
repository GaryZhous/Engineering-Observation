import pygal
import numpy as np
sample_size = int(input("plz enter the size of the sample:"))
x = []
y = []
z = []
for i in range(sample_size):
  x.append(float(input("plz enter the length of the patio:")))
  y.append(float(input("plz enter the width of the patio:")))
  z.append(float(input("plz enter the height of the patio:")))

x = np.array(x)
y = np.array(y)
z = np.array(z)
volume = x*y*z
volume_space = float(input("plz enter the entire volume of the available space:"))
percentage_occupying = [(val/volume_space)*100 for val in volume]
hist = pygal.Bar(fill = True)
hist.add("",percentage_occupying)
hist.x_labels = volume
hist.x_title = "volume of each patio sample (m^3)"
hist.y_title = "percentage of occupance of each sample (%)"
hist.render_to_file("data.svg")
