'''Write a Python program to read a list of integers from the user and find the maximum and minimum values in the list without using built-in functions like max() or min().
Use loops and comparisons to find the result.'''

a=list(map(int,input().split()))
maxx=a[0]
minn=a[0]
l=len(a)
for i in range(1,l):
    if a[i]>maxx:
        maxx=a[i]
        
    if a[i]<minn:
        minn=a[i]
print(maxx)
print(minn)
