# import random
# # word=["bear","pizza","snack","washington","moon"]
# # max_wrong=

# word="secret"
# allowed_error=7
# guesses=[]
# done=False
# while not done:
#     for letter in word:
#         if letter.lower() in guesses:
#             print(letter,end=" ")
#         else:
#             print("_",end=" ")
#     print("")
#     # done=True
#     guess=input(f"allowed errors left{allowed_error},next guess: ")
#     guesses.append(guess.lower())
#     if guess.lower() not in word.lower():
#         allowed_error-=1
#         if allowed_error==0:
#             break
#     done=True
#     for letter in word:
#         if letter.lower() in guesses:
#             done=False
# if done:
#     print("you found the word! it was{word}")
# else:
#     print(f"guess over the word was{word}")





# word=list("apple")
# hidden=[]
# for chr in word:
#     hidden.append('_')

# attems=0
# max_attems=4

# isGameOver=False
# while not isGameOver:
#     print(f"you have{attems}attems remaining")
#     hiddenstrint=' '.join(hidden)
#     print(f"the current word is:{hiddenstrint} ")
#     print("     ------")
#     print("     |     |")
#     print("     |     ")
#     print("     |     ")
#     print("     |     ")
#     print("     |     ")
#     print("-----------")

#     break
#     # print(word)
#     # print(hidden)
