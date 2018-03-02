class Settings():
    def __init__(self):
        self.screen_width=1200
        self.screen_height=700
        self.bg_color=(0,0,0)
        self.ship_speed_factor = 1.5  #飞船的速度

        #子弹设置
        self.bullet_speed_factor = 2
        self.bullet_height = 20
        self.bullet_width = 10
        self.bullet_color =255,60,60

        #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_direction为1表示向右移
        self.fleet_direction = 1

