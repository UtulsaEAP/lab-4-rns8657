"""
Complete the following python code to reverse the string entered by the user.

Name: Ryan Smith
Lab Time: Thursday @2pm
"""

def reverse_string():
    text = input()
    string = ""
    while (text != "Done" and text!= "done" and text != "d"):
        for i in range (len(text)):
            string += text[len(text) - 1 - i] 
        string += "\n"
        text = input()
    print(string)

    

if __name__ == "__main__":
    reverse_string()