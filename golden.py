n = int(input("how many triangle: "))
def goldenRectangle(l,h):
    if l/h>=1.6 and l/h<=1.7:
        return "it is goldenrectangle (" + str(l)+","+str(h) + ")"
while n > 0:
    l  = int(input("lenght : "))
    w = int(input("width: "))
    print(goldenRectangle(l,w))
    n = n - 1
