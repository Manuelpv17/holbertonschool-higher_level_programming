#!/usr/bin/python3
"""class will be the “base” of all 
other classes in this project
"""
import json
import csv
import turtle


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        j = "[]"
        if list_dictionaries:
            j = json.dumps(list_dictionaries)
        return j

    @classmethod
    def save_to_file(cls, list_objs):
        l = []
        for obj in list_objs:
            d = obj.to_dictionary()
            l.append(d)
        j = cls.to_json_string(l)
        with open(cls.__name__ + ".json", mode="w", encoding="utf-8") as f:
            f.write(j)

    @staticmethod
    def from_json_string(json_string):
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        l = []
        try:
            with open(cls.__name__ + ".json", mode="r", encoding="utf-8") as f:
                j = f.read()
        except:
            return l

        s = cls.from_json_string(j)
        for elm in s:
            l.append(cls.create(**elm))
        return l

    @classmethod
    def save_to_file_csv(cls, list_objs):
        s = ""
        for obj in list_objs:
            s += obj.to_csv() + "\n"
        with open(cls.__name__ + ".csv", mode="w", encoding="utf-8") as f:
            f.write(s)

    @classmethod
    def load_from_file_csv(cls):
        l = []
        with open(cls.__name__ + ".csv", mode="r", encoding="utf-8", newline='') as f:
            read = csv.reader(f)
            for elm in read:
                for i, value in enumerate(elm):
                    elm[i] = int(value)
                l.append(cls.create_csv(*elm))
        return l

    @classmethod
    def create_csv(cls, *array):
        dummy = cls(1, 1)
        dummy.update(*array)
        return dummy

    @staticmethod
    def print_turtle(obj, t, xx, yy):
        t.hideturtle()
        t.penup()
        t.goto(xx, yy)
        t.showturtle()
        t.pendown()
        t.shapesize(1/3)
        t.shape("square")
        t.color("black", "blue")

        x = turtle.Turtle(visible="False")
        x.hideturtle()
        y = turtle.Turtle(visible="False")
        y.hideturtle()
        x.penup()
        x.setpos(xx, yy)
        x.pendown()
        y.penup()
        y.setpos(xx, yy)
        y.pendown()
        x.pensize(3)
        y.pensize(3)
        x.showturtle()
        y.showturtle()
        x.forward(140)
        x.write("x", font=("Arial", 8, 'normal', 'bold'))
        y.left(90)
        y.forward(140)
        y.write("y", font=("Arial", 8, 'normal', 'bold'))

        t.penup()
        t.forward(obj.x)
        t.left(90)
        t.forward(obj.y)
        t.left(-90)
        t.pendown()

        t.begin_fill()
        t.forward(obj.width)
        t.left(90)
        t.forward(obj.height)
        t.left(90)
        t.forward(obj.width)
        t.left(90)
        t.forward(obj.height)
        t.end_fill()

        p_y = turtle.Turtle(visible="False")
        p_y.penup()
        p_y.hideturtle()
        p_y.goto(xx - 15, yy + obj.y)
        p_y.write(str(obj.y))
        p_y.forward(15)
        for i in range(0, obj.x, 5):
            if i % 10 == 0:
                p_y.pendown()
                p_y.forward(5)
            else:
                p_y.penup()
                p_y.forward(5)

        p_x = turtle.Turtle(visible="False")
        p_x.penup()
        p_x.hideturtle()
        p_x.goto(xx + obj.x, yy - 16)
        p_x.write(str(obj.x))
        p_x.left(90)
        p_x.forward(16)
        for i in range(0, obj.y, 5):
            if i % 10 == 0:
                p_x.pendown()
                p_x.forward(5)
            else:
                p_x.penup()
                p_x.forward(5)

        name = turtle.Turtle(visible="False")
        name.penup()
        name.hideturtle()
        name.goto(xx, yy - 28)
        name.write(obj, font=("Arial", 8, 'normal', 'bold'))

    @staticmethod
    def draw(list_rectangles, list_squares):
        turtle.Screen().setup(width=800, height=600)
        turtle.Screen().title("Let's draw it  :)")

        x = -290
        y = 80
        titleRec = turtle.Turtle(visible="False")
        titleRec.hideturtle()
        titleRec.penup()
        titleRec.setposition(x + 220, y + 180)
        titleRec.write("Rectangles", font=("Arial", 20, 'normal', 'bold'))
        titleRec.pendown()
        for rec_obj in list_rectangles:
            Base.print_turtle(rec_obj, turtle.Turtle(visible="False"), x, y)
            x += 220
        x = -290
        y -= 280
        titleSqu = turtle.Turtle(visible="False")
        titleSqu.hideturtle()
        titleSqu.penup()
        titleSqu.setposition(x + 220, y + 180)
        titleSqu.write("Squares", font=("Arial", 20, 'normal', 'bold'))
        titleSqu.pendown()
        for square_obj in list_squares:
            Base.print_turtle(square_obj, turtle.Turtle(visible="False"), x, y)
            x += 220

        turtle.done()
