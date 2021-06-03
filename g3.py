import pygame
from pygame.locals import *
import random
import time


pygame.init()

pygame.display.set_caption("star-wars")

class Game:
    def __init__(self):
        self.display_width=600
        self.display_height=600

        self.game_display = pygame.display.set_mode((self.display_width,self.display_height))
        self.bg=pygame.image.load('rocket.png')
        self.bg=pygame.transform.scale(self.bg,(100,100))
        
        self.sp=pygame.image.load('space4.jpg')
        self.sp=pygame.transform.scale(self.sp,(600,600))
        
        self.ob=pygame.image.load('Rocket1.png')
        self.ob=pygame.transform.scale(self.ob,(100,100))
        
        #self.bu=pygame.image.load('bullets.jpg')
        #self.bu=pygame.transform.scale(self.bu,(50,50))
        
        self.wl=pygame.image.load('backg.png')
        self.wl=pygame.transform.scale(self.wl ,(360,600))
        
        #self.wl=pygame.image.load('space2.png')
        #self.wl=pygame.transform.scale(self.wl ,(360,600))
        
        self.color=pygame.image.load('black.png')
        self.color=pygame.transform.scale(self.color ,(120,600))
        
        #self.cr=pygame.image.load('crash.png')
        #self.cr=pygame.transform.scale(self.cr ,(50,50))

        self.x=120
        self.y=500
        self.height=100
        self.width=100
        self.vel=8
        self.vel_med=10
        self.vel_hard=12

        self.keys=pygame.key.get_pressed()
        self.clock=pygame.time.Clock()

        self.l=[120,150,200,250,300,350,380]
        self.a=random.choice(self.l)
        self.b=0

        self.c=self.x
        self.d=self.y-100

        self.e=random.choice(self.l)
        self.f=0

        self.acc=8
        self.acc1=10
        self.acc_medium=10
        self.acc_hard=12
        self.score=0
        self.flag=0

        self.run=False
        self.run_medium=False
        self.run_hard=False
        self.over=True
        self.exit=False
        self.r=True

    def screen(self):
        self.game_display.blit(self.sp, (0,0))
        #pygame.draw.rect(self.game_display,(0,191,255),(0,0,600,600))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.r=False
            self.keys=pygame.key.get_pressed()
            if(self.keys[pygame.K_1]):
                self.flag=1
                self.r=False
                self.run=True
            if(self.keys[pygame.K_2]):
                self.flag=2
                self.r=False
                self.run_medium=True
            if(self.keys[pygame.K_3]):
                self.flag=3
                self.r=False
                self.run_hard=True
    
    def car(self):
        self.game_display.blit(self.color, (0,0))
        self.game_display.blit(self.color, (480,0))
        self.game_display.blit(self.wl, (120,0))
        self.game_display.blit(self.bg, (self.x,self.y))
        self.game_display.blit(self.ob, (self.a,self.b))
        #self.game_display.blit(self.ob, (self.e,self.f))

    def update(self):
        pygame.display.update()
        self.clock.tick(60)

    def display_score(self):
        self.myfont=pygame.font.Font("freesansbold.ttf",20)
        self.scoretext=self.myfont.render("score= "+str(self.score),1,(0,191,255))
        self.game_display.blit(self.scoretext, (0,0))
        self.update()
    
    def text_objects(self,text):
	textSurface=self.myfont.render(text,True,(0,191,255))
	return textSurface,textSurface.get_rect()
    
    def message_display(self,text):
        self.largetext=pygame.font.Font('freesansbold.ttf',30)
	self.TextSurf,self.TextRect=self.text_objects(text)
	self.TextRect.center=((self.display_width/2),(self.display_height/2))
	self.game_display.blit(self.TextSurf,self.TextRect)
	self.update()

    def movement(self):
        #while self.over:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.run=False
            if(self.score<=50):
                self.vel=8
            elif(self.score>=50 and self.score<=100):
                self.vel=12
            elif(self.score>=100):
                self.vel=15
            self.keys=pygame.key.get_pressed()
            if self.keys[pygame.K_LEFT] and self.x>=120:
                    self.x-=self.vel
            if self.keys[pygame.K_RIGHT] and self.x<=480-self.width:
                    self.x+=self.vel
            if self.keys[pygame.K_ESCAPE]:
                self.run=False
            self.car()
            self.obstacle()
            self.display_score()
            self.gameover_condition()
            #self.gameover()
            #self.update()
    
    def movement_medium(self):
        #while self.over:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.run_medium=False
        if(self.score<=30):
            self.vel_medium=10
        elif(self.score>=30 and self.score<=80):
            self.vel_medium=15
        elif(self.score>=80):
            self.vel_medium=20
        self.keys=pygame.key.get_pressed()
        if self.keys[pygame.K_LEFT] and self.x>=120:
                self.x-=self.vel_medium
        if self.keys[pygame.K_RIGHT] and self.x<=480-self.width:
                self.x+=self.vel_medium
        if self.keys[pygame.K_ESCAPE]:
            self.run_medium=False
        self.car()
        self.obstacle_medium()
        self.display_score()
        self.gameover_condition()
        #self.gameover()
        #self.update()
    
    def movement_hard(self):
        #while self.over:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.run_hard=False
            if(self.score<=25):
                self.vel_hard=12
            elif(self.score>=25 and self.score<=50):
                self.vel_hard=18
            elif(self.score>=100):
                self.vel_hard=25
            self.keys=pygame.key.get_pressed()
            if self.keys[pygame.K_LEFT] and self.x>=120:
                    self.x-=self.vel_hard
            if self.keys[pygame.K_RIGHT] and self.x<=480-self.width:
                    self.x+=self.vel_hard
            if self.keys[pygame.K_ESCAPE]:
                self.run_hard=False
            self.car()
            self.obstacle_hard()
            self.display_score()
            self.gameover_condition()
            #self.gameover()
            #self.update()

    def obstacle(self):
        if(self.b<self.display_height):
            self.b+=self.acc
            self.update()
        if(self.b>=self.display_height):
            self.b=0
            self.a=random.choice([120,180,240,self.x,320,380])
            self.score+=5
            self.acc+=1
            #self.vel1+=self.acc1
            self.update()
    
    def obstacle_medium(self):
        if(self.b<self.display_height):
            self.b+=self.acc_medium
            self.update()
        if(self.b>=self.display_height):
            self.b=0
            self.a=random.choice([120,180,240,self.x,320,380])
            self.score+=5
            self.acc_medium+=2
            #self.vel1+=self.acc1
            self.update()
    
    def obstacle_hard(self):
        if(self.b<self.display_height):
            self.b+=self.acc_hard
            self.update()
        if(self.b>=self.display_height):
            self.b=0
            self.a=random.choice([120,180,240,self.x,320,380])
            self.score+=5
            self.acc_hard+=4
            #self.vel1+=self.acc1
            self.update()
    
    def gameover_condition(self):
        if((self.a>self.x-50 and self.a<=self.x+40) and (self.b<=self.y+100 and self.y<self.b)):
            #self.over=True
    #def gameover(self):
            self.game_display.fill((255,255,255))
            self.message_display('Gameover Score= '+str(self.score))
            time.sleep(3)
            pygame.quit()
        #self.update()
    
    def gameloop(self):
        while self.r==True:
            self.screen()
            self.update()
        if(self.flag==1):
            while(self.run):
                self.movement()
        if(self.flag==2):
            while(self.run_medium):
                self.movement_medium()
        if(self.flag==3):
            while(self.run_hard):
                self.movement_hard()
            #while self.over:
            #    self.gameover()
g=Game()
g.gameloop()
