# write a python function that return nth fibonaaci number
def fibonaaci(n):
    if n== 0:
        return 0
    elif n== 1:
        return 1 
    else:
        return fibonaaci(n-1)+fibonaaci(n-2)

print("Fibonaaci of 10 is ",fibonaaci(10))