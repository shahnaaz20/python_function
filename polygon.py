def shapeArea(n):
    i = 1
    sum = 0
    while i < n*2:
        if i%2!=0:
            a = i
            sum = sum + i
        i = i + 1
    print(sum+(sum-a))
shapeArea(2)