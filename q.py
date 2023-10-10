













































# import turtle
# turtle.bgcolor("black")

# pentagon = turtle.Turtle()
# pentagon.speed(45)
# pentagon.pencolor("cyan")
# for i in range(900):
#     pentagon.forward(i)
#     pentagon.left(9999)














# import turtle
# import colorsys
# t = turtle.Turtle()
# s = turtle.Screen().bgcolor('black')
# t.speed(0)
# n = 70
# h = 0
# for i in range(360):
#     c = colorsys.hsv_to_rgb(h, 1, 0.8)
#     h+= 1/n
#     t.color(c)
#     t.left(1)
#     t.fd(1)
#     for j in range(2):
#         t.left(2)
#         t.circle(220)



















from turtle import*
import colorsys
speed(45)
hideturtle()
bgcolor("black")
tracer(5)
width(2)
h=0.01
for i in range(55):
	color(colorsys.hsv_to_rgb(h,1,1))
	forward(100)
	left(60)
	forward(100)
	right(120)
	circle(50)
	left(240)
	forward(100)
	left(60)
	forward(100)
	h+=0.02
	color(colorsys.hsv_to_rgb(h,1,1))
	forward(100)
	left(60)
	forward(100)
	right(120)
	circle(-50)
	left(240)
	forward(100)

	left(60)
	forward(100)
	left(2)
	h+=0.02
done()




















# doniyorcalc = input("Enter an operator (+ - * /): ")
# num1 = float(input("birinchi sonni kirit: "))
# num2 = float(input("ikkinchi sonni kirit: "))
# if doniyorcalc == "+":
#     result = num1 + num2
#     print(round(result, 3))
# elif doniyorcalc == "-":
#     result = num1 - num2
#     print(round(result, 3))
# elif doniyorcalc == "*":
#     result = num1 * num2
#     print(round(result, 3))
# elif doniyorcalc == "/":
#     result = num1 / num2
#     print(round(result, 3))
# else:
#     print(f"[doniyorcalc] is not find valid  doniyorcalc")

























# import turtle
# from turtle import*
# speed(4567)
# color("red")
# bgcolor("black")
# b = 200
# while b > 0:
#     left(4467)
#     forward(b*3)
#     b = b - 1








































