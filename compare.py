def string(s,t):
    i = 0
    new_word = ""
    while i < len(t):
        j = 0
        while j < len(s):
            if t[i]==s[j]:
                new_word = new_word + t[i]
            j = j +1
        i = i + 1
    print(new_word)
string("sunilllssuuiill","usiln")
