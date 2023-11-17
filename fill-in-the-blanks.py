score1=0
score2=0
score3=0
score4=0

print("Fill in the blanks :")

print("Who is the handsome boy in erode________ ?")
answer=input("Enter your answer:")
if answer == "Vicky":
    print("you are correct")
    score1 =+1
else:
    print("you are wrong")


print("capital of India is ______ ?")
answer=input("Enter your answer:")

if answer == "Delhi":
    print("you are correct")
    score2 =+1
else:
    print("you are wrong")
  
print("capital of Tamilnadu is ______ ?")
answer=input("Enter your answer:")

if answer == "Chennai":
    print("you are correct")
    score3 =+1
else:
    print("you are wrong")
    

print("Erode is famous for________ ?")
answer=input("Enter your answer:")

if answer == "Turmeric":
    print("you are correct")
    score4 =+1
else:
    print("you are wrong")


   


total_score = score1 + score2 + score3 + score4
print("Total you scored:", total_score,"/4")
