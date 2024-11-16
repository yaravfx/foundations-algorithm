# Using recursion to implement power and factorial functions


def power(num, pwr):
    if pwr == 0:
        return 1

    else:
        # multiply the num by the return value of calling the power function again, this time decreasing the power by 1
        return num * power(num, pwr - 1)


print(power(5, 3))



def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)
