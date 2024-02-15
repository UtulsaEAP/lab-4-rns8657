"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name:
Lab Time:
"""

def password_mod():
    word = input()
    password = ''
    for i in range (len(word)):
        if (word[i] == "i"):
            password += "1"
        elif (word[i] == "a"):
            password += "@"
        elif (word[i] == "m"):
            password += "M"
        elif (word[i] == "B"):
            password += "8"
        elif (word[i] == "s"):
            password += "$"
        else:
            password += word[i]
    print(password + "!")

if __name__ == "__main__":
    password_mod()