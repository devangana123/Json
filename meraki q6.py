# Q6.Python object key unique key value ko access karne ka program likho?

# Original Python object:- 

# {
#     "a":  1, 
#     "a":  2, 
#     "a":  3, 
#     "a": 4, 
#     "b": 1, 
#     "b": 2
# }


# Unique Key in a JSON object:-

# {'a': 4, 'b': 2}


import json
j={
    "a":1,
    "a":2,
    "a":3,
    "a":4,
    "b":1,
    "b":2
}
a={}
for i in j:
    if i not in a:
        a.update(j)
print("Unique key in json object=",a)    

