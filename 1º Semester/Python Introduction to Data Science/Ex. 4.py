def fact(number):
    factorial = 1
    for n in range(number, 0, - 1):
        factorial *= n
        if n > 1:
            print(n, end=" * ")
        else:
            print(n, end=" = ")
    print(factorial)

number = int(input("Type a number: "))
print(f"the factorial of {number} is:")
fact(number)
