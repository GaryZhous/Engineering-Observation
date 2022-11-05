from matplotlib import pyplot as plt
from temp_sub import read
low_temps = []
high_temps = []
read(input("plz enter the file name:"), low_temps)
read(input("plz enter the file name:"), high_temps)
fig = plt.figure(dpi=128, figsize=(20, 10))
years = [2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012]
plt.plot(years, low_temps, c='red', alpha=0.5)
plt.plot(years, high_temps, c='blue', alpha=0.5)
plt.fill_between(years, low_temps, high_temps, facecolor='blue', alpha=0.1)
plt.title("Yearly Lowest and Highest Temperatures of Toronto Over The Past 10 Years", fontsize=18)
plt.xlabel('Years', fontsize=16)
plt.ylabel('Temperature (°C)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
for i, j in zip(years, low_temps):
   plt.text(i, j+0.5, '({}, {})'.format(i, j))
for i, j in zip(years, high_temps):
   plt.text(i, j+0.5, '({}, {})'.format(i, j))
plt.savefig("Temp.png", bbox_inches='tight')
