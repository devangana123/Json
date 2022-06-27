# Q8.Tumhare pass four employes ki details hai list mai:-

# [“neelam”,”programer”,”24”,”2400”,]
# [“komal”,”trainer”,”24”,”20000”]
# [“anuradha”,”HR”,”25”,”40000”]
# [“Abhishek”,”manager”,”29”,”63000”]

# Visualize

# ab aapko 4 dictionaries create karni hai jaise ki emp1 emp2 emp3 and emp4.
# har ek employee ka dictionary main name,designation,age and salary honi chahiye.
# aur ye sab dictionary ki keys hai jismai maine list main value di hai. Iska use kar ke aapko ek json file create karni hai? Jaise ki niche diya hai.

# Output:-

# { 
#      "emp1":{ "name":"nilam",
#        "Designation":"programmer",
#        "Age":"34",
#        "salary":"24000",
#          }

#     "emp2":
#       { "name":"komal",
#         "Designation":"Trainee",
#         "Age":"24",
#         "salary":"20000" ,
#         }

 
#     "emp3":
#        { "name":"anuradha",
#          "Designation":"HR",
#          "Age":"25",
#          "salary":"40000",
#          }


#     "emp4":
#        { "name":"Abhishek",
#          "Designation":"Manager",
#          "Age":"29",
#        }
#  }





import json
keys=["name","degignation","age","salary"]  
a=["neelam","programer","24","24000"]   
empy1={}   
empy2={}   
empy3={}   
empy4={}   
dict={}   
for i in range(len(keys)):    
    empy1[keys[i]]=a[i]   
    dict["employee1"]=empy1   
    # print(empy1)   
    b=["komal","trainer","24","20000"]   
    for i in range(len(keys)):    
        empy2[keys[i]]=b[i]   
        dict["employee2"]=empy2   
        # print(empy2)   
        c=["anuradha","HR","25","40000"]   
    for i in range(len(keys)):    
        empy3[keys[i]]=c[i]   
        dict["employee3"]=empy3   
        # print(empy3)   
        d=["Abhishek","manager","29","63000"]    
    for i in range(len(keys)):    
        empy4[keys[i]]=d[i]   
        dict["employee4"]=empy4   
        # print(empy4)   
        out_file = open("meraki q8.json", "w")
        json.dump(dict, out_file, indent = 6)
out_file.close()

