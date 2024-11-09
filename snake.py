from turtle import Screen, Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 0
RIGHT = 180
segments = []





class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.move()
        self.up()
        self.down()
        self.right()
        self.left()


    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)



    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVING_DISTANCE)


    def add_segments(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # add a new segment to the game
        self.add_segments(self.segments[-1].position())



    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(270)


    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(0)


    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(180)

    def reset(self):
        for segment in self.segments:
            segment.goto(100, 1000)
        self.segments.clear()
        self.create_snake()



