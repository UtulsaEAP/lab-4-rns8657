"""
Complete the following python code to print all numbers between the two values incrementing by 5 from the initial value to the final value. The initial value and final value are entered by the user. If the final value is less than the initial value, print "Second integer can't be less than the first.

Name: Ryan Smith
Lab Time: Thursday @2pm
"""

def inc_5():
    num1 = int(input())
    num2 = int(input())
    string = str(num1) 

    if (num2 >= num1):
        while(num2 > num1):
            num1 += 5
            string += " " + str(num1) 
        print(string)
    else:
        print("Second integer can't be less than the first.")
        


    



if __name__ == '__main__':
    inc_5()