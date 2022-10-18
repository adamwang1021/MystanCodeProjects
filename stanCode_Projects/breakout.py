"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts
lives = 3       # count for lives remain


def main():
    """
    This program is used to create a small game of breaking bricks
    using the path of the ball to destroy the bricks,
    and the bounce of the ball when it hits the paddle,
    and when the ball falls to the bottom, to restart and count the remaining lives
    """
    global lives
    graphics = BreakoutGraphics()
    while True:
        if graphics.count == graphics.brick_r * graphics.brick_c:
            break
        if not graphics.click:
            while True:
                vx = graphics.get_vx()
                vy = graphics.get_vy()
                # Update
                if lives > 0:
                    graphics.ball.move(vx, vy)
                # Check
                if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                    graphics.set_vx()
                if graphics.ball.y <= 0:
                    graphics.set_vy()
                if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                    lives -= 1
                    graphics.ball.filled = True
                    graphics.window.add(graphics.ball,x=graphics.window_w/2 - graphics.ball_radius, y=graphics.window_h/2-graphics.ball_radius)
                    graphics.click = True
                    break
                graphics.collision()
                if graphics.count == graphics.brick_r * graphics.brick_c:
                    break
                # Pause
                pause(FRAME_RATE)
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
