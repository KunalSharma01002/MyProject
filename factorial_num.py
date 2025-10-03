
def factorial_num(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
result = factorial_num(num)
print('Factorial number',num,'is:',result)







