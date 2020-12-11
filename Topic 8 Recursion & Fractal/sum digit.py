#Given a non-negative integer n
#return the sum of its digits recursively (without loops).


def sum_numbers(num):
    if num == 0:
        return 0
    return(num %10 + sum_numbers(int(num/10)))

num = 12345
result = sum_numbers(num)
print(result)

