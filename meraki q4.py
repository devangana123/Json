# Q4.Python dictionary(sort by key) object ko json data ::mai convert karne ka program likho?

import json
j={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}

b=open("meraki q4.json" ,"w")
b.write((json.dumps(j,sort_keys=True,indent=4)))
b.close()
