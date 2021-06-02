import pygame
import configparser

config = configparser.ConfigParser()
config.read("config.ini") 
ploegnaam_thuis = config["TeamA"]["naam"] 
logo_A = config["TeamA"]["logo"]
ploegnaam_uit = config["TeamB"]["naam"]
logo_B = config["TeamB"]["logo"]
font_type = config["Preferences"]["font"]
font_size = config["Preferences"].getint("font_size")
font_size_sets = config["Preferences"].getint("font_size_sets")
text_colour = config["Preferences"]["text_colour"]
background = config["Preferences"]["background"]

WIDTH = 800
HEIGHT = 600

score_thuis = 0
score_uit = 0
sets_thuis = 0
sets_uit = 0
set_score = 5

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.SysFont(font_type, font_size)
font_sets = pygame.font.SysFont(font_type, font_size_sets)
logo_thuis = pygame.image.load("Maaseik.png")
logo_uit = pygame.image.load("Roeselare.png")

logo_thuis = pygame.transform.smoothscale(logo_thuis,(200, 200))
logo_uit = pygame.transform.smoothscale(logo_uit,(200, 200))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                score_thuis = 0
                score_uit = 0
                sets_thuis = 0
                sets_uit = 0
                set_score = 5
            elif event.key == pygame.K_RIGHT:
                score_thuis = score_thuis + 1
            elif event.key == pygame.K_LEFT:
                score_uit = score_uit + 1

    if score_thuis >= set_score and score_thuis >= score_uit + 2:
        score_thuis = 0
        score_uit = 0
        sets_thuis = sets_thuis + 1

    if score_uit >= set_score and score_uit >= score_thuis + 2:
        score_uit = 0
        score_thuis = 0
        sets_uit = sets_uit + 1

    screen.fill(background)

    if sets_thuis == 3:
        text3 = font.render(f"{ploegnaam_thuis} wint!", True, text_colour)
        xpos = WIDTH / 2 - text3.get_width() / 2
        ypos = HEIGHT / 2 - text3.get_height() / 2 + 100
        screen.blit(text3, (xpos, ypos))
        
    if sets_uit == 3:
        text3 = font.render(f"{ploegnaam_uit} wint!", True, text_colour)
        xpos = WIDTH / 2 - text3.get_width() / 2
        ypos = HEIGHT / 2 - text3.get_height() / 2 + 100
        screen.blit(text3, (xpos, ypos))
    
    text_thuisploeg = font.render(f"{ploegnaam_thuis}" , True, text_colour)
    text_uitploeg = font.render(f"{ploegnaam_uit}", True, text_colour)

    score_home = font.render(f"{score_thuis}", True, text_colour)
    score_away = font.render(f"{score_uit}", True, text_colour)
    sets_thuisploeg = font_sets.render(f"{sets_thuis} ", True, text_colour)
    sets_uitploeg = font_sets.render(f"{sets_uit}", True, text_colour)

    screen.blit(text_thuisploeg, (30 , HEIGHT - 300))
    screen.blit(text_uitploeg, (WIDTH - 30 - text_uitploeg.get_width(), HEIGHT - 300))
    screen.blit(logo_thuis, (20 , text_thuisploeg.get_height() -  5))
    screen .blit(logo_uit, (WIDTH - logo_uit.get_width() - 20, text_uitploeg.get_height() - 5))

    screen.blit(score_home, (WIDTH/2 - 50, HEIGHT - 200))
    screen.blit(score_away, (WIDTH/2 + 50, HEIGHT - 200))
    screen.blit(sets_thuisploeg, (WIDTH/2 - 20, HEIGHT - 150))
    screen.blit(sets_uitploeg, (WIDTH/2 + 20, HEIGHT - 150))

    

    pygame.display.flip()
