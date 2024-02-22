"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Ryan Smith
Lab Time: Thursday @2pm
"""

def norm():
    #ksldjfklsdjflk
    pass
    repeat = int(input())
    numbers = []

    for i in range (repeat):
        number = float(input())
        numbers.append(number)
    
    maximum = max(numbers)
    for i in range(repeat):
        print(f'{numbers[i] / maximum:.2f}' )

if __name__ == "__main__":
    norm()