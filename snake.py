from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]

UP = 90
DOWN =270
LEFT = 180
RIGHT = 0

class Snake():
    """This is the snake body
    """
    def __init__(self) -> None:
        self.segments = []
        self.snakeobjects()
        self.head = self.segments[0]
  
    
    #creating snakeobjects "squares"
    def snakeobjects(self):
        """ creates the first 3 squares that
        the snake body
        """
        for postion in STARTING_POSITION:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(postion)
            self.segments.append(new_segment)
    #teste en annen logikk
    def move(self):
        """logic that makes tail follow the head
        """
        for seg_num in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        #hold tail coordinates
        x_tail = self.segments[-1].xcor()
        y_tail = self.segments[-1].ycor()
        
        #create new segment
        extend_segment = Turtle(shape="square")
        extend_segment.color("white")
        extend_segment.penup()
        extend_segment.goto(x_tail, y_tail)
        self.segments.append(extend_segment)


    #creating the keys to move the snake
    def Up(self):
        #SNAKE RULE if snake is not heading 
        #down you move snake up
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def Left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def Down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def Right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

