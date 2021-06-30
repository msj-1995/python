import pygame
from plane_sprites import *

screen = pygame.display.set_mode((480, 700))

bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 300))
pygame.display.update()

clock = pygame.time.Clock()
hero_rect = pygame.Rect(150, 300, 102, 126)

# 创建敌机的精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", 2)

# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)

while True:
    clock.tick(60)
    # 监听事件
    for event in pygame.event.get():
        # 判断事件类型是否是退出按钮
        if event.type == pygame.QUIT:
            print("游戏退出.....")
            # 卸载pygame的所有模块
            pygame.quit()
            # 退出游戏,直接终止当前正在执行的程序
            exit()
    hero_rect.y -= 1
    if hero_rect.y <= 0:
        hero_rect.y = 700
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 让精灵组调用两个方法，update和draw
    enemy_group.update()
    # 在screen上绘制精灵组中所有的精灵
    enemy_group.draw(screen)

    pygame.display.update()

pygame.quit()
