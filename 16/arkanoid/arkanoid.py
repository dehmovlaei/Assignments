import arcade
from rocket import Rocket
from ball import Ball
from block import Block
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=600, height=800, title='arkanoid 🔵🔵🔵', center_window=True)
        self.background = arcade.load_texture(':resources:images/backgrounds/abstract_1.jpg')
        self.rocket = Rocket(self)
        self.sprite_list = arcade.SpriteList()
        self.ball = Ball(self)
        self.x = 30
        self.y = 600
        self.color = arcade.color.AMERICAN_ROSE

    def on_draw(self):
        arcade.start_render()

        for i in range(5):
            for j in range(10):
                self.blocks = Block(self.x, self.y, self.color)
                self.blocks.draw()
                self.x += 60                
        self.y += 25
        
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.rocket.draw()
        self.ball.draw()
        arcade.draw_text(f'SCORE: {self.rocket.score}', 5, 780, arcade.color.AMERICAN_ROSE, 15, 2,'left',('calibri', 'calibri'), True)
               
        arcade.finish_render

    def on_key_press(self, symbol: int, modifiers: int):

        if symbol == arcade.key.LEFT or symbol == arcade.key.A :
            self.rocket.change_x = -1
        elif symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.rocket.change_x = 1
        elif symbol == arcade.key.DOWN:
            self.rocket.change_x = 0

    def on_update(self, delta_time: float):
        self.ball.move()
        self.rocket.move()
        
        if self.ball.center_x < 2 or self.ball.center_x > self.width-2:
            self.ball.change_x *= -1

        if self.ball.center_y > self.height:
            self.ball.change_y *= -1
        
        if arcade.check_for_collision(self.rocket, self.ball):
            self.ball.change_y *= -1

        # if arcade.check_for_collision_with_list(self.ball, self.rocket):
        #     self.ball.change_y *= -1
        #     self.rocket.score += 1

        if self.ball.center_y < 0:
            print('OOps !!!')
            del self.ball
            self.ball = Ball(self)
        
if __name__ == '__main__':
     game = Game()
     arcade.run()