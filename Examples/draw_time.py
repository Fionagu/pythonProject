import turtle, time


def draw_gap():
    turtle.penup()
    turtle.fd(5)


def draw_line(draw):
    draw_gap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    draw_gap()
    turtle.right(90)

def draw_digit(digit):
    draw_line(True) if digit in [2,3,4,5,6,8,9] else draw_line(False)
    draw_line(True) if digit in [0,1,3,4,5,6,7,8,9] else draw_line(False)
    draw_line(True) if digit in [0,2,3,5,6,8,9] else draw_line(False)
    draw_line(True) if digit in [0,2,6,8] else draw_line(False)
    turtle.left(90)
    draw_line(True) if digit in [0,4,5,6,8,9] else draw_line(False)
    draw_line(True) if digit in [0,2,3,5,6,7,8,9] else draw_line(False)
    draw_line(True) if digit in [0,1,2,3,4,7,8,9] else draw_line(False)
    turtle.left(180)   
    turtle.penup()
    turtle.fd(20)

def draw_date(date):
    for i in date:
        draw_digit(eval(i))


def draw_system_date(date): #data 为日期，格式为 '%Y-%m=%d+
    turtle.pencolor('red')
    for i in date:
        if i == '-':
            turtle.write('年', font=('Aria', 18, 'normal'))
            turtle.pencolor('green')
            turtle.fd(40)
        elif i == '=':
            turtle.write('月', font=('Aria', 18, 'normal'))
            turtle.pencolor('blue')
            turtle.fd(40)
        elif i == '+':
            turtle.write('日', font=('Aria', 18, 'normal'))
        else:
            draw_digit(eval(i))


def main():
    turtle.setup(800, 350, 200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    draw_system_date(time.strftime('%Y-%m=%d+', time.gmtime()))
    # draw_date('20200325')
    turtle.hideturtle()
    turtle.done()

main()