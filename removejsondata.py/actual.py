
import json
from os import link
import pandas as pd
import numpy as np

with open('final_sulekha_data.json') as f:
   data = json.load(f)
   
   
temp = json.dumps(data,indent=2)
print(temp)

# print(type(data))

# for descps in data:
#     if descps == 'descp':
#         print ("ajdsknfksdac")
    

# def drop_duplicates(data):
#     """ Appends the item to the returned array only if not
#         already present in our dummy array that serves as reference.
#     """
#     selected  = []
#     links = []
#     for item in data:
#         if item['links'] not in link:
#             selected.append(item)
#             links.append(item['links'])
#     return selected

# print( drop_duplicates(data) )

# try:
#     with open('final_sulekha_data.json', 'r') as fr:
#         lines = fr.readlines()
 
#         with open('final_sulekha3n_data.json', 'w') as fw:
#             for line in lines:
#                if line.strip("\n") != "Flat 10% OFF on posting fee15% off Resume PackageOrLocal":
#                 fw.write(line)
#                 # find() returns -1
#                 # if no match found
#                 # if line.find("Flat 10% OFF on posting fee15% off Resume PackageOrLocal") == -1:
#                 #     fw.write(line)
#     print("Deleted")
# except:
#     print("Oops! something error")




temp = json.dumps(data,indent=6)

# with open('final_sulekha_data.json') as f:
#     for line in f:
#         data = json.load(f)
        
#     ww = pd.DataFrame(data)
# ww.head()