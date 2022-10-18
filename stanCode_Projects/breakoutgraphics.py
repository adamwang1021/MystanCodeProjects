"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 8    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
count = 0

class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        self.count = count
        self.brick_r = brick_rows
        self.brick_c = brick_cols
        self.paddle_w = paddle_width
        self.paddle_o = paddle_offset
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.window_w = window_width
        self.window_h = window_height
        self.ball_radius = ball_radius
        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width - paddle_width)/2, y=(window_height-paddle_offset))
        self.paddle_x = (window_width - paddle_width)/2
        self.paddle.filled = True
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width/2 - ball_radius, y=window_height/2-ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)
        # Default initial velocity for the ball
        # Initialize our mouse listeners
        self.__dx = 0
        self.__dy = 0
        self.click = True   # Designing a mouse-click switch
        onmouseclicked(self.drop)
        onmousemoved(self.paddle_move)
        # Draw bricks
        brick_x = 0
        brick_y = brick_offset
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.bricks = GRect(brick_width, brick_height)
                self.bricks.filled = True
                if j < 2:
                    self.bricks.fill_color = 'red'
                    self.bricks.color = 'red'
                elif j < 4:
                    self.bricks.fill_color = 'orange'
                    self.bricks.color = 'orange'
                elif j < 6:
                    self.bricks.fill_color = 'yellow'
                    self.bricks.color = 'yellow'
                elif j < 8:
                    self.bricks.fill_color = 'green'
                    self.bricks.color = 'green'
                else:
                    self.bricks.fill_color = 'blue'
                    self.bricks.color = 'blue'
                self.window.add(self.bricks, x=brick_x, y=brick_y)
                brick_y = brick_y + brick_height + brick_spacing
            brick_y = brick_offset
            brick_x = brick_x + brick_width + brick_spacing

    def paddle_move(self, event):
        """
        Link mouse movement and paddle position
        """
        if 0 < event.x < self.window.width:
            self.paddle.x = event.x - self.paddle_w/2
            if self.paddle.x < 0:
                self.paddle.x = 0
            if self.paddle.x + self.paddle_w > self.window_w:
                self.paddle.x = self.window_w - self.paddle_w
            self.paddle_x = self.paddle.x

    def drop(self, mouse):
        """
        Design the mouse click response,set the speed of the ball
        """
        if self.click:
            self.click = False
            self.__dx = random.randint(1, MAX_X_SPEED)
            print(self.__dx)
            self.__dy = INITIAL_Y_SPEED
            print(self.__dy)
            while True:
                if random.random() == 0:
                    random.random()
                else:
                    if random.random() > 0.5:
                        self.__dx = -self.__dx
                    break

    # getter
    def get_vx(self):
        return self.__dx

    # getter
    def get_vy(self):
        return self.__dy

    def set_vx(self):
        self.__dx = -self.__dx

    def set_vy(self):
        self.__dy = -self.__dy

    def collision(self):
        maybe_obj = self.window.get_object_at(self.ball.x, self.ball.y)
        maybe_obj_2 = self.window.get_object_at(self.ball.x + self.ball_radius * 2, self.ball.y)
        maybe_obj_3 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball_radius * 2)
        maybe_obj_4 = self.window.get_object_at(self.ball.x + self.ball_radius * 2,self.ball.y + self.ball_radius * 2)

        if maybe_obj:
            if maybe_obj is not self.paddle:
                self.__dy = -self.__dy
                self.window.remove(maybe_obj)
                self.count += 1
            else:
                if self.__dy > 0:
                    self.__dy = -self.__dy
        elif maybe_obj_2:
            if maybe_obj_2 is not self.paddle:
                self.__dy = -self.__dy
                self.window.remove(maybe_obj_2)
                self.count += 1
            else:
                if self.__dy > 0:
                    self.__dy = -self.__dy
        elif maybe_obj_3:
            if maybe_obj_3 is not self.paddle:
                self.__dy = -self.__dy
                self.window.remove(maybe_obj_3)
                self.count += 1
            else:
                if self.__dy > 0:
                    self.__dy = -self.__dy
        elif maybe_obj_4:
            if maybe_obj_4 is not self.paddle:
                self.__dy = -self.__dy
                self.window.remove(maybe_obj_4)
                self.count += 1
            else:
                if self.__dy > 0:
                    self.__dy = -self.__dy
        else:
            pass