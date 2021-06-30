import pygame

pygame.init()
screen = pygame.display.set_mode((480,700))

bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))

hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 500))

pygame.display.update()

# 创建一个始终对象
clock = pygame.time.Clock()

# 游戏循环，意味着游戏的正式开始
i = 0
while True:
    # 指定循环体内部代码执行的频率
    clock.tick(60)
    print(i)
    i += 1

pygame.quit()
