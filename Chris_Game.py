import arcade
import random

# Window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

# Scaling
SCALE_PLAYER_ENEMY = 0.5
MOUSE_SCALE = 0.1
BUTTON_SCALE = 1
LASER_SCALE = 1

# Movement Speed
MOVEMENT_SPEED = 5.5
BULLET_SPEED = 7

INITIAL_ENEMY_COUNT = 1

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        # Background image sprite (Nothing to do with the game)
        self.background_image = None

        # Sprite lists
        self.player_list = None
        self.enemy_list = None
        self.player_laser_list = None
        self.enemy_laser_list = None
        self.play_button = None

        # Mouse sprite list
        self.mouse_sprite = None

        # Determines whether the game is playing/game over
        self.game_playing = False
        self.game_over = False

        # Scores and other values
        self.score = 0
        self.bullet_count = 0
        self.reload_count = 0
    
    def setup(self):
        # Mouse set to not visible
        self.set_mouse_visible(False)

        # Background Image
        self.background_image = arcade.SpriteList()

        # Sprite Lists
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.player_laser_list = arcade.SpriteList()
        self.enemy_laser_list = arcade.SpriteList()
        self.play_button = arcade.SpriteList()

        # Mouse Sprite List
        self.mouse_sprite = arcade.SpriteList()

        # Bullet Count + Reloading
        self.bullet_count = 5
        self.reload_count = 2
        
        # Enemy speed moving down
        self.enemy_speed = 0.5

        # Background Image (Nothing to do with the game)
        background = arcade.Sprite("stars.png")

        background.center_x = SCREEN_WIDTH/2
        background.center_y = SCREEN_HEIGHT/2

        self.background_image.append(background)

        # Mouse Pointer
        self.mouse = arcade.Sprite("mouse_pointer.png", MOUSE_SCALE)

        self.mouse.center_x = SCREEN_WIDTH/2
        self.mouse.center_y = SCREEN_HEIGHT/2

        self.mouse_sprite.append(self.mouse)

        # Play Button (Used for menu and the game over screens)
        playbutton = arcade.Sprite("playbutton.png", BUTTON_SCALE)

        playbutton.center_x = SCREEN_WIDTH/2
        playbutton.center_y = SCREEN_HEIGHT/2

        self.play_button.append(playbutton)

        # Player
        self.player = arcade.Sprite("player.png", SCALE_PLAYER_ENEMY)

        self.player.center_x = SCREEN_WIDTH/2
        self.player.center_y = SCREEN_HEIGHT/15

        self.player_list.append(self.player)

        self.moving_left = False
        self.moving_right = False

        self.player_health = 100

        # Enemy

        for i in range(INITIAL_ENEMY_COUNT):
            self.enemy = arcade.Sprite("enemy.png", SCALE_PLAYER_ENEMY)

            self.enemy.center_x = SCREEN_WIDTH/2
            self.enemy.center_y = random.randrange(SCREEN_HEIGHT + 30, 800)

            self.enemy_list.append(self.enemy)           

    def on_draw(self):
        arcade.start_render()
        self.background_image.draw()

        # Colors of text for the health of the player
        if self.player_health >= 67:
            color = arcade.color.GREEN
        elif 66 >= self.player_health >= 40:
            color = arcade.color.YELLOW
        else:
            color = arcade.color.RED

        if self.game_playing == False and self.game_over == False:
            # Menu Screen
            self.menu()
            self.play_button.draw()
        elif self.game_over == True:
            arcade.draw_text(self.reason, SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT-200, arcade.color.WHITE, 30)
            arcade.draw_text(f"Score: {self.score}", SCREEN_WIDTH/2.35, SCREEN_HEIGHT-250, arcade.color.WHITE, 30)
            self.play_button.draw()
        else:
            self.player_list.draw()
            self.player_laser_list.draw()
            self.enemy_list.draw()
            self.enemy_laser_list.draw()
            arcade.draw_text(f"Score: {self.score}", 20,20, arcade.color.WHITE, 20)
            arcade.draw_text(f"Bullets: {self.bullet_count}", self.player.center_x - 30 , 80, arcade.color.WHITE, 12)
            arcade.draw_text(f"Health: {self.player_health}", self.player.center_x - 30 , 10, color, 12)

            # Set back to this reason after restarting the game
            self.reason = "  You died"
        
        # Drawn last to allow it to overlap over objects
        self.mouse_sprite.draw()

    def on_key_press(self, key, modifiers):
        # Fullscreen
        if key == arcade.key.F11:
            self.set_fullscreen(True)
        if key == arcade.key.ESCAPE:
            self.set_fullscreen(False)  

        # So that you can't do stuff while in the menu screen
        if self.game_playing == True:
            # Move left/right
            if key == arcade.key.A or key == arcade.key.LEFT:
                self.moving_left = True
            if key == arcade.key.D or key == arcade.key.RIGHT:
                self.moving_right = True
            
            # Reloading
            if self.reload_count > 0 and self.bullet_count != 5:
                if key == arcade.key.R:
                    self.bullet_count = 5
                    self.reload_count -= 1
            
            # Shooting
            if key == arcade.key.SPACE:
                # Player Lasers
                if self.bullet_count > 0:
                    self.player_laser = arcade.Sprite("player_laser.png", LASER_SCALE)
                    self.player_laser.center_x = self.player.center_x
                    self.player_laser.center_y = self.player.center_y + 30

                    self.player_laser.change_y = BULLET_SPEED

                    self.player_laser_list.append(self.player_laser)

                    self.bullet_count -= 1
    
    def on_key_release(self, key, modifiers):
        if self.game_playing == True:
            # Stops the player from moving when the key is released
            if key == arcade.key.A or key == arcade.key.LEFT:
                self.moving_left = False
            if key == arcade.key.D or key == arcade.key.RIGHT:
                self.moving_right = False
    
    def on_mouse_motion(self, x, y, dx, dy):
        # Sets the mouse sprite to the mouse coordinates
        self.mouse.center_x = x
        self.mouse.center_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        # This makes it so when you click inside of the box, the game will know the game is currently playing
        if self.game_playing == False or self.game_over == True:
            if 372 < self.mouse.center_x < 640 and 286 < self.mouse.center_y < 395:
                self.game_over = False
                self.game_playing = True
                self.score = 0

    def update(self, delta_time):
        if self.game_playing == True:
            # Moving
            if self.moving_left == True:
                self.player.center_x -= MOVEMENT_SPEED

                # Stops the player from going off screen
                if self.player.center_x <= 25:
                    self.player.center_x = 25

            if self.moving_right == True:
                self.player.center_x += MOVEMENT_SPEED
                
                # Also stops the player from going off screen
                if self.player.center_x >= SCREEN_WIDTH-25:
                    self.player.center_x = SCREEN_WIDTH-25
            
            # Updating sprite lists
            self.player_laser_list.update()
            self.enemy_list.update()
            self.enemy_laser_list.update()

            for self.enemy in self.enemy_list:
                # Enemies moving down
                self.enemy.center_y -= self.enemy_speed

                # Enemies randomly shoot
                self.odds = 150

                adj_odds = int(self.odds * (1/60) / delta_time)

                if self.enemy.center_y <= 700:
                    if random.randrange(adj_odds) == 0:
                        self.enemy_laser = arcade.Sprite("enemy_laser.png", LASER_SCALE)
                        self.enemy_laser.center_x = self.enemy.center_x
                        self.enemy_laser.top = self.enemy.bottom
                        self.enemy_laser.change_y = -BULLET_SPEED
                        self.enemy_laser_list.append(self.enemy_laser)
                
                # Game over if one of the enemies passes the player
                if self.enemy.center_y <= 0:
                    self.player_health -= 100
                    self.reason = "An enemy got past you"

            for self.player_laser in self.player_laser_list:
                # Checks for collisions with the player lasers and the enemy
                laser_enemy_hitlist = arcade.check_for_collision_with_list(self.player_laser, self.enemy_list)

                if len(laser_enemy_hitlist) > 0:
                    self.player_laser.remove_from_sprite_lists()
                
                # Generates a random x and y for the enemies after being hit
                for self.enemy in laser_enemy_hitlist:
                    self.enemy.center_x = random.randrange(20, SCREEN_WIDTH - 20)
                    self.enemy.center_y = random.randrange(SCREEN_HEIGHT + 30, 800)
                    self.score += 1

                    # Every time you get 5 points, enemies get faster
                    if self.score % 5 == 0:
                        self.enemy_speed += 0.05

                    # Maximum amount of bullets is 5
                    if self.bullet_count < 5:
                        self.bullet_count += 1
                
                    # Adds enemies as your score gets higher
                    if self.score % 5 == 0 and len(self.enemy_list) < 12:
                        self.enemy = arcade.Sprite("enemy.png", SCALE_PLAYER_ENEMY)

                        self.enemy.center_x = random.randrange(25, SCREEN_WIDTH - 25)
                        self.enemy.center_y = random.randrange(SCREEN_HEIGHT + 30, 800)

                        self.enemy_list.append(self.enemy)
                        self.odds -= 15

                # Remove the laser if it goes off screen
                if self.player_laser.bottom > SCREEN_HEIGHT:
                    self.player_laser.remove_from_sprite_lists()
            
            for self.enemy_laser in self.enemy_laser_list:
                # Checks for collisions with the enemy lasers and the player
                laser_player_hitlist = arcade.check_for_collision_with_list(self.enemy_laser, self.player_list)

                if len(laser_player_hitlist) > 0:
                    # Removes the enemy laser if the player is hit, and does random damage between 12 and 24
                    self.enemy_laser.remove_from_sprite_lists()
                    self.player_health -= random.randrange(12,24)
                
                if self.enemy_laser.top < 0:
                    self.enemy_laser.remove_from_sprite_lists()
            
            for self.enemy in self.enemy_list:
                player_enemy_hitlist = arcade.check_for_collision_with_list(self.enemy, self.player_list)

                if len(player_enemy_hitlist) > 0:
                    self.reason = "You crashed into an enemy"
                    self.player_health -= 100

                    # Technically you've destroyed the enemy, so you get a point
                    self.score += 1

            # If the player health is less than zero, the game is over
            if self.player_health <= 0:
                self.game_over = True
                self.game_playing = False
                self.setup()

    def menu(self):
        # All of the text for the menu screen
        arcade.draw_text("This game starts off easy... the enemies will shoot at you, and will also move towards you.", SCREEN_WIDTH/2 -420, SCREEN_HEIGHT - 100, arcade.color.LIGHT_BLUE, 15)
        arcade.draw_text("If you get hit by one of the lasers, you will lose some of your health. If one of the enemy ships ", SCREEN_WIDTH/2 -420, SCREEN_HEIGHT - 125, arcade.color.LIGHT_BLUE, 15)
        arcade.draw_text("gets past you, then you lose. The game will get harder over time. You do have a limited number", SCREEN_WIDTH/2 -420, SCREEN_HEIGHT - 150, arcade.color.LIGHT_BLUE, 15)
        arcade.draw_text("of bullets. You do gain a bullet everytime you hit something, you get a maximum of 2 reloads.", SCREEN_WIDTH/2 -420, SCREEN_HEIGHT - 175, arcade.color.LIGHT_BLUE, 15)
        arcade.draw_text("CONTROLS:", SCREEN_WIDTH/2 - 65, SCREEN_HEIGHT/2 -100, arcade.color.GREEN, 15)
        arcade.draw_text("W/D or Arrow Keys - Move", SCREEN_WIDTH/2 - 125, SCREEN_HEIGHT/2 -125, arcade.color.LIGHT_BLUE, 15)
        arcade.draw_text("Space - Shoot", SCREEN_WIDTH/2 - 75, SCREEN_HEIGHT/2 -150, arcade.color.LIGHT_BLUE, 15)
        arcade.draw_text("R - Reload", SCREEN_WIDTH/2 - 55, SCREEN_HEIGHT/2 -175, arcade.color.LIGHT_BLUE, 15)

def main():
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, "Game")
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()