import arcade
import sprites
import random
import ctypes

c_functions = ctypes.CDLL("./SO/cFunctions.so")

game_playing = ctypes.c_uint(0)

class Window(arcade.Window):
    def __init__(self, width: int, height: int, title: str):
        super().__init__(width=width, height=height, title=title)

        self.player_sprite_list = None
        self.enemy_sprite_list = None
        self.player_laser_list = None
        self.enemy_laser_list = None

    def setup(self):
        self.background_image = arcade.Sprite("./PNG/background.png", center_x=self.width/2, center_y=self.height/2)

        self.player_sprite_list = arcade.SpriteList()
        self.enemy_sprite_list = arcade.SpriteList()
        self.player_laser_list = arcade.SpriteList()
        self.enemy_laser_list = arcade.SpriteList()

        self.player = sprites.Player("./PNG/player.png", 0.5, self.width/2, self.height/20, 100)
        self.player_sprite_list.append(self.player)

        self.health_text_color = arcade.color.GREEN

        self.enemy = sprites.Enemy("./PNG/enemy.png", 0.5, self.width/2, self.height + 100)
        self.enemy_sprite_list.append(self.enemy)

        sprites.enemy_speed = 0.3

    def on_key_press(self, key, modifiers):
        return_value = c_functions.keyPressed(ctypes.c_uint(key), ctypes.byref(self.player.move_left), ctypes.byref(self.player.move_right), ctypes.byref(game_playing))
        if return_value == 1: self.setup()
        elif return_value == 2: self.player.shoot(self)

    def on_key_release(self, key, modifiers):
        c_functions.keyReleased(ctypes.c_uint(key), ctypes.byref(self.player.move_left), ctypes.byref(self.player.move_right))

    def on_draw(self):
        arcade.start_render()
        self.background_image.draw()

        if game_playing:
            self.player_sprite_list.draw()
            self.enemy_sprite_list.draw()
            self.player_laser_list.draw()
            self.enemy_laser_list.draw()

            arcade.draw_text(f"Score: {self.player.score}", self.width/30, self.height/15, arcade.color.WHITE, 18)
            arcade.draw_text(f"Health: {self.player.health.value}", self.player.center_x - 35, self.player.center_y - 30, self.health_text_color, 10)
            arcade.draw_text(f"Bullets: {self.player.bullets}", self.width - 115, self.height/15, arcade.color.WHITE, 18)
        
        else:
            arcade.draw_text("Press enter to play", self.width / 2 - 100, self.height / 2, arcade.color.WHITE, 18)
            arcade.draw_text(f"Score: {self.player.score}", self.width/2 - 50, self.height/2 - 50, arcade.color.WHITE, 18)

    def update(self, delta_time):
        if game_playing:
            c_functions.setScore(self.player.score);

            self.player_sprite_list.update()
            self.enemy_sprite_list.update()
            self.player_laser_list.update()
            self.enemy_laser_list.update()

            for laser in self.player_laser_list:
                player_laser_enemy_hitlist = arcade.check_for_collision_with_list(laser, self.enemy_sprite_list)

                if len(player_laser_enemy_hitlist) > 0:
                    laser.remove_from_sprite_lists()

                    for enemy in player_laser_enemy_hitlist:
                        enemy.center_x = random.randint(20, self.width - 20)
                        enemy.center_y = random.randint(self.height + 30, 800)
                        self.player.score += 1
                        self.player.bullets += 1

                        if self.player.score % 5 == 0:
                            another_enemy = sprites.Enemy("./PNG/enemy.png", 0.5, random.randint(0, self.width), random.randint(self.height + 30, 800))
                            self.enemy_sprite_list.append(another_enemy)
                            sprites.enemy_speed += 0.05

            for enemy in self.enemy_sprite_list:
                if random.randint(0, 100) == 0 and enemy.center_y < self.height:
                    enemy.shoot(self)
            
            for enemy_laser in self.enemy_laser_list:
                enemy_laser_player_hitlist = arcade.check_for_collision_with_list(enemy_laser, self.player_sprite_list)

                if len(enemy_laser_player_hitlist) > 0:
                    enemy_laser.remove_from_sprite_lists()
                    return_value = c_functions.subtractHealth(ctypes.byref(self.player.health), ctypes.byref(game_playing), ctypes.c_int(self.player.score))
                    if return_value == 1: self.health_text_color = arcade.color.GREEN
                    elif return_value == 2: self.health_text_color = arcade.color.YELLOW
                    elif return_value == 3: self.health_text_color = arcade.color.RED   
            
            player_enemy_hitlist = arcade.check_for_collision_with_list(self.player, self.enemy_sprite_list)
            if len(player_enemy_hitlist) > 0: self.player.score += 1; c_functions.playerCrashIntoEnemy(ctypes.byref(game_playing), ctypes.c_int(self.player.score));