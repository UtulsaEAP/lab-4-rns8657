"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Ryan Smith
Lab Time: Thursday @2pm

"""


def reverse_binary():
    user_num = int(input())
    string = ""
    while (user_num > 0):
        string += str(user_num % 2)
        user_num = user_num // 2
    print(string)

if __name__ == "__main__":
    reverse_binary()