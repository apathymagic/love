# l2=[]
# for y in range(15,-15,-1):
#     l3 = []
#     for x in range(-30,30):
#         l3.append((' I love U'[(x-y)%9]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' '))
#     l2.append(''.join(l3))
# l1 ='\n'.join(l2) 

# for i in l1:
#     print("\033[91m"+i,end="",flush=True)

import turtle as p
p.setup(500,500)   
p.pencolor('red')
p.pensize(2)
p.penup()
p.goto(0,60)
p.begin_fill()
p.fillcolor('pink')
p.pendown()
p.left(135)
p.circle(42.3,180)
p.goto(0,-60)
p.left(90)
p.goto(60,0)
p.circle(42.3,180)
p.end_fill()
p.penup()
p.goto(250,250)
p.done()