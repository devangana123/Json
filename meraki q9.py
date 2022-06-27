# # Apki pass ek shopping name ki ek dictionary hai
# # {
# #     "shopping_list":
# #         { 
# #             "chaco":"15",
# #             "Biscuits":"50",
# #             "Diary_milk":"30",
# #             "ice_cream":"20",
# #         } 
# # }
# # Apki dictionary ka use kar ke ek json file create karna hai.
# # Aur apko kuch task perform karne hai jaise ki
# # main dekhna chahta hu shopping list ko json file dekhna.
# # phir main user se poochu ga ki kon sa item khareedna chahte ho.
# # uske baad user name dega phir user se input poochege jaise ki tum kitne item chahte ho.
# # phir aapka wo number of items json file se remove karna hai.
# # Agar tumhe shopping items add karna hai to tumko json file main insert karna hoga.
# # Output:-
# # show shopping_list:- 
# # {
# #     "shopping_list":{ 
# #         "chaco":"15",
# #         "Biscuits":"50",
# #         "Diary_milk":"30",
# #         "ice_cream":"20",
# #          } 
# # }


import json
A = {"shopping_list":
        { 
            "choco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
 }
J = input("enter a item :")
S = int(input("enter the quantity :"))
for i in A :
    for j in A[i]:
        if J in A[i] :
            if j == J and int(A[i][j])>=S:
                print(A[i][j])
                b = int(A[i][j]) + S
                A[i][j] = str(b)
                break
        elif j != J:
          print("Not available")
          break

with open("data1.json","w") as write_file:  
    json.dump( A, write_file , indent=4)  
with open("data1.json", "r") as read_file:  
    c =  read_file.read() 
print(c)
# print(type(c))
























# x = pow(4, 3)
# print(x)

# x = abs(-7.25)
# print(x)

# x = min(5, 10, 25)
# y = max(5, 10, 25)
# print(x)
# print(y) 


# import math
# x = math.sqrt(64)
# print(x) 


# x = math.ceil(1.4)
# y = math.floor(1.4)

# print(x) # returns 2
# print(y) # returns 1 



# import math
# x = math.pi
# print(x) 

# i=0
# while i<=10:
#     i+=1
#     if i==5 and i==7:
#         continue
#     print(i)
#         # continue



# i=0
# while i<=10:
#     if i==5 :
#         break
#     i+=1
#     print(i)

# i=10
# while i>=1:
#     print(i)
#     i=i-1




# import json
# a=open("login.json","w")
# a.write("")
# a.close()