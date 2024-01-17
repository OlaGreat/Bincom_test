
def fibbonacci(number):
    if number ==1 or number == 0:
        return number
    else:
        return fibbonacci(number-1) + fibbonacci(number-2)


print(fibbonacci(5))
