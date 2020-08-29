import pygame
import random
import os

pygame.mixer.init()

pygame.init()


#colours
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
mix=(220,230,230)

screen_width=900
screen_height=600
gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("snakes")
pygame.display.update()

bgimg=pygame.image.load('snake.jpg')
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()




clock=pygame.time.Clock()
font=pygame.font.SysFont(None,55)

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow,color,snake_list,Snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, Snake_size, Snake_size])

def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill(mix)

        text_screen("WELCOME TO SNAKES",black,220,250)
        text_screen("PRESS SPACE BAR TO PLAY", red, 190, 290)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load('Nagin.mp3')
                    pygame.mixer.music.play()
                    gameloop()
    pygame.display.update()
    clock.tick(60)



def gameloop():
    exit_game = False
    game_over = False
    Snake_x = 45
    Snake_y = 55
    Snake_size = 10
    Velocity_x = 0
    Velocity_y = 0
    score = 0
    fps = 10
    food_x = 200
    food_y = 200
    init_vel = 10
    snake_list = []
    snake_len = 1
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()
    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)


            text_screen("game over, press enter to continue",red,screen_width/4,screen_height/2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        pygame.mixer.music.stop()

                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        Velocity_x=init_vel
                        Velocity_y=0
                    if event.key==pygame.K_LEFT:
                        Velocity_x=-init_vel
                        Velocity_y=0
                    if event.key==pygame.K_UP:
                        Velocity_x = 0
                        Velocity_y = -init_vel
                    if event.key==pygame.K_DOWN:
                        Velocity_x = 0
                        Velocity_y = init_vel

            Snake_x=Snake_x+Velocity_x
            Snake_y=Snake_y+Velocity_y

            if abs(Snake_x-food_x)<10 and abs(Snake_y-food_y)<10:
                score = score+10
                fps=fps+2
                if score>int(hiscore):
                    hiscore=score


                food_x = random.randint(20, screen_width -20)
                food_y = random.randint(20, screen_height - 20)
                snake_len=snake_len+2

            gameWindow.fill(white)
            gameWindow.blit(bgimg,(0,0))
            text_screen("score:" + str(score)+"     Hi-score:"+str(hiscore), red, 5, 5
                        )
            pygame.draw.circle(gameWindow, red, [food_x,food_y],7)

            head=[]
            head.append(Snake_x)
            head.append(Snake_y)
            snake_list.append(head)
            if len(snake_list)>snake_len:
                del snake_list[0]
            plot_snake(gameWindow, red, snake_list, Snake_size)
            #last wale element ko chodkar kisi bhi element se head bhd gya ,game over hojayega
            if head in snake_list[:-1]:
                game_over=True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
            if Snake_x<0 or Snake_x>screen_width or Snake_y<0 or Snake_y>screen_height:
                game_over=True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()

welcome()