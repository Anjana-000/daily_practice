'''

Question 4
Given an array. Select the alternative elements in the array starting from second position. Reverse these elements and place them in the array

For example
Input : 1 5 6 7 8 9 0
Output : 1 9 6 7 8 5 0
'''

n=list(map(int,input().split()))
j=0
alternate=n[1::2][::-1]
for i in range(1,len(n),2):
    n[i]=alternate[j]
    j+=1
print(n)
