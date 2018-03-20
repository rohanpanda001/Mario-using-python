import pygame, random, sys
from pygame.locals import *
pygame.init()

def terminate():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('mario_dies.wav')
    pygame.mixer.music.play()
    flag=0    
    Canvas.blit(end,End)    
    pygame.display.update()

def waitforit(): 
    while True:
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                else:
                    pygame.mixer.music.play(-1)
                    return 1
                
def collision(a,b):
    if (((a.left > b.left) and (a.left < b.right) and 
  (a.top > b.top) and (a.top < b.bottom))
    or ((a.left > b.left) and (a.left < b.right) and 
  (a.bottom > b.top) and (a.bottom < b.bottom))
    or ((a.right > b.left) and (a.right < b.right) and 
  (a.top > b.top) and (a.top < b.bottom))
    or ((a.right > b.left) and (a.right < b.bottom) and 
  (a.bottom > b.top) and (a.bottom < b.bottom))):
        return 1
    else:
        return 0

    
def flamehitsMario(flames):
    for i in flames:
        if collision(Mario,i) and i.right>0:
            return True

        
def check_level():
    if score in range(0,250):
        return 1
    elif score in range(250,500):
        return 2
    elif score in range(500,750):
        return 3
    elif score in range(750,1000):
        return 4

def game():
    
    global topscore,score,black,end,End,flame,Flame,Mario,mario
    pygame.mixer.music.load('mario_theme.wav')
    mario=pygame.image.load('maryo.png')
    dragon=pygame.image.load('dragon.png')
    fire=pygame.image.load('fire_bricks.png')
    cactus=pygame.image.load('cactus_bricks.png')
    start=pygame.image.load('start.png')
    end=pygame.image.load('end.png')
    flame=pygame.image.load('fireball.png')
    
    Mario=mario.get_rect()
    Dragon=dragon.get_rect()
    Fire=fire.get_rect()
    Start=start.get_rect()
    End=end.get_rect()
    Cactus=cactus.get_rect()

    Mario.topleft=(10,300)
    Dragon.topleft=(1100,300)
    Fire.topleft=(0,550)
    Cactus.bottomleft=(0,50)
    Start.centerx=600
    Start.centery=300
    End.centerx=600
    End.centery=300
    
    
    black=(0,0,0)
    blue=(0,0,255)
    white=(255,255,255)
    
    font = pygame.font.SysFont(None, 40)
    mainClock = pygame.time.Clock()
    
    
    Canvas.fill(black)
    if flag==1:
        Canvas.blit(start,Start)
    Canvas.blit(mario,Mario)
    Canvas.blit(dragon,Dragon)
    Canvas.blit(fire,Fire)
    Canvas.blit(cactus,Cactus)
    pygame.display.update()

    x=waitforit()
    
    gravity=2.5
    move_up=move_down=move_left=move_right=False
    up=False
    down=True
    d_speed=5
    m_speed=5
    flamectr=0
    flamespeed=10
    flame_break=50
    flames=[]
    ctr=0
    k=20
    key=5
    score=0
    fps=60
    
    
    while True:
            if collision(Mario,Cactus) or collision(Mario,Fire):
                terminate()
                return
            
            if flamehitsMario(flames):
                terminate()
                return
            
            
            level=check_level()
            
            if level==2:
                Cactus.bottomleft=(0,100)
                Fire.topleft=(0,500)
                gravity=3
                flamespeed=12.5
                flame_break=30
                m_speed=7
                d_speed=7

            if level==3:
                Cactus.bottomleft=(0,150)
                Fire.topleft=(0,450)
                gravity=3
                flamespeed=15
                flame_break=25
                m_speed=10
                d_speed=10

            if level==4:
                Cactus.bottomleft=(0,200)
                Fire.topleft=(0,400)
                gravity=3
                flamespeed=12.5
            
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key==K_UP:
                        move_up=True
                        score+=key
                    if event.key==K_DOWN:
                        move_down=True
                        score+=key
                    if event.key==K_RIGHT:
                        move_right=True
                        
                    if event.key==K_LEFT:
                        move_left=True
                    
                if event.type==KEYUP:
                    if event.key==K_UP:
                        move_up=False
                    if event.key==K_DOWN:
                        move_down=False
                    if event.key==K_LEFT:
                        move_left=False
                    if event.key==K_RIGHT:
                        move_right=False

                
    
            if move_up:
                Mario.top-=m_speed
                
            if move_down:
                Mario.bottom+=m_speed

            if move_left and Mario.left>0:
                Mario.left-=m_speed

            if move_right:
                Mario.right+=m_speed
            
            if move_up==False and move_down==False:
                Mario.bottom+=gravity

            
            Canvas.fill(black)
            

            if down:
                if(Dragon.bottom>Fire.top):
                    down=False
                    up=True
                else:   
                    Dragon.bottom+=d_speed
            if up:
                if(Dragon.top<Cactus.bottom):
                    up=False
                    down=True
                else:   
                    Dragon.top-=d_speed

                    
            flamectr+=1

            
            if flamectr%flame_break==0:
                
                Flame=flame.get_rect()
                Flame.topright=Dragon.topleft
                flames.append(Flame)
                ctr+=1
            for i in range(0,ctr):
                flames[i].left-=flamespeed
                Canvas.blit(flame,flames[i])

            
            name=font.render('Score:', 1, white)
            name_rect=name.get_rect()
            name_rect.topleft=(400, Cactus.bottom+10)

            Score= font.render(str(score), 1, white)
            SCORE=Score.get_rect()
            SCORE.topleft = name_rect.topright

            topscr=font.render(' | TopScore:', 1, white)
            Topscore=topscr.get_rect()
            Topscore.topleft=SCORE.topright

            name2=font.render(str(topscore), 1, white)
            name2_rect=name2.get_rect()
            name2_rect.topleft=Topscore.topright

            name3=font.render(' | Level:',1,white)
            name3_rect=name3.get_rect()
            name3_rect.topleft=name2_rect.topright

            lvl=font.render(str(level),1,white)
            Level=lvl.get_rect()
            Level.topleft=name3_rect.topright
            
                    
            Canvas.blit(mario,Mario)
            Canvas.blit(dragon,Dragon)
            Canvas.blit(fire,Fire)
            Canvas.blit(cactus,Cactus)
            Canvas.blit(name,name_rect)
            Canvas.blit(Score,SCORE)
            Canvas.blit(topscr,Topscore)
            Canvas.blit(name2,name2_rect)
            Canvas.blit(name3,name3_rect)
            Canvas.blit(lvl,Level)
            pygame.display.update()
            mainClock.tick(fps)

            
    pygame.display.update()


Canvas = pygame.display.set_mode((1200,600))
pygame.display.set_caption('Mario - by Rohan')
global flag
flag=1
topscore=0
game()
while waitforit()==1:
    if topscore<score:
        topscore=score
    game()


            



                
