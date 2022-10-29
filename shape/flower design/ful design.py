from asyncio import sleep
from turtle import*
from turtle import*

def fleur():
    for i in range (300):
    
        circle(190-i,90)
        sleep(0.01)
        circle(190-i,90)
        circle(50-i,90)
        left(90)
        circle(190-i,90)
        left(18)
        

fleur()
mainloop()       