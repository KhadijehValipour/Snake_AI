
import arcade
import pandas as pd
from snake import Snake
from apple import Apple

      

class Game(arcade.Window) :
    def __init__(self):
        super().__init__(width=512 , height=512 , title= "Super Snake 🐍🍎")
        arcade.set_background_color(arcade.color.KHAKI)
        
        self.snake = Snake(self)
        self.food=Apple(self)
        self.dataset=[]

    def on_draw(self):
        arcade.start_render()
        self.snake.draw()
        self.food.draw()
        arcade.finish_render()

    def on_update(self, delta_time: float):
        self.snake.move()

        data = {"wu":None , 
                "wr":None ,
                "wd":None ,
                "wl":None ,
                "au":None ,
                "ar":None ,
                "ad":None ,
                "al":None ,
                "bu":None ,
                "br":None ,
                "bd":None ,
                "bl":None ,
                "direction" : None}

        if self.snake.center_y > self.food.center_y :
            self.snake.change_x = 0
            self.snake.change_y = -1
            data['direction'] = 2

        elif self.snake.center_y < self.food.center_y :
            self.snake.change_x = 0
            self.snake.change_y = 1
            data['direction'] = 0

        elif self.snake.center_x > self.food.center_x :
            self.snake.change_x = -1
            self.snake.change_y = 0
            data['direction'] = 3

        elif self.snake.center_x < self.food.center_x :
            self.snake.change_x = 1
            self.snake.change_y = 0
            data['direction'] = 1

        # Data collection by calculating the distance from the apple to the head of the snake
        if self.snake.center_x == self.food.center_x and self.snake.center_y < self.food.center_y :
            data["au"] = 1
            data["ad"] = 0
            data["al"] = 0
            data["ar"] = 0 

        elif self.snake.center_x == self.food.center_x and self.snake.center_y > self.food.center_y :
            data["au"] = 0
            data["ad"] = 1
            data["al"] = 0
            data["ar"] = 0

        elif self.snake.center_x > self.food.center_x and self.snake.center_y == self.food.center_y :
            data["au"] = 0
            data["ad"] = 0
            data["al"] = 1
            data["ar"] = 0

        elif self.snake.center_x < self.food.center_x and self.snake.center_y == self.food.center_y :
            data["au"] = 0
            data["ad"] = 0
            data["al"] = 0
            data["ar"] = 1
        
        # Data collection by calculating the distance from the wall to the head of the snake
        data["wu"] = game.height - self.snake.center_y
        data["wd"] = self.snake.center_y
        data["wl"] = self.snake.center_x
        data["wr"] = game.width - self.snake.center_x

        
        # Data collection by calculating the distance from the snake's head to its body
        for part in self.snake.body :
             if self.snake.center_x == part['x'] and self.snake.center_y < part['y'] :
                 data['bu'] = 1
                 data['bd'] = 0
                 data['bl'] = 0
                 data['br'] = 0
             elif self.snake.center_x == part['x'] and self.snake.center_y > part['y'] :
                 data['bu'] = 0
                 data['bd'] = 1
                 data['bl'] = 0
                 data['br'] = 0
             elif self.snake.center_x < part['x'] and self.snake.center_y == part['y'] :
                 data['bu'] = 0
                 data['bd'] = 0
                 data['bl'] = 0
                 data['br'] = 1
             elif self.snake.center_x > part['x'] and self.snake.center_y == part['y'] :
                 data['bu'] = 0
                 data['bd'] = 0
                 data['bl'] = 1
                 data['br'] = 0
             elif  self.snake.center_y < part['y'] :
                 data['bu'] = 1
                 data['bd'] = 0
                 data['bl'] = 0
                 data['br'] = 0
             elif self.snake.center_y > part['y'] :
                 data['bu'] = 0
                 data['bd'] = 1
                 data['bl'] = 0
                 data['br'] = 0
             elif self.snake.center_x < part['x'] :
                 data['bu'] = 0
                 data['bd'] = 0
                 data['bl'] = 0
                 data['br'] = 1
             elif self.snake.center_x > part['x']  :
                 data['bu'] = 0
                 data['bd'] = 0
                 data['bl'] = 1
                 data['br'] = 0

        self.dataset.append(data)


        self.snake.on_update(delta_time)
        self.food.on_update()
        
        if arcade.check_for_collision(self.snake , self.food):
            self.snake.eat(self.food)
            self.food = Apple(self)


    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.Q :
            df = pd.DataFrame(self.dataset)
            df.to_csv('dataset.csv' , index=False)
            arcade.close_window()
            exit(0)


if __name__ == "__main__" :
    game = Game()
    arcade.run()