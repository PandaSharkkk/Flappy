import pygame, sys
from random import randint

def collide(player, obstacles):
    if bird_rect.top <= 0:
        bird_rect.top = 0

    if bird_rect.bottom >= 800:
        bird_rect.bottom = 800

    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom >= 500:
                screen.blit(pipe_surfbot, obstacle_rect)
            else:
                screen.blit(pipe_surftop, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > - 100]
        return obstacle_list
    else:
        return []

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Flappy')
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

pipe_surftop = pygame.image.load('pictures/pipe-green1.png').convert_alpha()
pipe_surfbot = pygame.image.load('pictures/pipe-green2.png').convert_alpha()

bird_surf = pygame.image.load('pictures/Fly1.png').convert_alpha()
bird_rect = bird_surf.get_rect(midbottom = (250, 300))
bird_gravity = 0

obstacle_rect_list = []

game_active = True

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                 bird_gravity = -10
        
        if event.type == obstacle_timer and game_active:
            randomint = randint(150, 450)
            obstacle_rect_list.append(pipe_surftop.get_rect(bottomleft = (900, randomint)))
            obstacle_rect_list.append(pipe_surfbot.get_rect(topleft = (900,  randomint + 200)))

    if game_active:
        screen.fill(250)
        bird_gravity += 0.5
        bird_rect.y += bird_gravity

        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        game_active = collide(bird_rect, obstacle_rect_list)

        screen.blit(bird_surf, bird_rect)

    
    pygame.display.update()
    clock.tick(60)
