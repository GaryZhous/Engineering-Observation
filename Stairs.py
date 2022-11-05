import stairs_sub
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
my_style = LS('#333366', base_style=LCS)
number_of_section = int(input("plz enter the number of the sections of the stairs:"))
section_names = []
ESDs = []
index = 0
while index < number_of_section:
  fileobject = open(input("plz enter the name of the file:")+".txt", "r")
  filetext = fileobject.readline().strip()
  data_set = []
  while filetext:
    data_set.append(filetext)
    filetext = fileobject.readline().strip()
  
  stairs = stairs_sub.Stairs(input("plz enter the name of the section:"))
  Estimated_SD = stairs.estimated_standard_deviation(data_set)
  section_names.append(stairs.section_label())
  ESDs.append(Estimated_SD)
  fileobject.close()
  index += 1

print(ESDs)
section_naming = ['bottom set of stairs south side', 'south side middle', 'south side top', 'north side bottom set of stairs', 'northside middle set of stairs', 'north side of top set of stairs', 'south of north  set of stairs measured middle', 'south of north  set of stairs measured top', 'south of previous set of stairs']
bits = []
url='https://docs.google.com/document/d/1iC6M47Ul6TJnyj0I7pOl5xQo3Bp8EM4ZpWwGjBiMRw8/edit?usp=sharing'
for i in range(number_of_section):
  bit = {'value':ESDs[i], 'label':section_naming[i], 'xlink':url}
  bits.append(bit)
hist = pygal.Bar(fill=True, style=my_style)
hist.title = "ESD of the heights of the stairs in different sections of SSH"
hist.x_labels = section_names
hist.x_title = "Names of Sections"
hist.y_title = "Estimated Standard Deviations of the heights (cm)"
hist.add("", bits)
hist.render_to_file("Stairs_ESD_visual.svg")
