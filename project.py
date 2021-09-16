import turtle

shapes = []
t = turtle.Turtle()


class Shape:
    def __init__(self, s_title, s_kind, s_x, s_y, s_dimension1, s_dimension2):
        self.title = s_title
        self.kind = s_kind
        self.x = s_x
        self.y = s_y
        self.dimension1 = s_dimension1
        self.dimension2 = s_dimension2
        self.show = True

    def draw(self):
        if self.show:
            t.color("black")
            t.width(1)
        else:
            t.color("white")
            t.width(2)
        if self.kind == 'c':
            t.penup()
            t.setpos(self.x, self.y)
            t.pendown()
            t.write(self.title)
            t.penup()
            t.setpos(self.x, self.y - self.dimension1)
            t.pendown()
            t.circle(self.dimension1)
        else:
            t.penup()
            t.setpos(self.x, self.y)
            t.pendown()
            t.forward(self.dimension1)
            t.right(90)
            t.forward(self.dimension2)
            t.right(90)
            t.forward(self.dimension1)
            t.right(90)
            t.forward(self.dimension2)
            t.right(90)
            t.penup()
            t.setpos(self.x + self.dimension1 / 2, self.y - self.dimension2 / 2)
            t.pendown()
            t.write(self.title)

    def check_in(self, x, y):
        x1 = self.x
        x2 = x1 + self.dimension1
        y1 = self.y - self.dimension2
        y2 = self.y
        if self.kind == 'c':
            if (x - x1)**2 + (y - y2)**2 < self.dimension1 ** 2 and self.show:
                return True
            return False
        if x > x1 and  x < x2 and y > y1 and y < y2 and self.show:
            return True
        return False

    def change(self):
        self.show = not self.show
        self.draw()


def getfilename():
    filename = input("enter file name ")

    try:
        ff = open(filename)
        ff.close()
        return filename
    except FileNotFoundError:
        print('File does not exist')
        return getfilename()


def draw():
    global shapes
    for shape in shapes:
        shape.draw()


def click(x, y):
    global shapes
    ch = 0
    for shape in shapes:
        if shape.check_in(x, y):
            windows.title(shape.title)
            ch = 1
            break
    if ch == 0:
        windows.title("outside")


def readfile():
    global shapes
    shapes = []
    file = getfilename()
    with open(file, 'r') as f:
        s = f.read()
        lines = s.split('\n')
        for i in range(len(lines)):
            line = lines[i].split(' ')
            title = line[0]
            x = int(line[1])
            y = int(line[2])
            kind = line[3]
            dimension1 = int(line[4])
            if kind == 'r':
                dimension2 = int(line[5])
            else:
                dimension2 = dimension1
            shape = Shape(title, kind, x, y, dimension1, dimension2)
            shapes.append(shape)


def change(title):
    global shapes
    for shape in shapes:
        if shape.title == title:
            shape.change()
            break


def key0():
    change('0')


def key1():
    change('1')


def key2():
    change('2')


def key3():
    change('3')


def key4():
    change('4')


def key5():
    change('5')


def key6():
    change('6')


def key7():
    change('7')


def key8():
    change('8')


def key9():
    change('9')


def keyn():
    windows.clear()
    start()


def start():
    readfile()
    windows.setup(800, 600)
    windows.title(" ")
    draw()
    windows.listen()
    windows.onscreenclick(click, 1)
    windows.onkey(key0, '0')
    windows.onkey(key1, '1')
    windows.onkey(key2, '2')
    windows.onkey(key3, '3')
    windows.onkey(key4, '4')
    windows.onkey(key5, '5')
    windows.onkey(key6, '6')
    windows.onkey(key7, '7')
    windows.onkey(key8, '8')
    windows.onkey(key9, '9')
    windows.onkey(keyn, 'n')
    windows.onkey(keyspace, 'space')


def keyspace():
    windows.bye()


windows = turtle.Screen()
start()
windows.mainloop()
