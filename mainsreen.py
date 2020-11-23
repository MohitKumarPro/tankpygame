import pygame
import random
import math
from pygame import mixer
from tkinter import messagebox



pygame.display.init()
pygame.mixer.init()
i=0
screen=pygame.display.set_mode((1366,700))

mixer.music.load('back.mp3')
mixer.music.play(-1)
pygame.display.set_caption("TANK WAR")
icon=pygame.image.load("title.png")
pygame.display.set_icon(icon)

#HERO
heroimg = pygame.image.load("tank.png")
herox = 1000
heroy = 300
hx=0
hy=0
last = 'up'
hello = 'no'


collision=0

#BULLET2
bullet_m = pygame.image.load("bullets.png")
bxx=0
byy=0
bbxx=0
bbyy=0
bbyy=0
bbbyy1=0
bbbxx1=0
bbbyy2=0
bbbxx2=0
bbbyy3=0
bbbxx3=0
bbbyy4=0
bbbxx4=0



#BULLET
bullet = pygame.image.load("bullet.png")
bx=0
by=0
bbby1=0
bbbx1=0
bbby2=0
bbbx2=0
bbby3=0
bbbx3=0
bbby4=0
bbbx4=0

bbby11=0
bbbx11=0
bbby22=0
bbbx22=0
bbby33=0
bbbx33=0
bbby44=0
bbbx44=0
#PLAER2
pla2 = pygame.image.load("tankiii.png")
px=0
py=0
pherox=300
pheroy=300



bmta='non'
bsta = 'none'
bvin1=0
num1=0
num2=10
num3=1300
num4=620
num5=0
num6=620
num7=1300
num8=10




bbx=0
bby=0
r_bu=bullet
last1='up'
state = 'ready'
state1 = 'read1'
state2 = 'read2'
state3 = 'ready3'


state11 = 'ready11'
state12 = 'read12'
state23 = 'read23'
state34 = 'ready34'
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf',32)
def hero(m_hero,x,y):
    screen.blit(m_hero,(x,y))

#PLAYER2
def play2(m_play,plax,play):
    screen.blit(m_play,(plax,play))


def bul(m_bu,xx,yy):
    screen.blit(m_bu,(xx,yy))


def bull(mbul,xbul,ybul):
    screen.blit(mbul,(xbul,ybul))


def iscollision(hexx,hey,bux,buy):
    dis = math.sqrt(math.pow(bux-hexx,2)+math.pow(buy-hey,2))


    if dis < 20:
        return True
    else:
        return False

def gameover(hel):

    overtext = font.render("GAME OVER"+"  "+hel,True,(255,255,255))
    screen.blit(overtext,(320,350))

                
   
                    
            ##################
         
                    

    
                
            


    
