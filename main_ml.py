import tensorflow as tf
import arcade
from snake import Snake
from apple import Apple

class Game(arcade.Window) :
    def __init__(self):
        super().__init__(width=512 , height=512 , title= "Super Snake 🐍🍎")
        arcade.set_background_color(arcade.color.KHAKI)  
        self.snake = Snake(self)
        self.food=Apple(self)
        self.model = tf.keras.models.load_model('E:/PYLEARN/app/MachineLearning_project/weights/snake_game_model.h5')


    def on_draw(self):
        arcade.start_render()
        self.snake.draw()
        self.food.draw()
        arcade.finish_render()

    def on_update(self, delta_time: float):
        self.snake.move()

        if self.snake.center_y > self.food.center_y :
            self.snake.change_x = 0
            self.snake.change_y = -1

        elif self.snake.center_y < self.food.center_y :
            self.snake.change_x = 0
            self.snake.change_y = 1

        elif self.snake.center_x > self.food.center_x :
            self.snake.change_x = -1
            self.snake.change_y = 0

        elif self.snake.center_x < self.food.center_x :
            self.snake.change_x = 1
            self.snake.change_y = 0


        self.snake.on_update(delta_time)
        self.food.on_update()
        
        if arcade.check_for_collision(self.snake , self.food):
            self.snake.eat(self.food)
            self.food = Apple(self)

if __name__ == "__main__" :
    game = Game()
    arcade.run()