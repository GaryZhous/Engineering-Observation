def read(file_name, list):
  fileobject = open(file_name + '.txt', "r")
  filetext = fileobject.readline()
  while filetext:
   list.append(int(filetext))
   filetext = fileobject.readline()
