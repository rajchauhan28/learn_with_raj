import time
import turtle
x = turtle.Turtle()
x.speed(70)
l = 70
for i in range (13):
	x.circle(l)
	x.circle(l - 5)
	x.circle(l - 10)
	x.circle(l - 15)
	x.circle(l - 20)
	x.circle(l - 25)
	x.lt(30)
l = l + 5
x.pencolor("red")
for i in range (13):
	x.circle(l)
	x.circle(l - 5)
	x.circle(l - 10)
	x.circle(l - 15)
	x.circle(l - 20)
	x.circle(l - 25)
	x.lt(30)
l = l + 5
x.pencolor("blue")
for i in range (13):
	x.circle(l)
	x.circle(l - 5)
	x.circle(l - 10)
	x.circle(l - 15)
	x.circle(l - 20)
	x.circle(l - 25)
	x.lt(30)
l = l + 5
x.pencolor("green")
for i in range (13):
	x.circle(l)
	x.circle(l - 5)
	x.circle(l - 10)
	x.circle(l - 15)
	x.circle(l - 20)
	x.circle(l - 25)
	x.lt(30)
l = l + 5
x.pencolor("yellow")
for i in range (13):
	x.circle(l)
	x.circle(l - 5)
	x.circle(l - 10)
	x.circle(l - 15)
	x.circle(l - 20)
	x.circle(l - 25)
	x.lt(30)
l = l + 5
x.pencolor("orange")
for i in range (13):
	x.circle(l)
	x.circle(l - 5)
	x.circle(l - 10)
	x.circle(l - 15)
	x.circle(l - 20)
	x.circle(l - 25)
	x.lt(30)
x.width(0)
x.pencolor("black")

x.lt(90)
x.fd(50)
x.width(10)
x.fd(200)
time.sleep(10)