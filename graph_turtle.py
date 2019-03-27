import turtle


class DrawDash:
    def check_input(self, inputs):
        for val in inputs:
            if not val > 0:
                raise Exception("Value must be greater than 0")

    def plot(self, inputs):

        s = turtle.Screen()
        s.title("graph turtle")
        s.screensize(1920, 1080)
        s.setup(.75, .75)

        t = turtle.Turtle()
        t.hideturtle()
        t.pensize(2)
        t.penup()
        t.goto(-1850, 0)
        t.pendown()

        for index in range(len(inputs)):
            if index % 2 == 0:
                t.left(45)
                for i in range(inputs[index]):
                    t.forward(10)
                    if i == inputs[index] - 1:
                        t.right(45)
                        t.up()
                        t.forward(4)
                        t.down()
                    else:
                        t.up()
                        t.forward(4)
                        t.down()

            else:
                t.right(45)
                for j in range(inputs[index]):
                    t.forward(10)
                    if j == inputs[index] - 1:
                        t.left(45)
                        t.up()
                        t.forward(4)
                        t.down()
                    else:
                        t.up()
                        t.forward(4)
                        t.down()
        turtle.done()


def main():
    inputs = list(map(int, input().strip().split()))
    draw = DrawDash()
    draw.check_input(inputs)
    draw.plot(inputs)


if __name__ == '__main__':
    main()
