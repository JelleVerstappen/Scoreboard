import pygame
from game import Game

WIDTH = 800
HEIGHT = 600

game = Game()
game.get_max_points()

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
                game.reset()
            elif event.key == pygame.K_RIGHT:
                game.score("A")
            elif event.key == pygame.K_LEFT:
                game.score("H")

    
    screen.fill("black")

    if game.sets_home == 3:
        Winnaar = "Thuis"
        text3 = font.render(f"{Winnaar} wint!", True, "white")
        xpos = WIDTH / 2 - text3.get_width() / 2
        ypos = HEIGHT / 2 - text3.get_height() / 2 + 100
        screen.blit(text3, (xpos, ypos))
        game.reset()
        
    if game.sets_away == 3:
        Winnaar = "Uit"
        text3 = font.render(f"{Winnaar} wint!", True, "white")
        xpos = WIDTH / 2 - text3.get_width() / 2
        ypos = HEIGHT / 2 - text3.get_height() / 2 + 100
        screen.blit(text3, (xpos, ypos))
        game.reset()
        

    text = font.render(f"Schalke {game.points_home} - {game.points_away} Chelsea", True, "white")
    text2 = font.render(f"{game.sets_home} - {game.sets_away}", True, "white")
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    screen.blit(text2, (WIDTH / 2 - text2.get_width() / 2, HEIGHT / 2 - text2.get_height() / 2 + 50))

    pygame.display.flip()
