def add_two_numbers(number_1,number_2):
    i = 0
    while i < len(number_1):
        print("The sum of two numbers are"+" "+str(number_1[i]+number_2[i]))
        i = i + 1
add_two_numbers([10,20,30],[20,30,40])