import pygame

WIDTH = 800
HEIGHT = 600

score_thuis = 0
score_uit = 0
sets_thuis = 0
sets_uit = 0
set_score = 5

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.SysFont("comicsansms", 24)

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
                set_score = 25
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

    screen.fill("black")

    if sets_thuis == 3:
        Winnaar = "Thuis"
        text3 = font.render(f"{Winnaar} wint!", True, "white")
        xpos = WIDTH / 2 - text3.get_width() / 2
        ypos = HEIGHT / 2 - text3.get_height() / 2 + 100
        screen.blit(text3, (xpos, ypos))
        
    if sets_uit == 3:
        Winnaar = "Uit"
        text3 = font.render(f"{Winnaar} wint!", True, "white")
        xpos = WIDTH / 2 - text3.get_width() / 2
        ypos = HEIGHT / 2 - text3.get_height() / 2 + 100
        screen.blit(text3, (xpos, ypos))



    label = "Hallo"
    text = font.render(f"Schalke {score_thuis} - {score_uit} Chelsea", True, "white")
    text2 = font.render(f"{sets_thuis} - {sets_uit}", True, "white")
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    screen.blit(text2, (WIDTH / 2 - text2.get_width() / 2, HEIGHT / 2 - text2.get_height() / 2 + 50))

    pygame.display.flip()
