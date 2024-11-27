# make a function to check whether number is armstrong or not 
def is_armstrong(num):
    power=len(str(num))
    return num==sum(int(digit)**power for digit in str(num))
print("Is Armstrong:",is_armstrong(153))