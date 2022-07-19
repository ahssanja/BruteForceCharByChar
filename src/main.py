import string
import time

print("Enter your password")

password = input()
word = ""
index = 0

dict = ["1","2","3","4","5","6","7","8","9","0"] + list(string.ascii_lowercase) + list(string.ascii_uppercase)

while(word != password):
    for char in dict:
        print(word + char)
        time.sleep(0.03)
        if(char == password[index]):
            word = word + char
            index = index + 1
            break

print("\npassword is " + word)
