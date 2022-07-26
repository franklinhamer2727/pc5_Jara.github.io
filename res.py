
with open('build/index.html', 'r') as file :
  filedata = file.read()



with open('build/index.html', 'w') as file:
  file.write(filedata)