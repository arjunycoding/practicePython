print("Welcome! If you are having trouble finding if a number is prime or composite you've come to the right place!")
number = int(input("Chosse a number and we will find out if it is prime or composite!\n"))
possibleNumbers = []
factors = []
def sive(num):
    i = 0
    while i <= num:
        possibleNumbers.append(i)
        i += 1
    i = 1
    while i <= num:
        if(num % possibleNumbers[i] == 0):
            factors.append(possibleNumbers[i])
        i+=1
    if(factors == [1, num]):
        print(f"{number} is a prime number")
    else:
        print(f"{number} is a composite number")
sive(number)
print(f"Here is your all the factors for the number {number}:", factors)