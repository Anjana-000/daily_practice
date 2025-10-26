'''6
1 90 34 89 7 9 
[1, 7, 9, 90, 89, 34]
'''



n=int(input())
arr=list(map(int,input().split()))
arr.sort()
mid=n//2
f_half=arr[:mid]
s_half=arr[mid:][::-1]
print(f_half+s_half)
