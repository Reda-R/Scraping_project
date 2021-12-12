import json

# Read in the file
with open('./.tmp_json/data.json', 'r') as file :
    filedata = file.read()

# Replace the target string
filedata = filedata.replace('}\n{', '},{')

# Write the file out again
with open('./.tmp_json/data.json', 'w') as file:
    file.write(filedata)