import turtle 
from turtle import *

# def stars():
#     turtle.pensize(3)
#     turtle.speed(5)
#     for i in range(300):
#         circle(190-i,90)
#         left(90)
#         circle(190-i,90)
#         left(200)
# stars()
# mainloop()

#modifications 
def flower():
    pensize(2)
    speed(50)
    for i in range(150):
        circle(190-i,90)
        left(90)
        circle(190-i,90)
        left(60)
flower()
mainloop()