run=True
while run:
    #INSIDE OF THE GAME LOOP
    screen.fill((255,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type == pygame.KEYDOWN:


            ##################
            if event.key == pygame.K_k:
                px = 0.2
            
                last1 = 'right'
            if event.key == pygame.K_j:
                px = -0.2
                last1 = 'left'
            if event.key == pygame.K_i:
                py = -0.2
                last1 = 'up'
            if event.key == pygame.K_m:
                py = 0.2
                last1 = 'down'
            #################
            if event.key ==pygame.K_e and last=='up':
                bullm = mixer.Sound('bullet1.mp3')
                bullm.play()
                state='fire'
                bbby1 = heroy
                dddb1= r_bu
                bbbx1= herox
            if event.key ==pygame.K_e and last=='right':
                bullm = mixer.Sound('bullet1.mp3')
                bullm.play()
                state1='fire1'
                bbby2 = heroy
                dddb2 = r_bu
                bbbx2= herox
            if event.key ==pygame.K_e and last=='left':
                bullm = mixer.Sound('bullet1.mp3')
                bullm.play()
                state2='fire2'
                bbby3 = heroy
                dddb3 = r_bu
                bbbx3= herox
            if event.key ==pygame.K_e and last=='down':
                bullm = mixer.Sound('bullet1.mp3')
                bullm.play()
                state3='fire3'
                bbby4 = heroy
                dddb4 = r_bu
                bbbx4= herox



    ###########################################

            if event.key ==pygame.K_q and last1=='up':
                bull1 = mixer.Sound('bullet2.mp3')
                bull1.play()
                state11='fire11'
                bbby11 = pheroy
                dddb11= m_bu
                bbbx11= pherox
            if event.key ==pygame.K_q and last1=='right':
                bull1 = mixer.Sound('bullet2.mp3')
                bull1.play()
                state12='fire12'
                bbby22 = pheroy
                dddb22 = m_bu
                bbbx22= pherox
            if event.key ==pygame.K_q and last1=='left':
                bull1 = mixer.Sound('bullet2.mp3')
                bull1.play()
                state23='fire23'
                bbby33 = pheroy
                dddb33 = m_bu
                bbbx33= pherox
            if event.key ==pygame.K_q and last1=='down':
                bull1 = mixer.Sound('bullet2.mp3')
                bull1.play()
                state34='fire34'
                bbby44= pheroy
                dddb44 = m_bu
                bbbx44= pherox
    ############################################
               
                   

            if event.key == pygame.K_RIGHT:
                hx = 0.2
            
                last = 'right'
            if event.key == pygame.K_LEFT:
                hx = -0.2
                last = 'left'
            if event.key == pygame.K_UP:
                hy = -0.2
                last = 'up'
            if event.key == pygame.K_DOWN:
                hy = 0.2
                last = 'down'
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                hx = 0
            if event.key == pygame.K_LEFT:
                hx = 0
            if event.key == pygame.K_UP:
                hy = 0
            if event.key == pygame.K_DOWN:
                hy = 0

            #######################
            if event.key == pygame.K_k:
                px = 0
            if event.key == pygame.K_j:
                px = 0
            if event.key == pygame.K_i:
                py = 0
            if event.key == pygame.K_m:
                py = 0
            ######################
    
    #RANDOM
    ranx = random.randint(1,4)


    herox = herox+hx
    heroy = heroy+hy
    pherox = pherox+px
    pheroy = pheroy+py
    if last =='up':
        r_hero = pygame.transform.rotate(heroimg,0)
        r_bu = pygame.transform.rotate(bullet,0)
        
    if last =='right':
        r_hero = pygame.transform.rotate(heroimg,-90)
        r_bu = pygame.transform.rotate(bullet,-90)
        
    if last =='left':
        r_hero = pygame.transform.rotate(heroimg,90)
        r_bu = pygame.transform.rotate(bullet,90)
        
    if last =='down':
        r_hero = pygame.transform.rotate(heroimg,180)
        r_bu = pygame.transform.rotate(bullet,180)
       #########################################
    if last1 == 'up':
        m_pla2 = pygame.transform.rotate(pla2,0)
        m_bu = pygame.transform.rotate(bullet_m,0)
        
    if last1 == 'right':
        m_pla2 = pygame.transform.rotate(pla2,-90)
        m_bu = pygame.transform.rotate(bullet_m,-90)
        
    if last1 =='left':
        m_pla2 = pygame.transform.rotate(pla2,90)
        m_bu = pygame.transform.rotate(bullet_m,90)
        
    if last1 =='down':
        m_pla2 = pygame.transform.rotate(pla2,180)
        m_bu = pygame.transform.rotate(bullet_m,180)
    #########################################
    
    if state=='fire':
        
        bul(dddb1,bbbx1+20,bbby1-bby)


        collision = iscollision(pherox,pheroy,bbbx1,bbby1-bby)

        if collision == True:

            hello = "GREEN KNIGHT WON THE GAME"
        bby+=1
        if bby==500 or collision==True:
            state = 'ready'
            bby=0
    
    if state1=='fire1':
        
        bul(dddb2,bbbx2+bbx,bbby2+20)


        collision = iscollision(pherox,pheroy,bbbx2+bbx,bbby2)
        if collision == True:

            hello = "GREEN KNIGHT WON THE GAME"

        bbx+=1
        if bbx==500 or collision==True:
            state1= 'ready1'
            bbx=0
    
    if state2=='fire2':
        
        bul(dddb3,bbbx3-bbx,bbby3+20)

        collision = iscollision(pherox,pheroy,bbbx3-bbx,bbby3)
        if collision == True:

            hello = "GREEN KNIGHT WON THE GAME"

        bbx+=1
        if bbx==500 or collision ==True:
            state2 = 'ready2'
            bbx=0
    if state3=='fire3':
        
        bul(dddb4,bbbx4+20,bbby4+bby)

        collision = iscollision(pherox,pheroy,bbbx4,bbby4+bby)
        if collision == True:

            hello = "GREEN KNIGHT WON THE GAME"


        bby+=1
        if bby==500 or collision == True:
            state3 = 'ready3'
            bby=0
    


    ###############################################
    
    if state11=='fire11':
        
        bull(dddb11,bbbx11+20,bbby11-bbyy)


        collision = iscollision(herox,heroy,bbbx11,bbby11-bbyy)
        if collision == True:

            hello = "BLACK KNIGHT WON THE GAME"

        bbyy+=1
        if bbyy==500 or collision==True:
            state11 = 'ready11'
            bbyy=0
    
    if state12=='fire12':
        
        bull(dddb22,bbbx22+bbxx,bbby22+20)


        collision = iscollision(herox,heroy,bbbx22+bbxx,bbby22)
        if collision == True:

            hello = "BLACK KNIGHT WON THE GAME"

        bbxx+=1
        if bbxx==500 or collision==True:
            state12= 'ready12'
            bbxx=0
    
    if state23=='fire23':
        
        bull(dddb33,bbbx33-bbxx,bbby33+20)


        collision = iscollision(herox,heroy,bbbx33-bbxx,bbby33)
        if collision == True:

            hello = "BLACK KNIGHT WON THE GAME"


        bbxx+=1
        if bbxx==500 or collision==True:
            state23 = 'ready23'
            bbxx=0
    if state34=='fire34':
        
        bull(dddb44,bbbx44+20,bbby44+bbyy)

        collision = iscollision(herox,heroy,bbbx44,bbby44+bbyy)
        if collision == True:
            hello = "BLACK KNIGHT WON THE GAME"
        bbyy+=1
        if bbyy==500 or collision==True:
            state34 = 'ready34'
            bbyy=0
    
    ##############################################
  
    ####collision


    if collision ==True:
        
        if i==0:
            hit= hello
            i=1
        gameover(hit)
            
        
        
        


    hero(r_hero,herox,heroy)
    play2(m_pla2,pherox,pheroy)
    pygame.display.update()

