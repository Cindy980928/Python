import pygame
class Ship():
    def __init__(self,ai_settings,screen):
        self.screen=screen
        self.image=pygame.image.load('plane.png')  #加载图像，返回一个表示飞船的surface
        self.image=pygame.transform.scale(self.image, (50,50))    #缩放
        self.rect=self.image.get_rect()   #获取相应surface的属性rect
        self.screen_rect=screen.get_rect()

        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        self.ai_settings = ai_settings

        #移动标志
        self.moving_right = False
        self.moving_left = False

        #在飞船的属性center中存储小数值
        self.center=float(self.rect.centerx)


    def update(self):
        """根据移动标志调整飞船的位置;限制飞船的活动范围"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor

    #根据self.center更新rect对象
           # self.rect.centerx = self.center
    def blitme(self):

        self.screen.blit(self.image,self.rect)
        #将背景图画上去，blit是个重要函数，第一个参数为一个Surface对象，第二个为左上角位置。