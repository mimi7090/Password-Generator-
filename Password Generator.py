import random
import string
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation
all_character = letters + numbers + symbols
while True :
    length = int(input("How long should your password be? :"))
    if length <= 0 :
        print("Please enter a positive number")
    else :
        password = ""
    for i in range(length) :
         password += random.choice(all_character)
    print("Your password is :",password)
    again = input("Do you want to generate another password?(yess/no) :").lower()
    if again != "yes" :
        print("Thanks for using password generator!")
        break
