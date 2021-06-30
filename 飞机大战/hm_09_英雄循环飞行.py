import pygame

pygame.init()

screen = pygame.display.set_mode((480, 700))

bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))

hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 300))

pygame.display.update()

hero_rect = pygame.Rect(150, 300, 102, 126)
clock = pygame.time.Clock()

while True:
    clock.tick(60)

    hero_rect.y -= 1
    # 判断飞机的位置是否达到顶部
    if hero_rect.y <= -126:
        hero_rect.y = 700

    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    pygame.display.update()

pygame.quit()
