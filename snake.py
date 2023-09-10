import arcade


class Snake(arcade.Sprite) :
    def __init__(self , game):
      super().__init__()
      self.width = 32
      self.height = 32
      self.center_x = game.width // 2
      self.center_y = game.height // 2
      self.color = arcade.color.GREEN
      self.change_x = 1
      self.change_y = 0
      self.speed = 16
      self.score = 0
      self.body = []

    def draw(self) :
      arcade.draw_rectangle_filled(self.center_x , self.center_y ,
                                    self.width , self.height , self.color )
      for part in self.body:
          arcade.draw_rectangle_filled(part['x'], part['y'] ,
                                        self.width , self.height , self.color)

    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed
        self.body.append({'x':self.center_x , 'y':self.center_y})
        if len(self.body) > self.score :

            self.body.pop(0)


    def eat(self,food): 
        del food
        self.score += 1
        print("score:",self.score)
        