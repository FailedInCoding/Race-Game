import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((1440,1000))
gameDisplay.fill(black)



pixAr = pygame.PixelArray(gameDisplay)
pixAr[100] [200] = green

pygame.draw.line(gameDisplay, blue, (100,350), (450, 600), 5)

pygame.draw.rect(gameDisplay, red, (1000,500,350,350))

pygame.draw.circle(gameDisplay, white, (600,300), 250)

pygame.draw.polygon(gameDisplay, green, ((25,150),(100, 125), (250, 375), (400,25)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit
            
        pygame.display.update()