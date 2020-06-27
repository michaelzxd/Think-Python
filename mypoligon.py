
import turtle
import math

bob = turtle.Turtle()

def polygon(t,n,length):
	angle = 360/n
	for i in range(n):
		bob.fd(length)
		bob.lt(angle)

def circle(t,r):
	circumference = 2 * math.pi * r
	n= int(circumference/3) + 3
	length = circumference / n
	polygon(t,n,length)

circle(bob,80)
turtle.mainloop()