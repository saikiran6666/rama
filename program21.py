#program on movement of robot
import math
# l=[0,0]
# while True:
#     s=input()
#     if not s:
#         break
#     move=s.split(" ")     #move=['up','5']
#     direction=move[0]
#     step=int(move[1])
#     if direction=='up':
#         l[0]+=step
#     elif direction=='down':
#         l[0]-=step
#     elif direction=='left':
#         l[1]-=step
#     elif direction=='right':
#         l[1]+=step
#     else:
#         pass
#  print(l[0 ])
# print(l[1])
# print(int(math.sqrt(l[1]**2+l[0]**2)))



import math
l=[0,0]
while True:
    s=input()
    if not s:
        break
    move = s.split(" ")
    direction=move[0]
    step=int(move[1])
    if direction=='up':
        l[0]+=step
    elif direction=='down':
        l[0]-=step
    elif direction=='left':
        l[1]-=step
    elif direction=='right':
        l[1]+=step
    else:
        pass
print(l[0])
print(l[1])
print(int(round(math.sqrt(l[1]**2+l[0]**2))))