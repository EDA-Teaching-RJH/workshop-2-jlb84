import math  

def main():
    A = int(input("Enter the length of side A: "))
    B = int(input("Enter the length of side B: "))
    C = pythag(A, B)
    
    print("The length of the hypotenuse is: ", C)

def pythag(A,B):
    C = math.sqrt(A ** 2 + B ** 2)
    return C

main()
