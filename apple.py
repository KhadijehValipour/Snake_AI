import arcade
import random

class Apple(arcade.Sprite) :
    def __init__(self,game):
        super().__init__("assents/apple.png")
        self.width = 32
        self.height = 32
        self.center_x = (random.randint(16 ,game.width - 16)) // 16 * 16
        self.center_y = (random.randint(16 , game.height - 16)) // 16 * 16
        self.change_x = 0
        self.change_y = 0 
 
