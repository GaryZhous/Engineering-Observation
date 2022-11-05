class Stairs():
  def __init__(self, name="bruh"):
    self.name = name
  def estimated_standard_deviation(self, data):
    new_set = [float(value) for value in data]
    sum = 0
    for i in data:
     sum += float(i)
    data_size = len(data)
    avg = sum/data_size
    data1 = 0
    for g in new_set:
     data1 += (g-avg)**2
    Estimated_Variance = data1/(data_size-1)
    return round(Estimated_Variance**0.5, 3)
  def section_label(self):
    return self.name.title()
