def product(numbers):
    i = 0
    product = 1
    while i < len(numbers):
        product = product * numbers[i]
        i = i + 1
    return(product)
print(product([1,2,3,4]))
