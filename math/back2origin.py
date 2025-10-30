'''
657. Robot Return to Origin
Given a sequence of moves ('L', 'R', 'U', 'D'), determine if the robot returns
to the origin (0, 0) after performing all moves.

Example 1:
Input: moves = "UD"
Output: True
Explanation:
The robot moves up once and down once, returning to the origin.

Example 2:
Input: moves = "LL"
Output: False
Explanation:
The robot ends at (-2, 0), not the origin.
'''

def return_to_origin(moves):
    l,r,u,d=0,0,0,0
    for i in moves:
        if i=="L":
            l+=1
        elif i=="R":
            r+=1
        elif i=="U":
            u+=1
        else:
            d+=1
    return l==r and u==d        

moves = input()
print(return_to_origin(moves))
