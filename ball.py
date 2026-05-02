class Ball:
    def__init__(self,x,y,r,color,vx = Note,vy=None):
        self.x = x
        self.y = y
        self.r = r
        self.vx = vx if vx is not None else 5
        self.vy = vy if vy is not None else 5
        self.rect = Rect(0,0,r,r)
        self.rect.center = (self.x,self.y)
    def check_collision(self,other)
        return self.rect.colliderect(other.rect)
    
    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.rect.center = (self.x,self.y)

        if self.x - self.r < 0 or self + self.r > 800:
            self.vx *= -1
        if self.y - self.r < 0 or self + self.r > 600:
            self.vy *= -1
    
    def draw(self,screen):
        draw.circle(screen, self.color, (self.x,self.y),self.r)