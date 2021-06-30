import pygame

screen = pygame.display.set_mode((480, 700))

bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))

hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 300))

pygame.display.update()

clock = pygame.time.Clock()

# 1. 定义rect记录飞机的位置
hero_rect = pygame.Rect(150, 300, 102, 126)

while True:
    clock.tick(60)

    # 2. 修改飞机的位置
    hero_rect.y -= 1

    # 3.调用blit方法绘制图像
    # 重新绘制背景，遮挡以前的图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 4. 更新显示
    pygame.display.update()

pygame.quit()
