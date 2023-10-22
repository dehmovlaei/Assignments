import arcade
from rocket import Rocket
from ball import Ball
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=500, title='Pong 2023 🏓🏓', center_window=True)
        arcade.set_background_color(arcade.color.DARK_GREEN)
        self.player1 = Rocket(40, self.height//2, arcade.color.RED, 'dehmovlaei')
        self.player2 = Rocket(self.width-40, self.height//2, arcade.color.CYAN, 'CPU')
        self.sprite_list = arcade.SpriteList()
        self.ball = Ball(self)

        self.sprite_list.append(self.player1)
        self.sprite_list.append(self.player2)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_outline(self.width//2, self.height//2,self.width-30, self.height-30,
                                      arcade.color.WHITE, border_width=10)
        arcade.draw_line(self.width//2, 30, self.width//2, self.height-30,
                         color=arcade.color.WHITE, line_width=10)
        self.player1.draw()
        self.player2.draw()
        self.ball.draw()

        arcade.finish_render

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        
        if self.player1.height-11 < y < self.height-self.player1.height+11:
            self.player1.center_y = y

    def on_update(self, delta_time: float):
        self.ball.move()
        self.player2.move(self)
        
        if self.ball.center_y < 30 or self.ball.center_y > self.height-30:
            self.ball.change_y *= -1

        if arcade.check_for_collision_with_list(self.ball, self.sprite_list):
            self.ball.change_x *= -1

        if self.ball.center_x < 0:
            print('GOAL !!!')
            self.player2.score += 1
            del self.ball
            self.ball = Ball(self)

        if self.ball.center_x > self.width:
            print('GOAL !!!')
            self.player1.score += 1
            del self.ball
            self.ball = Ball(self)

if __name__ == '__main__':
     game = Game()
     arcade.run()