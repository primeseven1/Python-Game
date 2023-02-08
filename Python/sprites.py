import arcade
import ctypes
import window

# I could not figure out how to make a static variable
enemy_speed = 0

class Laser(arcade.Sprite):
    def __init__(self, filename: str, scale: float, center_x: int, center_y: int, velocity: float, enemy: bool):
        super().__init__(filename=filename, scale=scale, center_x=center_x, center_y=center_y)

        self.velocity = velocity
        self.enemy = enemy
    
    def update(self):
        if window.game_playing:
            if self.enemy:
                self.center_y -= self.velocity
            else:
                self.center_y += self.velocity

            if (self.bottom > 600 or self.top < 0):
                self.remove_from_sprite_lists()

class Player(arcade.Sprite):
    def __init__(self, filename: str, scale: float, center_x: int, center_y: int, health: int):
        super().__init__(filename=filename, scale=scale, center_x=center_x, center_y=center_y)

        self.move_left = ctypes.c_int(0)
        self.move_right = ctypes.c_int(0)

        self.health = ctypes.c_int(health)

        self.bullets = 5
        self.score = 0

    def shoot(self, window):
        if self.bullets:
            laser = Laser("./PNG/player_laser.png", 1, self.center_x, self.center_y + 25, 3, False)
            window.player_laser_list.append(laser)
            self.bullets -= 1

    def update(self):
        if self.move_left and self.center_x > 0 + 25:
            self.center_x -= 3
        if self.move_right and self.center_x < 800 - 25:
            self.center_x += 3

class Enemy(arcade.Sprite):
    def __init__(self, filename: str, scale: float, center_x: int, center_y: int):
        super().__init__(filename=filename, scale=scale, center_x=center_x, center_y=center_y)
        

    def shoot(self, window):
            laser = Laser("./PNG/enemy_laser.png", 1, self.center_x, self.center_y -25, 3, True)
            window.enemy_laser_list.append(laser)

    def update(self):
        if window.game_playing:
            self.center_y -= enemy_speed
        
        window.c_functions.enemyPastPlayer(window.game_playing_ptr, ctypes.c_float(self.center_y))