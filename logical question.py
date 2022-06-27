# a=[3,0,1,2,6,5,7,9]
# i=0
# b=[]
# max=0
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#         b.append(max)
#     else:
#         b.append(max)
#     i+=1
# print(b)




# a=[3,7,1,2,6,5,6,9]
# min=a[0]
# i=0
# while i<len(a):
#     if a[i]<min:
#         min=a[i]
#     i+=1
# print(min)

# a=[1,1,0,1,1,1,0,1]
# i=0
# b=[]
# while i<len(a):
#     c=0
#     c1=0
#     j=0
#     while j<len(a):
#         if a[j]==0 and j<i:
#             c+=1
#         if a[j]==1 and j>=i:
#             c1+=1
#         j+=1
#     k=c1+c
#     b.append(k)
#     i+=1
# print(b)



# a=[1,1,0,1,1,1,0,1]
# i=0
# b=[]
# while i<len(a):
#     c=0
#     j=0
#     while j<len(a):
#         if a[j]==0 and j<i:
#             c+=1
#         j+=1
#     b.append(c)
#     i+=1
# print(b)



# a=[1,1,0,1,1,1,0,1]
# i=0
# b=[]
# while i<len(a):
#     c=0
#     c1=0
#     j=0
#     while j<len(a):
#         if a[j]==0 and j<i:
#             c+=1
#         if a[j]==1 and j>=i:                                                                                                            
#             c1+=1
#         j+=1
#     k=c1+c
#     b.append(k)
#     i+=1
# print(b)

# i=5
# while i>=1:                             
#     j=5
#     while j>=i:
#         print(i,end=" ")
#         j-=1
#     print()
#     i-=1


# a=[3,7,8,9,4,5,6,2,1]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     if a[i]%2==0:
#         b.append(a[i])
#     else:
#         c.append(a[i])
#     i+=1
# print("even number",b)
# print("odd number",c)



# a=[3,7,8,9,4,5,6,2,1]
# i=0
# sum=0
# while i<len(a):
#     sum+=a[i]
#     i+=1
# print(sum)



# a={"a":9,"b":5,"c":4,"d":8}
# i=0
# sum=0
# for i in a.values():
#     sum=sum+i
# print(sum)


# a=["a","b","c","d"]
# b=[100,200,300,400]                 #output:-{"a":100,"b":200,"c":300,"d":400}
# c={}
# for x in range(len(a)):
#     c.update({a[x]:b[x]})
# print(c)



# age=int(input("enter the age:-"))
# if age>=18:
#     var=input("go to collage or not:-")
#     if var=="yes":
#         collage=input("which collage:-")
#         field=input("which field:-")
#         if field=="science":
#             print("2 year after get job")
#         elif field=="art":
#             print("after 3 years get job")
#         elif field=="math":
#             print("1.50 year after get job ")
#     elif var=="no":
#         marraige=input("are you married:-")
#         if marraige=="yes":
#             type=input("which type of marrage:-")
#             if type=="love marrage":
#                 place=input("which place:-")
#                 if place=="temple":
#                     print("god bless you")
#                 elif place=="court":
#                     print("friend circle")
#             elif type=="arreng marrage":
#                  print("happy ending")
#         elif marraige=="no":
#             print("enjoy your self")
# elif age<=18:
#     var1=input("are you go to school or not:-")
#     age2=int(input("enter thr age"))
#     if var1=="yes":
#         if age2>10:
#             subject=input("enter the subject:-")
#             if subject=="science" or "math" or "art":
#                print("its nice field")
#         elif age2<10:
#             print("good")
#     elif var1=="no":
#         print("do your study")
# else:
#     print("invalid")





# a=[1,2,3,4,5,6,7,8,9,10]
# i=0
# b=[]
# while i<len(a):
#     c=a[i]**2
#     b.append(c+1)
#     i+=1
# print(b)



# k=1
# i=1
# while i<=5:
#     b=1
#     while b<=5-i:
#         print(" ",end=" ")
#         b=b+1
#     j=1
#     while j<=k:
#         print("*",end="  ")
#         j=j+1
#     k=k+1
#     print()
#     i=i+1

# i=1
# while i<=100:
#     if i%3==0 and i%7==0:
#         print("navgurukul") 
#     elif i%3==0:
#         print("nav")
#     elif i%7==0:
#         print("gurukul")
#     else:
#         print(i)
#     i+=1

#     num=int(input("enter the number  "))
#     sum+=num
#     i+=1
# print(sum)