from pygame import*
from random import randint

init()

WINDOW_SIZE = 800,600
FPS = 60

running = True
lose = False

screen = display.set_mode(WINDOW_SIZE)
display .set_caption("AGAR.IO")

clk = time.Clock()




 class playr:
   def__init__(self,x,y,r,name,color=(255,0,0)):
        self.x = x
        self.y = y
        self.r = r
        self.name = name
        self.color = color
   
   def move(self):
        keys = key.get_pressed()
        if keys [K_w]:
         self.y -= 5
        if keys [K_w]:
         self.y += 5
        if keys [K_w]:
         self.x -= 5
        if keys [K_w]:
         self.x += 5
    def draw(self):
    draw.circle(screen, self.color, (self.x,self.y), self.r)


class food:
   def __init__(self):
      self.x = randint(-2000,2000)
      self.y = randint(-2000,2000)
      self.r = 10
      self.color = (randint(10,255),randint(10,255),randint(10,255))

    def check_collision(self,playr):
      dx = self.x - playr.x
      dy = self.y - playr.y
      return hypot(dx,dy) < self.r + playr.r
   def draw.circle(screen, self.color, (self.x,self.y), self.r)

scala = 
my playr = playr

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    screen.fill((255,255,255))

    for f in foods:
       if f.chech_collision
    
                            
                            


    display.update()
    clk.tick(FPS)

   