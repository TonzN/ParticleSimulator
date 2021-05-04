import mathLib as m
import math
import particleSystem as pS
import UI2 as ui
import pygame
import time
import random

window = ui.NewWindow()

Gravity = 9.8
#standard = 100pixel = 1m
particles = []

while True:  
    for i in range(600):
        p = pS.Particle(window.screen, 400-7, 300-7, 7, 7, (random.randint(70, 220),random.randint(70, 220),random.randint(70, 220)), 1)
        particles.append(p)
        p.xv = 9
        p.NewAngle(i)
        p.xv = 1.618*i
        #p.xv = random.choice([i, -i])

    while True:      
        window.NextFrame() 
        for i in particles:
            i.Update()
        
   