'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
mouseboi = turtle.Turtle()
mouseboi.shape('turtle')

mouseboi.begin_fill()
mouseboi.color('grey')
mouseboi.penup()
mouseboi.goto(30,-150)
mouseboi.pendown()
mouseboi.circle(110)
mouseboi.end_fill()
mouseboi.penup()

mouseboi.begin_fill()
mouseboi.penup()
mouseboi.goto(-80,20)
mouseboi.pendown()
mouseboi.circle(50)
mouseboi.end_fill()
mouseboi.penup()

mouseboi.goto(100,50)
mouseboi.pendown()
mouseboi.begin_fill()
mouseboi.circle(50)
mouseboi.end_fill()
mouseboi.penup()

mouseboi.goto(95,55)
mouseboi.pendown()
mouseboi.begin_fill()
mouseboi.color('pink')
mouseboi.circle(20)
mouseboi.end_fill()
mouseboi.penup()

mouseboi.goto(-73,30)
mouseboi.pendown()
mouseboi.begin_fill()
mouseboi.color('pink')
mouseboi.circle(20)
mouseboi.end_fill()
mouseboi.penup()

mouseboi.goto(-27,0)
mouseboi.pendown()
mouseboi.begin_fill()
mouseboi.color('black')
mouseboi.circle(8)
mouseboi.end_fill()
mouseboi.penup()

mouseboi.goto(65,0)
mouseboi.pendown()
mouseboi.begin_fill()
mouseboi.color('black')
mouseboi.circle(8)
mouseboi.end_fill()
mouseboi.penup()

mouseboi.goto(65,-100)
mouseboi.pendown()
mouseboi.backward(90)
mouseboi.forward(50)
mouseboi.penup()

mouseboi.goto(200,200)



turtle.exitonclick() #Keeps pycharm window open
