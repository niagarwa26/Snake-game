import pygame
import random
pygame.init()

#colours
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

screen_width=900
screen_height=600

gameWindow = pygame.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  uu=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("snakes")
pygame.display.update()

exit_game=False
game_over=False
Snake_x=45
Snake_y=55
Snake_size=10
Velocity_x=0
Velocity_y=0
score=0
fps=15
food_x=200
food_y=200


clock=pygame.time.Clock()


while not exit_game:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            exit_game=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                Velocity_x=10
                Velocity_y=0
            if event.key==pygame.K_LEFT:
                Velocity_x=-10
                Velocity_y=0
            if event.key==pygame.K_UP:
                Velocity_x = 0
                Velocity_y = -10
            if event.key==pygame.K_DOWN:
                Velocity_x = 0
                Velocity_y = 10
    Snake_x=Snake_x+Velocity_x
    Snake_y=Snake_y+Velocity_y

    if abs(Snake_x-food_x)<6 and abs(Snake_y-food_y)<6:
        score = score+1
        print("score:",score)
        food_x = random.randint(20, screen_width -20)
        food_y = random.randint(20, screen_height - 20)

    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, red, [food_x, food_y, Snake_size, Snake_size])
    pygame.draw.rect(gameWindow,black,[Snake_x,Snake_y,Snake_size,Snake_size])
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
quit()