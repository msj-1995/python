import pygame

pygame.init()

screen = pygame.display.set_mode((480, 700))

bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))

hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (0, 0))
# 可以在所有绘制工作绘制完成后同一调用update方法
pygame.display.update()

while True:
    pass

pygame.quit()