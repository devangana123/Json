# Q7.Text file data ko json file data mai convert karo,jaise ki neeche diya hai?

import json


dic={ "Name ":"Abhishek","Designation":"CEO of navgurukul","Gender" :"male","Age": 29}
a=json.dumps(dic,indent=2)
with open("Text.text.json","w") as f:
    f.write(a)
    f.close()
f=open("Text.text.json","r")
b=f.read
# print(a)