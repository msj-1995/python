import pygame

pygame.init()

screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1.加载图像数据
bg = pygame.image.load("./images/background.png")

# 2.blit指定绘制位置:在screen的（0，0）位置绘制
screen.blit(bg, (0, 0))

# 3.更行屏幕
pygame.display.update()

while True:
    pass

pygame.quit()
