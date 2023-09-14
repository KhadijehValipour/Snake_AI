import arcade


class Snake(arcade.Sprite) :
    def __init__(self , game):
      super().__init__()
      self.width = 32
      self.height = 32
      self.center_x = game.width // 2
      self.center_y = game.height // 2
      self.color = arcade.color.YELLOW
      self.colorbody = arcade.color.BRONZE_YELLOW
      self.change_x = 1
      self.change_y = 0
      self.speed = 16
      self.score = 0
      self.body = []

    def draw(self) :
      arcade.draw_rectangle_filled(self.center_x , self.center_y , self.width , self.height , self.color )
      
      for i , part in enumerate(self.body):
          if i % 2 == 0 :
            self.colorbody = arcade.color.BRONZE_YELLOW
          elif i % 2 == 1 :
             self.colorbody = arcade.color.YELLOW
          arcade.draw_rectangle_filled(part['x'], part['y'] , self.width , self.height , self.colorbody)
        

    def move(self):
        
        self.body.append({'x':self.center_x ,'y':self.center_y})

        if len(self.body) > self.score : 
           self.body.pop(0)
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def eat(self,food): 
        del food
        self.score += 1
        print("score:",self.score)
        