'''
To save/get some information in/from a json files (tipically used to exchange information between programs or programming languages), there are 2 usual function to manage it. To do so, previuosly it is needed to import the json module.
    - json.dump() -> To save the information. This function takes 2 arguments being the information to be saved and the file object where to save.
    - json.load() -> To get the information saved in a file object. This function takes only 1 arguments that is the file object.
'''
import json
from icecream import ic

'''
=====================================SAVING=====================================
'''
filename = 'json/file3.json'
text = 'This text will be loaded in a json file. The information could be raw data or, otherwise, information about a user, score, accounts,..'
text2 = [1, 3, 5, 7]
with open(filename, 'w') as f:
    json.dump(text, f)


'''
====================================LOADING====================================
'''
with open(filename) as f:
    content = json.load(f)
ic(type(content))
ic(content)
