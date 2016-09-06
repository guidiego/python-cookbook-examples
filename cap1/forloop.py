s = "a string to examine"
for i in range(len(s)):
    for j in range(i+1, len(s)):
        if s[i] == s[j]:
            answer = (i, j)
