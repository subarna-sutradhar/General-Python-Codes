"""To check if given number is prime is not METHOD: 1"""
num = int(input("Enter a number: "))
#if a given number is greater than 1
ans = input("CONTINUE?...")
while(ans == "y"):
    if num > 1:
        """Iterate from 2 to n / 2"""
        for i in range(2, num // 2):
            """If num is divisible by any number between
            2 and n / 2, it is not prime"""
            if(num % 1) == 0:
                print(num, "is not a prime number")
                break

        else:
            print(num, "is a prime number")

    else:
        print(num, "is not a prime number")

    num = int(input("Enter a number: "))
    ans = input("CONTINUE?...")
    