def adjacentElementsProduct(inputArray):
    i = 0
    maximum = inputArray[0]*inputArray[1]
    while i  < len(inputArray)-1:
        product= inputArray[i]*inputArray[i+1]
        print(product)
        if maximum < product:
            maximum = product    
        i = i+1
    return (maximum)
print(adjacentElementsProduct([1,0,1,0,199]))