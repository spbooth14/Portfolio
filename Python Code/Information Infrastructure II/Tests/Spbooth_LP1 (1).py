#I211 Lab Practical 1
#Skyler Booth
#Spbooth

#Section 2
passwordList = [line.strip() for line in open("passwords.txt", "r")]

#Section 3
def show_list(lst):
    if len(lst) > 1:
        print("The current possible passwords are:")
        print("-"*30)
        for word in lst:
            print(word)
        print()
        print("(" +str(len(lst)) + " possible)")
    else:
        print("Password Found!")
        print("-"*30)
        for word in lst:
            print(word)
        print()
        print("(" +str(len(lst)) + " possible)")

show_list(passwordList)

#Section 4
#Clue 1
print("Clue 1: The password is atleast 6 characters long.")
print()
clue1 = [word for word in passwordList if len(word) >= 6]
show_list(clue1)

#Clue 2
print("Clue 2: The password contains 1 letter.")
print()
clue2 = [word for word in clue1 \
   if len([let for let in word if let.isalpha()]) > 0]
show_list(clue2)       
#Clue 3
print("Clue 3: The password does not start with a vowel, but the second charater is a vowel.")
print()
clue3 = [word for word in clue2 if word[0].lower() not in "aeiou" and word[1].lower() in "aeiou"]

show_list(clue3) 
#Clue 4
print("Clue 4: The password has atleast twice as many consonants as vowels.")
print()
##clue4 = []
##for word in clue3:
##    vowelCount = 0
##    consonentCount = 0
##    for i in range(len(word)):
##        if word[i] in "aeiou":
##            vowelCount += 1
##        else:
##            consonentCount+= 1
##    if consonentCount > vowelCount*2:
##        clue4.append(word)
        
clue4 = [word for word in clue3\
         if len([word[i] for i in range(len(word)) if word[i] in "aeiou"])*2 < len([word[i] for i in range(len(word)) if word[i] not in "aeiou" and word[i].isalpha()])]
        
show_list(clue4)


#Section 5
#Clue 5
print("Bonus: The password has the same letter twice in a row")
print()
clue5 = [word for word in clue4\
         if len([i for i in range(len(word)-1) if word[i] == word[i+1]])>0]
##for word in clue4:
##    doubleLetterCount = 0
##    for i in range(len(word)-1):
##        if word[i] == word[i+1]:
##            doubleLetterCount +=1
##    if doubleLetterCount>0:
##        clue5.append(word)
    


show_list(clue5)
