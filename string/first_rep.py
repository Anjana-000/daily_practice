def firstrep(s):
    seen = set()       # create an empty set to store characters we've already seen
    for i in s:        # loop through each character in the string
        if i in seen:  # check if we've seen this character before
            return i   # if yes, this is the first repeating character → return it
        seen.add(i)    # otherwise, add it to the set
    return None        # if no repeats found after the loop, return None
