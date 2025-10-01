start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

print("Prime numbers between", start, "and", end, "are:")

# Loop through the range
if start > end:
    start, end = end,start
    for num in range(start, end + 1):
        if num > 1:  # primes are greater than 1
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(num)