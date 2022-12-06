def isprime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def iseven(n):
    if n%2==0:
        return True
    else:
        return False
    
def ispositive(n):
    if n>=0:
        return True
    else:
        return False
    
A=int(input("Enter A value: "))
B=int(input("Enter B value: "))
C=int(input(f"Enter a value between {A} and {B}: "))
while C > B or C < A:
        C=int(input(f"Enter a value between {A} and {B}: "))
print("The properties followed by this number are: ")
if isprime(C):
    print(f"{C} is a prime number")
else:
    if C==1:
        print(f"{C} is neighter prime nor composite")
    else:
        print(f"{C} is a composite number")
if iseven(C):
    print(f"{C} is an even number")
else:
    print(f"{C} is an odd number")
if ispositive(C):
    print(f"{C} is a positive number")
else:
    print(f"{C} is a negative number")