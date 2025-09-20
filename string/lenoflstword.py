def lengthOfLastWord(s):
    length = 0
    s = s.strip()
    for i in range(len(s)-1, -1, -1):   # go from end to start
        if s[i] == " ":                # stop if we hit a space
            break
        else:
            length += 1                 # count characters
    return length
