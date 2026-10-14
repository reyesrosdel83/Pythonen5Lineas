import pygame, random
    pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont("monospace", 18)
chars = [chr(i) for i in range(33, 126)]
y = [0]*80

while True:
    screen.fill((0,0,0,20))
    for i, pos in enumerate(y):
        txt = font.render(random.choice(chars), True, (0,255,70))
        screen.blit(txt, (i*10, pos))
        y[i] = 0 if pos > 600 and random.random() > 0.975 else pos + 15
    pygame.display.flip()
    pygame.time.delay(50)