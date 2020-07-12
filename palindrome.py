def checkPalindrome(inputString):
    reverse_name = ""
    length = len(inputString)
    index = length - 1
    while(index >= 0):
        reverse_name = reverse_name + inputString[index]
        index = index - 1
    if reverse_name==inputString:
        answer = True
    else:
        answer = False
    return (answer)
print(checkPalindrome("aabaa"))