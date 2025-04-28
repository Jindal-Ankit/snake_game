from turtle import Turtle


MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snake = []
        start_x = 0
        start_pos = (start_x,0)
        for _ in range(3):
            #create square shape and color white
            turt = self.create_snake_segment(start_pos)
            start_x = turt.xcor() - 20
            #append to a list "snake"
            self.snake.append(turt)
            self.head = self.snake[0]

    def move(self):
        snake_segments = self.snake
        for seg_idx in range(len(snake_segments)-1, 0, -1):
            seg_x_cor = snake_segments[seg_idx-1].xcor()
            seg_y_cor = snake_segments[seg_idx-1].ycor()
            snake_segments[seg_idx].goto(seg_x_cor,seg_y_cor)

        snake_segments[0].forward(MOVE_DISTANCE)

    def create_snake_segment(self, position):
        turt = Turtle(shape="square")
        turt.penup()
        turt.color("white")
        # set position for each square one behind another
        turt.goto(position)
        return turt

    def extend(self):
        self.snake.append(self.create_snake_segment((self.snake[-1].xcor(), self.snake[-1].ycor())))

    def did_snake_head_collision_with_tail(self):
        count = 0
        print(len(self.snake[1:]))
        for seg in self.snake[1:]:
            count += 1
            print(f"{count} {self.head.distance(seg)}")
           # print(f"Distance snake and segment {seg}: {self.head.distance(seg)}")
            if self.head.distance(seg) < 15:
                return True

    def up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(90)

    def down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(270)

    def left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(180)

    def right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(0)