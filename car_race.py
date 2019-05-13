import pygame
pygame.init()
gray=(119,118,110)
black=(0,0,0)
red=(255,0,0)
green=(0,200,0)
blue=(0,0,200)
bright_gray=(226,226,226)
white=(255,255,255)
bright_red=(255,0,0)
bright_green=(0,255,0)
bright_blue=(0,0,255)
display_width=800
display_height=600
import time
import random


gamedisplays=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("car game")
clock=pygame.time.Clock()
carimg=pygame.image.load('car1.png')
backgroundpic=pygame.image.load("download12.jpg")
bg=pygame.image.load("background1.png")
yellow_strip=pygame.image.load("strip.png")
strip=pygame.image.load("strip.jpg")
intro_background=pygame.image.load("background.jpg")
instruction_background=pygame.image.load("background2.jpg")
instruction_background=pygame.transform.scale(instruction_background,(display_width,display_height))
car_width=56
pause=False

def intro_loop():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(intro_background,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',115)
        introduction()
        pygame.display.update()
        clock.tick(50)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gamedisplays,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            if action=="play":
                countdown()
            elif action=="quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action=="intro":
                introduction()
            elif action=="menu":
                intro_loop()
            elif action=="pause":
                paused()
            elif action=="unpause":
                unpaused()


    else:
        pygame.draw.rect(gamedisplays,ic,(x,y,w,h))
    smalltext=pygame.font.Font("freesansbold.ttf",20)
    textsurf,textrect=text_objects(msg,smalltext)
    textrect.center=((x+(w/2)),(y+(h/2)))
    gamedisplays.blit(textsurf,textrect)


def introduction():
    introduction=True
    while introduction:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(instruction_background,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',80)
        smalltext=pygame.font.Font('freesansbold.ttf',20)
        mediumtext=pygame.font.Font('freesansbold.ttf',40)
        textSurf,textRect=text_objects("This is a car game in which you need to dodge the coming cars",smalltext)
        textRect.center=((380),(155))
        TextSurf,TextRect=text_objects("INSTRUCTION",largetext)
        TextRect.center=((400),(100))
        gamedisplays.blit(TextSurf,TextRect)
        gamedisplays.blit(textSurf,textRect)
        stextSurf,stextRect=text_objects("ARROW LEFT : TO MOVE LEFT",smalltext)
        stextRect.center=((150),(400))
        hTextSurf,hTextRect=text_objects("ARROW RIGHT : TO MOVE RIGHT" ,smalltext)
        hTextRect.center=((165),(450))
        sTextSurf,sTextRect=text_objects("CONTROLS",mediumtext)
        sTextRect.center=((350),(300))
        gamedisplays.blit(sTextSurf,sTextRect)
        gamedisplays.blit(stextSurf,stextRect)
        gamedisplays.blit(hTextSurf,hTextRect)
        button("START",600,520,100,50,green,bright_green,"play")
        pygame.display.update()
        clock.tick(30)
def paused():
    global pause
    while pause:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            gamedisplays.blit(instruction_background,(0,0))
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("PAUSED",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            button("CONTINUE",150,450,150,50,green,bright_green,"unpause")
            button("RESTART",350,450,150,50,blue,bright_blue,"play")
            button("MAIN MENU",550,450,200,50,red,bright_red,"menu")
            pygame.display.update()
            clock.tick(30)

def unpaused():
    global pause
    pause=False

def countdown_background():
    font=pygame.font.SysFont(None,25)
    x=(display_width*0.45)
    y=(display_height*0.8)
    gamedisplays.blit(yellow_strip,(400,100))
    gamedisplays.blit(yellow_strip,(400,200))
    gamedisplays.blit(yellow_strip,(400,300))
    gamedisplays.blit(yellow_strip,(400,400))
    gamedisplays.blit(yellow_strip,(400,100))
    gamedisplays.blit(yellow_strip,(400,500))
    gamedisplays.blit(yellow_strip,(400,0))
    gamedisplays.blit(yellow_strip,(400,600))
    gamedisplays.blit(strip,(120,200))
    gamedisplays.blit(strip,(120,0))
    gamedisplays.blit(strip,(120,100))
    gamedisplays.blit(strip,(680,100))
    gamedisplays.blit(strip,(680,0))
    gamedisplays.blit(strip,(680,200))
    gamedisplays.blit(carimg,(x,y))
    score=font.render("Score : 0",True,black)
    gamedisplays.blit(score,(20,80))
    button("Pause",680,0,120,50,white,bright_gray,"pause")

def countdown():
    countdown=True
    while countdown:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            gamedisplays.blit(bg,(0,0))
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("3",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.blit(bg,(0,0))
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("2",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.blit(bg,(0,0))
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("1",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.blit(bg,(0,0))
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("GO!!!",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            game_loop()

def obstacle(obs_startx,obs_starty,obs):
    if obs==0:
        obs_pic=pygame.image.load("car.png")
    elif obs==1:
        obs_pic=pygame.image.load("car1.png")
    elif obs==2:
        obs_pic=pygame.image.load("car2.png")
    elif obs==3:
        obs_pic=pygame.image.load("car4.png")
    elif obs==4:
        obs_pic=pygame.image.load("car5.png")
    elif obs==5:
        obs_pic=pygame.image.load("car6.png")
    elif obs==6:
        obs_pic=pygame.image.load("car7.png")
    gamedisplays.blit(obs_pic,(obs_startx,obs_starty))

def score_system(passed,score):
    font=pygame.font.SysFont(None,25)
    score=font.render("Score : "+str(score),True,black)
    gamedisplays.blit(score,(20,80))
def text_objects(text,font):
    
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()

def message_display(text):
    
    largetext=pygame.font.Font("freesansbold.ttf",80)
    textsurf,textrect=text_objects(text,largetext)
    textrect.center=((display_width/2),(display_height/2))
    gamedisplays.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()

def crash():
    
    message_display("YOU CRASHED")

def background():
    gamedisplays.blit(yellow_strip,(400,0))
    gamedisplays.blit(yellow_strip,(400,100))
    gamedisplays.blit(yellow_strip,(400,200))
    gamedisplays.blit(yellow_strip,(400,300))
    gamedisplays.blit(yellow_strip,(400,400))
    gamedisplays.blit(yellow_strip,(400,500))
    

def car(x,y):
    
    gamedisplays.blit(carimg,(x,y))

def game_loop():
    
    global pause
    x=(display_width*0.45)
    y=(display_height*0.8)
    x_change=0
    obstacle_speed=9
    obs=0
    y_change=0
    obs_startx=random.randrange(200,(display_width-200))
    obs_starty=-750
    obs_width=56
    obs_height=125
    passed=0
    level=0
    score=0
    y2=7
    fps=120
    bumped=False
    while not bumped:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                if event.key==pygame.K_RIGHT:
                    x_change=5
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0

        x+=x_change
        pause=True
        gamedisplays.blit(bg,(0,0))
        rel_y=y2%backgroundpic.get_rect().width
        if rel_y<800:
            gamedisplays.blit(yellow_strip,(400,rel_y))
            gamedisplays.blit(yellow_strip,(400,rel_y+100))
            gamedisplays.blit(yellow_strip,(400,rel_y+200))
            gamedisplays.blit(yellow_strip,(400,rel_y+300))
            gamedisplays.blit(yellow_strip,(400,rel_y+400))
            gamedisplays.blit(yellow_strip,(400,rel_y+500))
            gamedisplays.blit(yellow_strip,(400,rel_y-100))
            gamedisplays.blit(strip,(120,rel_y-200))
            gamedisplays.blit(strip,(120,rel_y+20))
            gamedisplays.blit(strip,(120,rel_y+30))
            gamedisplays.blit(strip,(680,rel_y-100))
            gamedisplays.blit(strip,(680,rel_y+20))
            gamedisplays.blit(strip,(680,rel_y+30))

        y2+=obstacle_speed
        obs_starty-=(obstacle_speed/4)
        obstacle(obs_startx,obs_starty,obs)
        obs_starty+=obstacle_speed
        car(x,y)
        score_system(passed,score)
        if x>690-car_width or x<110:
            crash()
        if x>display_width-(car_width+110) or x<110:
            crash()
        if obs_starty>display_height:
            obs_starty=0-obs_height
            obs_startx=random.randrange(170,(display_width-170))
            obs=random.randrange(0,7)
            passed=passed+1
            score=passed*10
            if int(passed)%10==0:
                level=level+1
                obstacle_speed+=4
                largetext=pygame.font.Font("freesansbold.ttf",80)
                textsurf,textrect=text_objects("LEVEL"+str(level),largetext)
                textrect.center=((display_width/2),(display_height/2))
                gamedisplays.blit(textsurf,textrect)
                pygame.display.update()
                time.sleep(3)
        if y<obs_starty+obs_height:
            if x > obs_startx and x < obs_startx + obs_width or x+car_width > obs_startx and x+car_width < obs_startx+obs_width:
                crash()
        button("Pause",680,0,120,50,white,bright_gray,"pause")
        if(score==10):
            pause=True
            while pause :
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        quit()
                        sys.exit()
                gamedisplays.blit(instruction_background,(0,0))
                largetext=pygame.font.Font('freesansbold.ttf',115)
                TextSurf,TextRect=text_objects("YOU WON ! ",largetext)
                TextRect.center=((display_width/2),(display_height/2))
                gamedisplays.blit(TextSurf,TextRect)
                button("RESTART",150,450,150,50,blue,bright_blue,"play")
                button("MAIN MENU",350,450,200,50,red,bright_red,"menu")
                pygame.display.update()
                clock.tick(60)
                
        pygame.display.update()
        clock.tick(60)
intro_loop()
game_loop()
pygame.quit()
quit()
