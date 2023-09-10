
import arcade
from snake import Snake
from apple import Apple

      

class Game(arcade.Window) :
    def __init__(self):
        super().__init__(width=512 , height=512 , title= "Super Snake 🐍🍎")
        arcade.set_background_color(arcade.color.KHAKI)
        
        self.snake = Snake(self)
        self.food=Apple(self)

    def on_draw(self):
        arcade.start_render()
        self.snake.draw()
        self.food.draw()
        arcade.finish_render()

    def on_update(self, delta_time: float):
        self.snake.move()

        if arcade.check_for_collision(self.snake , self.food):
            self.snake.eat(self.food)
            self.food = Apple(self)


    def on_key_release(self, symbol: int, modifiers: int):
        
        if symbol == arcade.key.UP :
            self.snake.change_x = 0
            self.snake.change_y = 1

        elif symbol == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1

        elif symbol == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0

        elif symbol == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0



if __name__ == "__main__" :
    game = Game()
    arcade.run()