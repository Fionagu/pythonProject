#V1
import turtle


def koch(size,n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)

# 科赫曲线的绘制
def draw_1():
    turtle.setup(800,400)
    turtle.penup()
    turtle.goto(-300,-50)
    turtle.pendown()
    turtle.pensize(2)
    koch(600,3) # 3阶科赫曲线
    turtle.hideturtle()


# 科赫雪花的绘制
def draw_2():
    turtle.setup(600,600)
    turtle.penup()
    turtle.goto(-200,100)
    turtle.pendown()
    turtle.pensize(2)
    level = 3
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.hideturtle()


# draw_1()
draw_2()