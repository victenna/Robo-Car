import pygame,math,time
pygame.init()
from pygame.math import Vector2
screen = pygame.display.set_mode((1400, 900))
clock = pygame.time.Clock()
car2=pygame.image.load('car1.png')
angle2=0
u0,v0=205,610
Q=11
border=[0]*Q
images=['img03_.png','imgeе1.png','imgeе2.png','img1.png','imgeе4.png',\
        'img1.png','imgeе6.png','imgeе7.png','imgeе8.png',\
        'imgeе9.png','imgeе10.png']

for i in range(Q):
    border[i]=pygame.image.load(images[i])
    
X=[700,240,510,640,1100,1280,1250,1090,920,380,180]
Y=[450,500,370,380,130,120,180,350,370,770,690]
u,v=0,-5

border_rect=[0]*Q
Pos=[0]*Q
for i in range (Q):
    border_rect[i]=border[i].get_rect(center=(X[i],Y[i]))
    Pos[i]=Vector2(border_rect[i].center)
ddelta=[0]*Q
        
def turn():
    global u0,v0,CAR2_pos
    u=(3*math.sin(3.14*angle2/180))
    v=(3*math.cos(3.14*angle2/180))
    CAR2=pygame.transform.rotate(car2,angle2)
    u0,v0=u0-u,v0-v
    
def condition1(i,level,S,du,dv,a):
    global k,s,angle2,u0,v0
    if ddelta[i]<level:
        k=i    
    if k==i and s<=S:
        s=s+1
        angle2=angle2-5*a
        print('k=',k,'s=',s,'angle2=',angle2)
        turn()
    if k==i and s>S:
        u0=u0+du
        v0=v0+dv
s,k=0,0
while True:
    screen.fill((124,252,0))
    for i in range (1,Q):
        screen.blit(border[i],border_rect[i])
    screen.blit(border[0],border_rect[0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    CAR2=pygame.transform.rotate(car2,angle2)
    CAR2_rect=CAR2.get_rect(center=(u0,v0))
    CAR2_pos=Vector2(CAR2_rect.center)
    screen.blit(CAR2,CAR2_rect)
    
    for i in range(1,Q):
        ddelta[i]=pygame.math.Vector2.length(Pos[i]-CAR2_pos)
        
    if angle2==0:
        v0=v0-5
#-------------------------------------------------  
    condition1(1,50,10,4,-2,1)
#-----------------------------------------------------------        
    condition1(2,40,16,6,0.03,1)
#-------------------------------------------------------------
    condition1(3,55,20,5,-2.8,-1)
#---------------------------------------------------
    condition1(4,70,25,5,0,1)
#-------------------------------------------
    condition1(5,80,50,-3.8,5.3,1)
#--------------------------------------------------------------
    condition1(7,50,59,-6,1,1)
#------------------------------------------------------------
    condition1(8,50,63,-4,2.6,-1)
#------------------------------------------------------------
    condition1(9,70,72,-5,-1.6,1)
#--------------------------------------------------
    condition1(10,60,89,0.2,-1.5,1)
    if k==10 and s>89:
         angle2=0
#------------------------------------------------------------
    if (ddelta[1])<63 and k==10:
        s,k=0,1
    pygame.display.flip()
    clock.tick(10)
        
    
    

