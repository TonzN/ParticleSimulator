import UI2 as ui
import math

class Particle(ui.Rect):
    def __init__(self,screen, x, y, w, h, color, density):
        super().__init__(screen,x, y, w, h, color)
        self.xv = 0 # v = velocity 
        self.yv = 0
        self.w, self.h = w, h
        self.mass = (w*h*density)/100
        self.force = self.mass*9.8
        ui.MainRenderQueue.Push(self)

    def Update(self):
        self.x += self.xv/60 
        self.y -= self.yv/60 - self.force/60


        if self.y > 600-self.height:
            self.y = 600-self.height
            if self.yv < 0:
                self.yv = abs(self.yv)
        elif self.y < 0:
            self.y = 0 
            if self.yv > 0:
                self.yv = self.yv * -1

        if self.x > 800-self.width:
            self.x = 800-self.width
            if self.xv > 0:
                self.xv = self.xv * -1
        elif self.x < 0:
            self.x = 0
            if self.xv < 0:
                self.xv = abs(self.xv)
    
    def NewAngle(self, deg):
        tangent = math.tan(math.radians(deg))   
        self.yv = self.force +  self.xv * tangent