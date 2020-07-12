def palindrome(name):
    reverse_name = ""
    length = len(name)
    index = length - 1
    while(index >= 0):
        reverse_name = reverse_name + name[index]
        index = index - 1
    print(name)
    print(reverse_name)
    if name == reverse_name:
        palindrome = "Its a palindrome"
    else:
        palindrome = "Its not a palindrome"
    return(palindrome)
print(palindrome("nnan"))
