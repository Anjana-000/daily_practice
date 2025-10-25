'''prime between two limit'''

l=int(input())
u=int(input())

for num in range(l,u+1):
    if num>1:
        for i in range(2,int(num**0.5)+1):
            if num%2==0:
                break;
        else:
            print(num,end=' ')
        
