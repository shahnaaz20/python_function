def prime(number):
    a = 2
    while a < number:
	    if number%a==0:
		    return number,"its not a prime number"
		    break
	    else:
		    return number,"its a prime number"
		    break
	    a = a + 1
print(prime(45))