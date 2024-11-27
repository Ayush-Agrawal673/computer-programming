 #Check if a number is a perfect number
def is_perfect_number(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

print("Is Perfect Number:", is_perfect_number(28))