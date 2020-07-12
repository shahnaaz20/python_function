def maximum(list):  
    i = 0
    max = 0
    while i < len(list):
        if list[i]>max:
            max = list[i]
        i = i + 1
    return(max)
print(maximum([2,3,56,4,5,7]))