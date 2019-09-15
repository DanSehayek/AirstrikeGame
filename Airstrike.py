import pygame
import time
import random
import math

pygame.init()

# COLOURS #

white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
green = (34,177,76)
yellow = (200,200,0)
light_green = (0,255,0)
light_yellow = (255,255,0)
light_red = (255,0,0)
blue = (0,0,255)
light_blue = (135, 206, 205)
orange = (255, 165, 0)

# SCREEN DIMENSIONS #

display_width = 800
display_height = 650

# SPRITE DIMENSIONS #

plane_width = 91
plane_height = 85
enemy_width = 85
enemy_height = 72
enemy2_width = 140
enemy2_height = 118
shell_size = 15
PowerUp_size = 53
mine_width = 42
mine_height = 42
enemy3_width = 68
enemy3_height = 72
explosion_e1_width = 49
explosion_e1_height = 41
explosion2_e1_width = 85
explosion2_e1_height = 71
explosion_e2_width = 95
explosion_e2_height = 84
explosion2_e2_width = 140
explosion2_e2_height = 123
mine_explosion_width = 48
mine_explosion_height = 42
mine_explosion2_width = 70
mine_explosion2_height = 62

# GAME SCREEN AND TITLE #

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Airstrike')

# IMAGES #

plane_img = pygame.image.load('Images/Plane_Image2.png')
shell_img = pygame.image.load('Images/Shell_Image2.png')
enemy_img = pygame.image.load('Images/Enemy_Image3.png')
enemy2_img = pygame.image.load('Images/Enemy2_Image2.png')
enemy3_img_left = pygame.image.load('Images/Enemy3Left_Image2.png')
enemy3_img_right = pygame.image.load('Images/Enemy3Right_Image2.png')
missile_img = pygame.image.load('Images/Missile_Image.png')
enemy_missile_img = pygame.image.load('Images/EnemyMissile_Image.png')
mine_img = pygame.image.load('Images/Mine_Image.png')

healthPowerUp_img = pygame.image.load('Images/HealthPowerUp_Image.png')
shieldPowerUp_img = pygame.image.load('Images/ShieldPowerUp_Image.png')
freezePowerUp_img = pygame.image.load('Images/FreezePowerUp_Image.png')
speedPowerUp_img = pygame.image.load('Images/SpeedPowerUp_Image.png')
missilePowerUp_img = pygame.image.load('Images/MissilePowerUp_Image.png')
powerUp_img = pygame.image.load('Images/PowerUp_Image.png')
shield_img = pygame.image.load('Images/Shield_Image.png')
fire_img = pygame.image.load('Images/Fire_Image.png')

menu_img = pygame.image.load('Images/Menu_Image2.png')
menu_b1_img = pygame.image.load('Images/MenuB1_Image2.png')
menu_b2_img = pygame.image.load('Images/MenuB2_Image2.png')
menu_b3_img = pygame.image.load('Images/MenuB3_Image2.png')
game_over_img = pygame.image.load('Images/GameOver_Image2.png')
game_over_b1_img = pygame.image.load('Images/GameOverB1_Image2.png')
game_over_b2_img = pygame.image.load('Images/GameOverB2_Image2.png')
settings_img = pygame.image.load('Images/Settings_Image2.png')
settings_b1_img = pygame.image.load('Images/SettingsB1_Image2.png')
settings_b2_img = pygame.image.load('Images/SettingsB2_Image2.png')

tutorial_1_img = pygame.image.load('Images/Tutorial1_Image.png')
tutorial_2_img = pygame.image.load('Images/Tutorial2_Image.png')
tutorial_3_img = pygame.image.load('Images/Tutorial3_Image.png')
tutorial_4_img = pygame.image.load('Images/Tutorial4_Image.png')
tutorial_5_img = pygame.image.load('Images/Tutorial5_Image.png')
tutorial_6_img = pygame.image.load('Images/Tutorial6_Image.png')
tutorial_7_img = pygame.image.load('Images/Tutorial7_Image.png')
tutorial_8_img = pygame.image.load('Images/Tutorial8_Image.png')

number0_img = pygame.image.load('Images/Number0_Image.png')
number1_img = pygame.image.load('Images/Number1_Image.png')
number2_img = pygame.image.load('Images/Number2_Image.png')
number3_img = pygame.image.load('Images/Number3_Image.png')
number4_img = pygame.image.load('Images/Number4_Image.png')
number5_img = pygame.image.load('Images/Number5_Image.png')
number6_img = pygame.image.load('Images/Number6_Image.png')
number7_img = pygame.image.load('Images/Number7_Image.png')
number8_img = pygame.image.load('Images/Number8_Image.png')
number9_img = pygame.image.load('Images/Number9_Image.png')

explosion_e1_img = pygame.image.load('Images/ExplosionE1_Image.png')
explosion2_e1_img = pygame.image.load('Images/ExplosionE1_Image2.png')
explosion_e2_img = pygame.image.load('Images/ExplosionE2_Image.png')
explosion2_e2_img = pygame.image.load('Images/ExplosionE2_Image2.png')
mine_explosion_img = pygame.image.load('Images/MineExplosion_Image.png')
mine_explosion2_img = pygame.image.load('Images/MineExplosion_Image2.png')

game_icon = pygame.image.load('Images/Game_Icon.png')
game_background = pygame.image.load('Images/GameBackground_Image.png')
checkmark_img = pygame.image.load('Images/Checkmark_Image.png')
score_img = pygame.image.load('Images/Score_Image.png')
home_button_img = pygame.image.load('Images/HomeButton_Image2.png')
transparent_img = pygame.image.load('Images/Transparent_Image.png')

# GAME ICON #
pygame.display.set_icon(game_icon)

# SOUNDS #
button_hover_sound = pygame.mixer.Sound("Audio/Button_Sound.wav")
button_confirm_sound = pygame.mixer.Sound("Audio/Button_Sound2.wav")
powerup_sound = pygame.mixer.Sound("Audio/PowerUp_Sound4.wav")
hit_sound = pygame.mixer.Sound("Audio/Hit_Sound2.wav")
hit_sound2 = pygame.mixer.Sound("Audio/Hit_Sound3.wav")

# CLOCK #
clock = pygame.time.Clock()

# FUNCTIONS #
def score(number, x_pos, y_pos):

    number = str(number)

    for x in range(0, len(number)):
        if number[x] == "0":
            gameDisplay.blit(number0_img, (x_pos + 36 * x, y_pos))
        elif number[x] == "1":
            gameDisplay.blit(number1_img, (x_pos + 36 * x, y_pos))
        elif number[x] == "2":
            gameDisplay.blit(number2_img, (x_pos + 36 * x, y_pos))
        elif number[x] == "3":
            gameDisplay.blit(number3_img, (x_pos + 36 * x, y_pos))
        elif number[x] == "4":
            gameDisplay.blit(number4_img, (x_pos + 36 * x, y_pos))
        elif number[x] == "5":
            gameDisplay.blit(number5_img, (x_pos + 36 * x, y_pos))
        elif number[x] == "6":
            gameDisplay.blit(number6_img, (x_pos + 36 * x, y_pos))
        elif number[x] == "7":
            gameDisplay.blit(number7_img, (x_pos + 36 * x, y_pos))
        elif number[x] == "8":
            gameDisplay.blit(number8_img, (x_pos + 36 * x, y_pos))
        elif number[x] == "9":
            gameDisplay.blit(number9_img, (x_pos + 36 * x, y_pos))

# MENU CLASSES #

class Main_Menu:

    def __init__(self):

        self.run = True
        self.button_1 = "Inactive"      #self.button = "Active" occurs when the user places their mouse on the button and will outline the button in orange
        self.button_2 = "Inactive"
        self.button_3 = "Inactive"
        self.image = menu_img

    def render(self):

        for event in pygame.event.get():        #Allows the user to quit if they click the close button
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(self.image, (0,0))                                                                             #Blits the menu image and a plane image to
        gameDisplay.blit(plane_img, (0.5 * display_width - plane_width/2, 0.5 * display_height - plane_height/4))       #the screen

        self.button(67, 563, 223, 622, "play")          #Verifies that the play/settings/quit button has been clicked and responds accordingly
        self.button(295, 564, 552, 622, "settings")
        self.button(623, 565, 750, 620, "quit")

        if self.button_1 == "Inactive" and self.button_2 == "Inactive" and self.button_3 == "Inactive":
            self.image = menu_img

        pygame.display.update()
        clock.tick(15)

    def button(self, x, y, x2, y2, action):

        cur = pygame.mouse.get_pos()            #Retrieves the cursor position
        click = pygame.mouse.get_pressed()      #Indicates which mouse buttons are currently clicked

        if x < cur[0] < x2 and y < cur[1] < y2:

            if click[0] == 1:       #If the left mouse button is clicked

                pygame.mixer.Sound.play(button_confirm_sound)

                if action == "quit":        #Quits if the user clicks the QUIT button
                    pygame.quit()
                    quit()

                elif action == "settings":      #Goes to the settings menu if the user clicks the SETTINGS button
                    settings.run = True
                    self.run = False

                elif action == "play":      #Goes to the game if the user clicks the PLAY button and resets attributes if the user has already played at least once
                    player.health = 100
                    player.x = display_width / 2 - plane_width / 2
                    player.y = display_height * 0.8
                    player.speedx = 0
                    player.speedy = 0
                    player.directionx = "None"
                    player.directiony = "None"
                    player.score = 0
                    player.time_counter = 0
                    enemyH.present = False
                    enemyH.image = enemy_img
                    enemyH.direction = "up"
                    enemyH.fire_counter = 5
                    enemyH.hit = False
                    enemyH.crash = 5
                    enemyH.explosion = False
                    enemyH.e_counter = 0
                    enemyV.present = False
                    enemyV.fire_counter = 5
                    enemyV.hit = False
                    enemyV.crash = 5
                    enemyV.explosion = False
                    enemyV.e_counter = 0
                    enemy2.present = False
                    enemy3.present = False
                    enemy3.hit = False
                    enemy3.explosion = False
                    enemy3.e_counter = 0
                    enemyBulletH.fire = False
                    enemyBulletV.fire = False
                    enemyBullet2.fire = False
                    enemyBullet2.firing = False
                    enemyBullet3.fire = False
                    powerUp.present = False
                    powerUp.type = None
                    mine.present = False
                    ring_of_fire.counter = 3
                    self.run = False
                    enemyH.x = 0
                    enemyH.y = 0
                    enemyV.x = 0
                    enemyV.y = 0
                    enemy2.x = 0
                    enemy2.y = 0
                    enemy3.x = 0
                    enemy3.y = 0
                    bullet.fire = False
                    gameLoop()

            else:       #If the user has placed the cursor on one of the buttons but has not clicked it then that button will light up in orange

                if action == "quit":
                    self.image = menu_b3_img
                    self.button_1 = "Active"
                elif action == "settings":
                    self.image = menu_b2_img
                    self.button_2 = "Active"
                elif action == "play":
                    self.image = menu_b1_img
                    self.button_3 = "Active"

        else:       #If the user has not placed the cursor on any of the buttons then all buttons will be set back to default style

            if action == "quit":
                self.button_1 = "Inactive"
            elif action == "settings":
                self.button_2 = "Inactive"
            elif action == "play":
                self.button_3 = "Inactive"

class Game_Over:

    def __init__(self):

        self.run = True
        self.menu = False
        self.button_1 = "Inactive"      #Buttons have same interactivity as buttons in main menu class
        self.button_2 = "Inactive"
        self.image = game_over_img

    def render(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(self.image, (0,0))                             #Blits the game over menu to the screen
        gameDisplay.blit(score_img, (53, 0.5 * display_height + 5))     #Blits the score box to the screen
        score(player.score, 233, 0.5 * display_height + 15)             #Blits the score to the screen
        gameDisplay.blit(home_button_img, (630, 50))                    #Blits the home button to the screen

        self.button(58, 554, 207, 615, "play")
        self.button(601, 557, 722, 615, "quit")
        self.button(630, 50, 713, 133, "menu")

        if self.button_1 == "Inactive" and self.button_2 == "Inactive":
            self.image = game_over_img

        pygame.display.update()
        clock.tick(15)

    def button(self, x, y, x2, y2, action):

        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < cur[0] < x2 and y < cur[1] < y2:

            if click[0] == 1:

                pygame.mixer.Sound.play(button_confirm_sound)

                if action == "quit":        #Allows the user to quit if they click the QUIT button
                    pygame.quit()
                    quit()

                elif action == "play":      #Allows the user to play again if they click the PLAY AGAIN button and resets attributes accordingly
                    player.health = 100
                    player.x = display_width / 2 - plane_width / 2
                    player.y = display_height * 0.8
                    player.speedx = 0
                    player.speedy = 0
                    player.directionx = "None"
                    player.directiony = "None"
                    player.score = 0
                    player.time_counter = 0
                    enemyH.present = False
                    enemyH.image = enemy_img
                    enemyH.direction = "up"
                    enemyH.fire_counter = 5
                    enemyH.hit = False
                    enemyH.crash = 5
                    enemyH.explosion = False
                    enemyH.e_counter = 0
                    enemyV.present = False
                    enemyV.fire_counter = 5
                    enemyV.hit = False
                    enemyV.crash = 5
                    enemyV.explosion = False
                    enemyV.e_counter = 0
                    enemy2.present = False
                    enemy3.present = False
                    enemy3.hit = False
                    enemy3.explosion = False
                    enemy3.e_counter = 0
                    enemyBulletH.fire = False
                    enemyBulletV.fire = False
                    enemyBullet2.fire = False
                    enemyBullet2.firing = False
                    enemyBullet3.fire = False
                    powerUp.present = False
                    powerUp.type = None
                    mine.present = False
                    ring_of_fire.counter = 3
                    self.run = False
                    enemyH.x = 0
                    enemyH.y = 0
                    enemyV.x = 0
                    enemyV.y = 0
                    enemy2.x = 0
                    enemy2.y = 0
                    enemy3.x = 0
                    enemy3.y = 0
                    bullet.fire = False
                    gameLoop()

                elif action == "menu":      #Allows the user to go to the main menu if they click the home button
                    self.run = False
                    self.menu = True
                    main_menu.run = True

            else:

                if action == "quit":
                    self.image = game_over_b2_img
                    self.button_2 = "Active"
                elif action == "play":
                    self.image = game_over_b1_img
                    self.button_1 = "Active"

        else:

            if action == "quit":
                self.button_2 = "Inactive"
            elif action == "play":
                self.button_1 = "Inactive"

class Settings:

    def __init__(self):

        self.run = True
        self.button_1 = "Inactive"      #Buttons have same interactivity as buttons in main menu class
        self.button_2 = "Inactive"
        self.image = settings_img
        self.music = True

    def render(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(self.image, (0,0))

        self.button(91, 555, 240, 615, "play")
        self.button(583, 558, 704, 618, "quit")
        self.button(422, 273, 485, 333, "tutorial")
        self.button(421, 373, 484, 433, "music")

        if tutorial.run == True:
            gameDisplay.blit(checkmark_img, (425, 280))         #Blits a checkmark to the tutorial box if the tutorial is on

        if self.music == True:
            gameDisplay.blit(checkmark_img, (424, 380))         #Blits a checkmark to the music box if the music is on

        if self.button_1 == "Inactive" and self.button_2 == "Inactive":
            self.image = settings_img

        pygame.display.update()
        clock.tick(15)

    def button(self, x, y, x2, y2, action):

        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < cur[0] < x2 and y < cur[1] < y2:

            if click[0] == 1:

                pygame.mixer.Sound.play(button_confirm_sound)

                if action == "quit":        #Allows the user to quit if they click the QUIT button
                    pygame.quit()
                    quit()
                elif action == "play":      #Allows the user to play if they click the PLAY button
                    self.run = False
                    main_menu.run = True
                elif action == "tutorial":      #Toggles the tutorial between on and off if the user clicks the tutorial box
                    if tutorial.run == False:
                        tutorial.run = True
                    elif tutorial.run == True:
                        tutorial.run = False
                elif action == "music":         #Toggles the music between on and off if the user clicks the music box
                    if self.music == True:
                        self.music = False
                        pygame.mixer.music.pause()
                    elif self.music == False:
                        self.music = True
                        pygame.mixer.music.unpause()

            else:

                if action == "quit":
                    self.image = settings_b2_img
                    self.button_2 = "Active"
                elif action == "play":
                    self.image = settings_b1_img
                    self.button_1 = "Active"

        else:

            if action == "quit":
                self.button_2 = "Inactive"
            elif action == "play":
                self.button_1 = "Inactive"

# GAME CLASSES #

class Plane:

    def __init__(self):

        self.x = display_width / 2 - plane_width/2
        self.y = display_height * 0.8
        self.width = plane_width
        self.height = plane_height
        self.speedx = 0
        self.speedy = 0
        self.health = 100
        self.health_color = "Green"
        self.hit = False
        self.hit2 = False
        self.crash = False
        self.directionx = "None"
        self.directiony = "None"
        self.stopx = False
        self.stopy = False
        self.score = 0
        self.shield = False
        self.shield_health = 0
        self.time_counter = 0

    def render(self):

        self.position_check()               #Calls the defined methods
        self.direction_check()
        self.stop_check()
        self.health_bar()
        self.score_display()

        self.time_counter += 1

        if powerUp.speed_boost == True and self.speedx != 0:            #Increases the speed if the speed powerup is obtained
            if self.directionx == "left":
                self.speedx = -10
            elif self.directionx == "right":
                self.speedx = 10

        if powerUp.speed_boost == True and self.speedy != 0:
            if self.directiony == "up":
                self.speedy = -10
            elif self.directiony == "down":
                self.speedy = 10

        self.x += self.speedx               #Adjusts the position based on the current speed
        self.y += self.speedy

        gameDisplay.blit(plane_img, (self.x, self.y))                       #Blits the plane image to the screen

        if self.shield_health <= 0:                                         #Removes shield if shield health is less than 0
            self.shield = False

        if self.shield == True:                                             #Displays the shield if the shield powerup is obtained
            gameDisplay.blit(shield_img, (self.x - 14, self.y - 14))

    def direction_check(self):                      #Sets the speed of the plane according to the direction
                                                    #The direction is chosen according to arrow key event handling
        if self.directionx == "left":
            self.speedx = -5

        if self.directionx == "right":
            self.speedx = 5

        if self.directiony == "up":
            self.speedy = -5

        if self.directiony == "down":
            self.speedy = 5

    def stop_check(self):       #Ensures that the plane does not travel diagonally

        if self.stopx == True:
            self.speedx = 0

        if self.stopy == True:
            self.speedy = 0

    def position_check(self):           #Ensures that the player does not exit the screen by comparing player position with
                                        #boundary position
        if self.x < 0:
            self.x = 0

        elif self.x + self.width > display_width:
            self.x = display_width - self.width

        if self.y < 0.1 * display_height:
            self.y = 0.1 * display_height

        elif self.y + self.height > display_height:
            self.y = display_height - self.height

    def health_bar(self):                   #Modifies the player's health according to hits and health powerups

        if self.hit == True and self.shield == False:

            self.health -= 10
            self.hit = False

        if self.hit == True and self.shield == True:

            self.shield_health -= 10
            self.hit = False

        if self.crash == True and self.shield == False:

            self.health -= 20
            self.crash = False

        if self.crash == True and self.shield == True:

            self.shield_health -=20
            self.crash = False

        if self.health > 75:
            self.health_colour = green
        elif self.health > 25:
            self.health_colour = yellow
        else:
            self.health_colour = red

        if self.health > 100:
            self.health = 100

        if self.health < 0:
            self.health = 0

        pygame.draw.rect(gameDisplay, black, (int(0.02 * display_width - 0.01), int(0.02 * display_height - 0.01), 100 + 1, 15 + 1))
        pygame.draw.rect(gameDisplay, self.health_colour, (int(0.02 * display_width), int(0.02 * display_height), self.health, 15))

    def score_display(self):            #Displays the score using the previously defined score function

        score(self.score, 0.85 * display_width, 0.025 * display_height)

class Bullet:

    def __init__(self):

        self.x = 0
        self.y = 0
        self.width = shell_size
        self.height = shell_size
        self.speed = 0
        self.fire = False
        self.hit = False
        self.image = shell_img
        self.missile = 0

    def render(self):

        if self.fire == True:

           if powerUp.speed_boost == True:          #Increases the speed if the speed powerup is obtained
               self.speed = 15
           else:
               self.speed = 10

           self.y -= self.speed         #Adjusts the position based on the current speed
           self.position_check()
           self.enemy_check()

           if self.missile > 0:
               self.image = missile_img                 #Selects the image for the bullet depending on whether or not
           else:                                        #it is a shell or a missile
               self.image = shell_img

           gameDisplay.blit(self.image, (self.x, self.y))

    def position_check(self):           #Enables the player to shoot again if the current bullet exits the screen

        if self.y < 0:

            self.fire = False
            if self.missile > 0:
                self.missile -= 1

    def enemy_check(self):              #Checks to see if the current bullet has collided with any of the current enemies

        if enemyH.x < self.x < enemyH.x + enemyH.width and enemyH.y < self.y < enemyH.y + enemyH.height and enemyH.present == True and enemyH.e_counter == 0:
            enemyH.hit = True
            self.fire = False           #Enables the player to shoot again if the collision is true
            player.score += 10          #Modifies the score accordingly

        if enemyV.x < self.x < enemyV.x + enemyV.width and enemyV.y < self.y < enemyV.y + enemyV.height and enemyV.present == True:
            if enemyV.explosion == False:
                enemyV.hit = True
                self.fire = False
                player.score += 10

        #The damage dealt to the Enemy 2 plane depends on whether or not the bullet is a missile

        if enemy2.x + enemy2.width/2 - 5 <= self.x <= enemy2.x + enemy2.width/2 + 5 and self.y < enemy2.y + enemy2.height and enemy2.present == True:
            if self.image == missile_img:
                enemy2.health -= 30
                self.missile -= 1
            else:
                enemy2.health -= 10
                self.missile -= 1
            self.fire = False

        #We add a second if statement for Enemy 2 to ensure wing collision detection

        elif enemy2.x <= self.x <= enemy2.x + enemy2.width/2 - 5 or enemy2.x + enemy2.width/2 + 5 <= self.x <= enemy2.x + enemy2.width:
            if self.y < enemy2.y + enemy2.height - 35 and enemy2.present == True:
                if self.image == missile_img:
                    enemy2.health -= 30
                    self.missile -= 1
                else:
                    enemy2.health -= 10
                    self.missile -= 1
                self.fire = False

class PowerUp:

    def __init__(self):

        self.x = 0
        self.y = 0
        self.width = PowerUp_size
        self.height = PowerUp_size
        self.present = False
        self.type = "None"
        self.freeze = False
        self.freeze_counter = 0
        self.speed_boost = False
        self.speed_boost_counter = 0

    def update(self):

        self.position_selector()                #Calls the defined methods
        self.position_check()

        if self.present == True:                #Displays the powerup if it is present with the appropriate image

            gameDisplay.blit(powerUp_img, (self.x, self.y))

            if self.type == "HealthBoost":

                gameDisplay.blit(healthPowerUp_img, (self.x, self.y))

            elif self.type == "Shield":

                gameDisplay.blit(shieldPowerUp_img, (self.x, self.y))

            elif self.type == "Missile":

                gameDisplay.blit(missilePowerUp_img, (self.x, self.y))

            elif self.type == "Freeze":

                gameDisplay.blit(freezePowerUp_img, (self.x, self.y))

            elif self.type == "SpeedBoost":

                gameDisplay.blit(speedPowerUp_img, (self.x, self.y))

        if self.freeze == True:                 #Counts the timer down for the Freeze powerup if it is activated
            self.freeze_counter += 1
            if self.freeze_counter == 240:
                self.freeze = False
                self.freeze_counter = 0

        if self.speed_boost == True:            #Counts the timer down for the Speed powerup if it is activated
            self.speed_boost_counter += 1
            if self.speed_boost_counter == 500:
                self.speed_boost = False
                self.speed_boost_counter = 0

    def position_selector(self):

        if self.present == False:

            special_number = random.randrange(0,1500)           #Selects a random number from 0 to 1500
                                                                #Selects the appropriate powerup corresponding to the special number
            if special_number == 5:                             #Selects a random position for the powerup
                self.present = True
                self.x = random.randrange(0.2 * display_width, 0.8 * display_width)
                self.y = random.randrange(0.2 * display_height, 0.8 * display_height)
                self.type = "HealthBoost"

            elif special_number == 10:
                self.present = True
                self.x = random.randrange(0.2 * display_width, 0.8 * display_width)
                self.y = random.randrange(0.2 * display_height, 0.8 * display_height)
                self.type = "Shield"

            elif special_number == 15:
                self.present = True
                self.x = random.randrange(0.2 * display_width, 0.8 * display_width)
                self.y = random.randrange(0.2 * display_height, 0.8 * display_height)
                self.type = "Missile"

            elif special_number == 20:
                self.present = True
                self.x = random.randrange(0.2 * display_width, 0.8 * display_width)
                self.y = random.randrange(0.2 * display_height, 0.8 * display_height)
                self.type = "Freeze"

            elif special_number == 25:
                self.present = True
                self.x = random.randrange(0.2 * display_width, 0.8 * display_width)
                self.y = random.randrange(0.2 * display_height, 0.8 * display_height)
                self.type = "SpeedBoost"

    def position_check(self):                   #Checks to see if the player's position coincides with the powerup's position

        if self.present == True:                #Assigns the appropriate powerup by calling the boost_check method

            if player.x < self.x < player.x + player.width and player.y < self.y < player.y + player.height:
                self.boost_check()

            elif player.x < self.x + self.width < player.x + player.width and player.y < self.y < player.y + player.height:
                self.boost_check()

            elif player.x < self.x < player.x + player.width and player.y < self.y + self.height < player.y + player.height:
                self.boost_check()

            elif player.x < self.x + self.width < player.x + player.width and player.y < self.y + self.height < player.y + player.height:
                self.boost_check()

    def boost_check(self):

        pygame.mixer.Sound.play(powerup_sound)

        if self.type == "HealthBoost":
            player.health += 20
        if self.type == "Shield":
            player.shield = True
            player.shield_health = 50
        if self.type == "Missile":
            bullet.missile = 5
        if self.type == "Freeze":
            self.freeze = True
        if self.type == "SpeedBoost":
            self.speed_boost = True
        self.present = False

class ROF:

    def __init__(self):

        self.x = int(player.x + player.width/2)
        self.y = int(player.y + player.height/2)
        self.radius = 5
        self.present = False
        self.distance_e1 = 0
        self.distance_e2 = 0
        self.distance_e3 = 0
        self.distance_e4 = 0
        self.symbol = fire_img
        self.counter = 3
        self.enemyH = False
        self.enemyV = False
        self.enemy2 = False
        self.enemy3 = False

    def render(self):

        if self.counter == 3:           #Displays the appropriate number of available rings of fire based on the number of rings that the player has used

            gameDisplay.blit(self.symbol, (int(0.022 * display_width), int(0.07 * display_height)))
            gameDisplay.blit(self.symbol, (int(0.022 * display_width + 20), int(0.07 * display_height)))
            gameDisplay.blit(self.symbol, (int(0.022 * display_width + 40), int(0.07 * display_height)))

        elif self.counter == 2:

            gameDisplay.blit(self.symbol, (int(0.022 * display_width), int(0.07 * display_height)))
            gameDisplay.blit(self.symbol, (int(0.022 * display_width + 20), int(0.07 * display_height)))

        elif self.counter == 1:

            gameDisplay.blit(self.symbol, (int(0.022 * display_width), int(0.07 * display_height)))

        if self.present == True:        #Calculates the distances from each of the enemy plnnes to the player plane

            self.distance_e1 = math.sqrt((enemyH.x - self.x)**2 + (enemyH.y - self.y)**2)
            self.distance_e2 = math.sqrt((enemyV.x - self.x)**2 + (enemyV.y - self.y)**2)
            self.distance_e3 = math.sqrt((enemy2.x - self.x)**2 + (enemy2.y - self.y)**2)
            self.distance_e4 = math.sqrt((enemy3.x - self.x)**2 + (enemy3.y - self.y)**2)

            self.x = int(player.x + player.width/2)
            self.y = int(player.y + player.height/2)

            pygame.draw.circle(gameDisplay, red, (self.x, self.y), self.radius, 3)      #Blits the ring of fire according to the current radius

            if 0.9 * self.distance_e1 < self.radius < 1.1 * self.distance_e1:           #Destroys any enemies within the current vicinity of the ring
                if enemyH.present == True and self.enemyH == False:
                    enemyH.hit = True
                    self.enemyH = True

            if 0.9 * self.distance_e2 < self.radius < 1.1 * self.distance_e2:
                if enemyV.present == True and self.enemyV == False:
                    enemyV.hit = True
                    self.enemyV = True

            if 0.9 * self.distance_e3 < self.radius < 1.1 * self.distance_e2:
                if enemy2.present == True and self.enemy2 == False:
                    enemy2.health = 0
                    self.enemy2 = True

            if 0.8 * self.distance_e4 < self.radius < 1.2 * self.distance_e3:
                if enemy3.present == True and self.enemy3 == False:
                    enemy3.hit = True
                    self.enemy3 = True

            self.radius += 8                            #Checks to see if the ring is past the edges of the screen and adjusts the attributes accordingly

            if self.x + self.radius  > display_width + 60 and self.x - self.radius < 60 and self.y + self.radius + 60 > display_height and self.y - self.radius - 60 < 0:
                self.present = False
                self.radius = 5
                self.enemyH = False
                self.enemyV = False
                self.enemy2 = False
                self.enemy3 = False

class EnemyH:

    def __init__(self):

        self.x = 0
        self.y = 0
        self.width = enemy_width
        self.height = enemy_height
        self.speed = 0
        self.present = False
        self.image = enemy_img
        self.direction = "up"
        self.hit = False
        self.crash = False
        self.fire_counter = 5
        self.explosion = False
        self.e_counter = 0

    def render(self):

        if self.hit == True or self.crash == True:      #Triggers an explosion if the plane is hit

            pygame.mixer.Sound.play(hit_sound)

            self.image = explosion_e1_img
            self.explosion = True
            self.hit = False
            self.crash = False
            self.x += 10
            self.y += 10

        if self.explosion == True:

            self.e_counter += 1

            if self.e_counter == 15:            #Sets a timer to determine when to enlarge the explosion and when to stop it

                self.image = explosion2_e1_img
                self.x = self.x + explosion_e1_width / 2 - explosion2_e1_width / 2
                self.y = self.y + explosion_e1_height / 2 - explosion2_e1_height / 2

            elif self.e_counter == 30:

                self.present = False
                self.explosion = False
                self.e_counter = 0

        self.position_check()               #Calls the defined methods
        self.position_selector()

        if powerUp.freeze == True or ring_of_fire.present == True or self.explosion == True:        #Stops the enemy plane if the freeze powerup or ring or fire
            self.speed = 0                                                                          #has been activated or the enemy plane is hit

        elif powerUp.freeze == False and self.speed == 0:           #Sets the speed back to a non zero value if the freeze
            if self.direction == "right":                           #powerup is no longer active
                self.speed = 4
            elif self.direction == "left":
                self.speed = -4

        self.x += self.speed                                #Adjusts the position of the enemy plane according to the speed

        gameDisplay.blit(self.image, (self.x, self.y))      #Blits the enemy plane to the screen

    def position_selector(self):

        if self.present == False and enemyBulletH.fire == True:         #Ensures that the enemy bullet is still moving when the enemy has been hit

            self.image = transparent_img

        elif self.present == False and enemyBulletH.fire == False:      #Initiates a new EnemyH plane if no EnemyH plane is present

            self.image = enemy_img
            self.direction = "up"

            x_position_list = [(0 - self.width), display_width + 10]
            y_position_list = [(0.8 * display_height), (0.5 * display_height), (0.2 * display_height), (0.65 * display_height), (0.35 * display_height)]
            y_position_list_2 = [(0.8 * display_height), (0.5 * display_height), (0.65 * display_height), (0.35 * display_height)]

            self.x = x_position_list[random.randrange(0,2)]                     #Selects a random horizontal position for the enemy plane

            if enemy2.present == True and enemy3.present == True:               #Selects a random vertical position for the enemy plane based on the current
                self.y = y_position_list[random.randrange(0,2)]                 #enemies on the screen so as to avoid enemy collisions

            elif enemy2.present == True:
                self.y = y_position_list_2[random.randrange(0,4)]

            elif enemy3.present == True:
                self.y = y_position_list[random.randrange(0,3)]

            else:
                self.y = y_position_list[random.randrange(0,5)]

            if self.x == x_position_list[0]:
                self.speed = 4

                if self.direction == "up":
                    self.image = pygame.transform.rotate(self.image, 270)

                if self.direction == "down":
                    self.image = pygame.transform.rotate(self.image, 90)

                if self.direction == "left":
                    self.image = pygame.transform.rotate(self.image, 180)

                self.direction = "right"

            elif self.x == x_position_list[1]:
                self.speed = -4

                if self.direction == "up":
                    self.image = pygame.transform.rotate(self.image, 90)

                if self.direction == "down":
                    self.image = pygame.transform.rotate(self.image, 270)

                if self.direction == "right":
                    self.image = pygame.transform.rotate(self.image, 180)

                self.direction = "left"

            self.present = True
            self.fire_counter = 0

    def position_check(self):       #Checks to see if the enemy plane has left the screen or has collided with the player plane and responds accordingly

        if self.image != transparent_img and self.image != explosion_e1_img and self.image != explosion2_e1_img:

            if self.x + self.width + 15 < 0 or self.x - 15 > display_width:
                self.present = False

            elif player.x < self.x < player.x + player.width and player.y < self.y < player.y + player.height:
                player.crash = True
                self.crash = True

            elif player.x < self.x + self.width < player.x + player.width and player.y < self.y < player.y + player.height:
                player.crash = True
                self.crash = True

            elif player.x < self.x < player.x + player.width and player.y < self.y + self.height < player.y + player.height:
                player.crash = True
                self.crash = True

            elif player.x < self.x + self.width < player.x + player.width and player.y < self.y + self.height < player.y + player.height:
                player.crash = True
                self.crash = True

class EnemyV:

    def __init__(self):

        self.x = 0
        self.y = 0
        self.width = enemy_width
        self.height = enemy_height
        self.speed = 0
        self.present = False
        self.image = pygame.transform.rotate(enemy_img, 180)
        self.hit = False
        self.crash = False
        self.fire_counter = 5
        self.wait = False
        self.explosion = False
        self.e_counter = 0

    def render(self):

        if self.hit == True or self.crash == True:          #Triggers an explosion if the plane is hit

            pygame.mixer.Sound.play(hit_sound)

            self.image = explosion_e1_img
            self.explosion = True
            self.hit = False
            self.crash = False
            self.x += 10
            self.y += 10

        if self.explosion == True:          #Sets a timer to determine when to enlarge the explosion and when to stop it

            self.e_counter += 1

            if self.e_counter == 15:

                self.image = explosion2_e1_img
                self.x = self.x + explosion_e1_width / 2 - explosion2_e1_width / 2
                self.y = self.y + explosion_e1_height / 2 - explosion2_e1_height / 2

            elif self.e_counter == 30:

                self.present = False
                self.explosion = False
                self.e_counter = 0
                self.y = -100

        self.position_check()               #Calls the defined methods
        self.position_selector()

        if powerUp.freeze == True or ring_of_fire.present == True or self.explosion == True:    #Stops the enemy plane if the freeze powerup or ring of fire has been activated
            self.speed = 0

        elif powerUp.freeze == False and self.speed == 0 and self.explosion == False and self.present == True:      #Sets the speed back to a non zero value if the freeze powerup is no longer active
            self.speed = 4

        self.y += self.speed                                    #Adjusts the position of the enemy plane according to the speed

        gameDisplay.blit(self.image, (self.x, self.y))          #Blits the enemy plane to the screen

    def position_selector(self):

        if self.present == False and enemyBulletV.fire == True:         #Ensures that the enemy bullet is still moving when the enemy has been hit

            self.image = transparent_img

        elif self.present == False and enemyBulletV.fire == False and enemy2.present == False:      #Initiates a new EnemyV plane if no EnemyV plane is present

            self.image = pygame.transform.rotate(enemy_img, 180)
            self.y = -100

            if self.wait == True:           #Ensures that a new EnemyV plane does not randomly appear at the top of the screen
                self.y = -100               #during freeze powerup or ring of fire activation
                self.wait = False

            x_position_list = [0.2 * display_width, 0.5 * display_width, 0.8 * display_width]

            self.x = x_position_list[random.randrange(0,3)]         #Selects a random horizontal position for the enemy plane

            self.speed = 4

            self.present = True
            self.fire_counter = 0

    def position_check(self):           #Checks to see if the enemy plane has left the screen or has collided with the player plane and responds accordingly

        if self.image != transparent_img and self.image != explosion_e1_img and self.image != explosion2_e1_img:

            if self.y > display_height:
                self.present = False

            elif player.x < self.x < player.x + player.width and player.y < self.y < player.y + player.height:
                player.crash = True
                self.crash = True

            elif player.x < self.x + self.width < player.x + player.width and player.y < self.y < player.y + player.height:
                player.crash = True
                self.crash = True

            elif player.x < self.x < player.x + player.width and player.y < self.y + self.height < player.y + player.height:
                player.crash = True
                self.crash = True

            elif player.x < self.x + self.width < player.x + player.width and player.y < self.y + self.height < player.y + player.height:
                player.crash = True
                self.crash = True

class Enemy2:

    def __init__(self):

        self.x = 0
        self.y = 0
        self.width = enemy2_width
        self.height = enemy2_height
        self.speedx = 0
        self.speedy = 0
        self.present = False
        self.image = pygame.transform.rotate(enemy2_img, 180)
        self.hit = False
        self.movex = False
        self.target_position = 0
        self.target_distance = 0
        self.health = 100
        self.health_colour = green
        self.time_counter = 0
        self.explosion = False
        self.e_counter = 0

    def render(self):

        if self.health <= 0 and self.explosion == False:        #Triggers an explosion if the enemy plane's health is less than or equal to zero

            pygame.mixer.Sound.play(hit_sound2)

            self.image = explosion_e2_img
            self.explosion = True
            self.x += 10
            self.y += 10
            self.speedx = 0
            self.speedy = 0

        if self.explosion == True:          #Sets a timer to determine when to enlarge the explosion and when to stop it

            self.e_counter += 1

            if self.e_counter == 15:

                self.image = explosion2_e2_img
                self.x = self.x + explosion_e2_width / 2 - explosion2_e2_width / 2
                self.y = self.y + explosion_e2_height / 2 - explosion2_e2_height / 2

            elif self.e_counter == 30:

                self.present = False
                self.explosion = False
                self.e_counter = 0
                self.health = 100
                player.score += 80
                enemyV.wait = True

        self.position_selector()            #Calls the defined methods
        self.position_check()

        if self.explosion == False:

            self.health_bar()               #Draws the health bar for the enemy plane

        if self.present == True:

            if self.movex == True:

                self.target_position = round(player.x / 2.0) * 2.0 - 60         #Sets the horizontal position to which the enemy plane will move equal to the
                                                                                #horizontal position of the player plane
                if self.target_position <= self.width:                          #Ensures that a portion of the enemy plane does not pass the left edge of the screen
                    self.target_position = self.width

                if self.x < self.target_position:           #Sets the speed of the enemy plane accordingly
                    self.speedx = 2
                if self.x > self.target_position:
                    self.speedx = -2

                self.movex = False

            if self.x == self.target_position and self.y == 0.15 * display_height:          #Triggers the enemy plane to stop and fire once it has reached its
                self.speedx = 0                                                             #target position
                enemyBullet2.fire = True

            if powerUp.freeze == True or ring_of_fire.present == True:              #Stops the enemy plane if the freeze powerup or ring of fire
                self.speedx = 0                                                     #has been activated
                self.speedy = 0

            elif powerUp.freeze == False and self.speedx == 0 and self.speedy == 0 and self.explosion == False:     #Sets the speed back to an appropriate value
                if self.y < 0.15 * display_height:                                                                  #once the freeze powerup is no longer active
                    self.speedy = 3
                else:
                    self.target_position = round(player.x / 2.0) * 2.0 - 60

                    if self.x < self.target_position:
                        self.speedx = 2
                    if self.x > self.target_position:
                        self.speedx = -2

            if self.image == explosion_e2_img or self.image == explosion2_e2_img:

                self.speedx = 0
                self.speedy = 0

            self.x += self.speedx                                   #Adjusts the position of the enemy plane according to the speed
            self.y += self.speedy
            gameDisplay.blit(self.image, (self.x, self.y))          #Blits the enemy plane to the screen

    def position_selector(self):

        if self.present == False:

            special_number = random.randrange(300)                  #Selects a random number from 0 to 300

            if special_number == 5:                                 #Initiates a new Enemy3 plane if that number is 5

                x_position_list = [120, 340, 560]

                special_number2 = random.randrange(0,3)

                self.x = x_position_list[special_number2]           #Selects a random horizontal position
                self.y = -0.2 * display_height

                self.speedx = 0
                self.speedy = 3

                self.present = True
                self.health = 100                                   #Resets the health to 100
                self.time_counter = 0

                self.image = pygame.transform.rotate(enemy2_img, 180)

    def position_check(self):                                   #Checks to see if the enemy plane has collided with the player plane and
                                                                #deducts health accordingly
        if self.y > 0.15 * display_height:
            self.y = 0.15 * display_height
            self.speedy = 0
            self.movex = True

        if self.present == True:

            if self.x < player.x < self.x + self.width and self.y < player.y < self.y + self.height:

                if self.time_counter == 5 or self.time_counter == 95 or self.time_counter == 195 or self.time_counter == 295 or self.time_counter == 395:
                    player.health -= 20
                    self.health -= 20

                self.time_counter += 1

            elif self.x < player.x + player.width < self.x + self.width and self.y < player.y < self.y + self.height:

                if self.time_counter == 5 or self.time_counter == 95 or self.time_counter == 195 or self.time_counter == 295 or self.time_counter == 395:
                    player.health -= 20
                    self.health -= 20

                self.time_counter += 1

            elif self.x < player.x < self.x + self.width and self.y < player.y + player.height < self.y + self.height:

                if self.time_counter == 5 or self.time_counter == 95 or self.time_counter == 195 or self.time_counter == 295 or self.time_counter == 395:
                    player.health -= 20
                    self.health -= 20

                self.time_counter += 1

            elif self.x < player.x + player.width < self.x + self.width and self.y < player.y + player.height < self.y + self.height:

                if self.time_counter == 5 or self.time_counter == 95 or self.time_counter == 195 or self.time_counter == 295 or self.time_counter == 395:
                    player.health -= 20
                    self.health -= 20

                self.time_counter += 1

    def health_bar(self):

        if self.present == True:                            #Sets the colour of the health bar according to the enemy plane's health and
                                                            #blits the health bar to the screen
            if self.health > 75:
                self.health_colour = green
            elif self.health > 25:
                self.health_colour = yellow
            else:
                self.health_colour = red

            pygame.draw.rect(gameDisplay, self.health_colour, (self.x, self.y - 10, self.health, 7))

class Enemy3:

    def __init__(self):

        self.x = 0
        self.y = 0
        self.width = enemy3_width
        self.height = enemy3_height
        self.speed = 0
        self.image = enemy3_img_right
        self.present = False
        self.movex = False
        self.special_number = 0
        self.hit = False
        self.explosion = False
        self.e_counter = 0

    def render(self):

        if self.hit == True:                            #Triggers an explosion if the enemy is hit

            pygame.mixer.Sound.play(hit_sound2)

            self.image = explosion_e1_img
            self.explosion = True
            self.hit = False
            self.x += 10
            self.y += 10

        if self.explosion == True:                      #Sets a timer to determine when to enlarge the explosion and when to stop it

            self.e_counter += 1

            if self.e_counter == 15:

                self.image = explosion2_e1_img
                self.x = self.x + explosion_e1_width / 2 - explosion2_e1_width / 2
                self.y = self.y + explosion_e1_height / 2 - explosion2_e1_height / 2

            elif self.e_counter == 30:

                self.present = False
                self.explosion = False
                self.e_counter = 0

        self.position_selector()                #Calls the defined methods
        self.position_check()

        if self.present == True:

            if self.movex == True:              #Moves the enemy away from the screen once it has finished shooting its missiles

                if self.speed == 0:

                    if self.x < display_width/2:
                        self.speed = -1

                    elif self.x > display_width/2:
                        self.speed = 1

                if self.x <= -70 or self.x >= display_width + 10:
                    self.present = False
                    self.movex = False

            self.x += self.speed                                    #Adjusts the position of the enemy according to the speed

            gameDisplay.blit(self.image, (self.x, self.y))          #Blits the enemy to the screen

    def position_selector(self):

        if self.present == False and enemyBullet3.fire == False:

            self.special_number = random.randrange(0,300)           #Selects a random number from 0 to 300

            if self.special_number == 5:                            #Initiates a new Enemy3 plane if that number is 5

                x_number = random.randrange(0,2)
                y_number = random.randrange(0,2)

                x_position_list = [-100, display_width + 100]
                y_position_list = [0.65 * display_height, 0.87 * display_height]

                self.x = x_position_list[x_number]                  #Selects a random horizontal position
                self.y = y_position_list[y_number]                  #Selects a random vertical position

                if x_number == 0:                       #Adjusts the speed and orientation accordingly
                    self.speed = 2
                    self.image = enemy3_img_right
                elif x_number == 1:
                    self.speed = -2
                    self.image = enemy3_img_left

                self.present = True

    def position_check(self):           #Stops the enemy if it has reached the left or right edge of the screen

        if self.present == True and self.movex == False:

            if self.speed == 2 and self.x == 0:
                self.speed = 0

            elif self.speed == -2 and self.x == display_width - self.width:
                self.speed = 0

class EnemyBulletH:

    def __init__(self):

        self.x = 0
        self.y = 0
        self.width = shell_size
        self.height = shell_size
        self.speed = 0
        self.fire = False
        self.image = shell_img

    def render(self):

        if enemyH.fire_counter == 0:                                #Sets the position of the EnemyH bullet to the front of the EnemyH plane if
                                                                    #EnemyH has not yet fired
            self.x = enemyH.x
            self.y = enemyH.y + enemyH.height/2 - self.height/2 + 7
            self.fire = True
            enemyH.fire_counter += 1

        self.position_check()                   #Calls the defined methods
        self.player_check()

        if self.fire == True:

            if powerUp.freeze == True or ring_of_fire.present == True:          #Stops the bullet if the freeze powerup or ring of fire has been activated
                self.speed = 0
            else:
                self.direction_check()                              #Sets the speed back to the appropriate non zero value once the freeze powerup
                                                                    #or ring of fire is no longer active
            self.x += self.speed                                    #Adjusts the position of the bullet according to its speed
            gameDisplay.blit(self.image, (self.x, self.y))          #Blits the bullet to the screen
            player.hit = False

    def direction_check(self):                              #Sets the speed and orientation of the bullet according to the direction of
                                                            #motion of EnemyH
        if enemyH.direction == "right":
            self.speed = 8
            self.image = pygame.transform.rotate(shell_img, 270)

        elif enemyH.direction == "left":
            self.speed = -8
            self.image = pygame.transform.rotate(shell_img, 90)

    def position_check(self):           #Recognizes that EnemyH is no longer firing if the bullet has left the screen

        if enemyH.direction == "right" and self.x - self.width > display_width or enemyH.direction == "left" and self.x < 0:

            self.fire = False

    def player_check(self):             #Checks to see if the bullet has collided with the player plane and responds accordingly

        if player.x < self.x < player.x + player.width and player.y < self.y < player.y + player.height:
            if self.fire == True:
                player.hit = True
                self.fire = False

        elif player.x < self.x + self.width < player.x + player.width and player.y < self.y < player.y + player.height:
            if self.fire == True:
               player.hit = True
               self.fire = False

        elif player.x < self.x < player.x + player.width and player.y < self.y + self.height < player.y + player.height:
            if self.fire == True:
                player.hit = True
                self.fire = False

        elif player.x < self.x + self.width < player.x + player.width and player.y < self.y + self.height < player.y + player.height:
            if self.fire == True:
                player.hit = True
                self.fire = False

class EnemyBulletV:

    def __init__(self):

        self.x = 0
        self.y = 0
        self.width = shell_size
        self.height = shell_size
        self.speed = 0
        self.fire = False
        self.image = pygame.transform.rotate(shell_img, 180)

    def render(self):

       if enemyV.fire_counter == 0:                                 #Sets the position of the EnemyV bullet to the front of the EnemyV plane if
                                                                    #EnemyV has not yet fired
            self.x = enemyV.x + enemyV.width/2 - self.width/2
            self.y = enemyV.y + enemyV.height
            self.fire = True
            enemyV.fire_counter += 1

       self.position_check()            #Calls the defined methods
       self.player_check()

       if self.fire == True:

           if powerUp.freeze == True or ring_of_fire.present == True:           #Stops the bullet if the freeze powerup or ring of fire has been activated
               self.speed = 0
           else:
               self.speed = 8           #Sets the speed back to the appropriate non zero value once the freeze powerup or ring of fire is no longer active

           self.y += self.speed                                     #Adjusts the position of the bullet according to its speed
           gameDisplay.blit(self.image, (self.x, self.y))           #Blits the bullet to the screen
           player.hit = False

    def position_check(self):           #Recognizes that EnemyV is no longer firing if the bullet has left the screen

        if self.y > display_height:

            self.fire = False

    def player_check(self):             #Checks to see if the bullet has collided with the player plane and responds accordingly

        if player.x < self.x < player.x + player.width and player.y < self.y < player.y + player.height:
            if self.fire == True:
                player.hit = True
                self.fire = False

        elif player.x < self.x + self.width < player.x + player.width and player.y < self.y < player.y + player.height:
            if self.fire == True:
               player.hit = True
               self.fire = False

        elif player.x < self.x < player.x + player.width and player.y < self.y + self.height < player.y + player.height:
            if self.fire == True:
                player.hit = True
                self.fire = False

        elif player.x < self.x + self.width < player.x + player.width and player.y < self.y + self.height < player.y + player.height:
            if self.fire == True:
                player.hit = True
                self.fire = False

class EnemyBullet2:

    def __init__(self):

        self.x = 0
        self.y = 0
        self.x2 = 0
        self.y2 = 0
        self.width = shell_size
        self.height = shell_size
        self.speed = 0
        self.fire = False
        self.firing = False
        self.image = pygame.transform.rotate(shell_img, 180)
        self.image2 = pygame.transform.rotate(shell_img, 180)
        self.hit1 = False
        self.hit2 = False

    def render(self):

        if enemy2.present == True and enemy2.y == 0.15 * display_height and enemy2.movex == False and self.fire == True and self.firing == False:

            self.x = enemy2.x + enemy2.width/3 - self.width/2                   #Sets the positions of both of the bullets to be at the front of the wings
            self.x2 = enemy2.x + 2 * enemy2.width/3 - self.width/2              #of Enemy2 if Enemy2 is not currently firing
            self.y = enemy2.y + enemy2.height/2
            self.image = pygame.transform.rotate(shell_img, 180)
            self.image2 = pygame.transform.rotate(shell_img, 180)
            self.hit1 = False
            self.hit2 = False
            self.firing = True

        self.position_check()           #Calls the defined methods
        self.player_check()

        if self.firing == True:

            self.speed = 5              #Sets the speed back to the appropriate non zero value if the freeze powerup or ring of fire is no longer active

            if powerUp.freeze == True or ring_of_fire.present == True:          #Stops the bullet if the freeze powerup or ring of fire has been activated
                self.speed = 0

            self.y += self.speed                                        #Adjusts the position of the bullet according to it speed
            gameDisplay.blit(self.image, (self.x, self.y))              #Blits the bullets to the screen
            gameDisplay.blit(self.image2, (self.x2, self.y))

    def position_check(self):           #Recognizes that Enemy2 is no longer firing if the bullet has left the screen

        if self.y > display_height:
            self.fire = False
            self.firing = False
            self.speed = 0
            self.y = enemy2.y + enemy2.height/2
            enemy2.movex = True

    def player_check(self):             #Checks to see if either of the Enemy2 bullets have collided with the player plane and responds accordingly

        if player.x < self.x < player.x + player.width and player.y < self.y < player.y + player.height:
            if self.hit1 == False:
                if player.shield == False:
                    player.health -= 10
                if player.shield == True:
                    player.shield_health -= 10
                self.image = transparent_img
                self.hit1 = True

        if player.x < self.x2 < player.x + player.width and player.y < self.y < player.y + player.height:
            if self.hit2 == False:
                if player.shield == False:
                    player.health -= 10
                if player.shield == True:
                    player.shield_health -= 10
                self.image2 = transparent_img
                self.hit2 = True

class EnemyBullet3:

    def __init__(self):

        self.x = 0
        self.y = 0
        self.fire = False
        self.direction = "up"
        self.image = enemy_missile_img
        self.fire_counter = 0

    def render(self):

        self.position_selector()            #Calls the defined methods
        self.position_check()
        self.player_check()

        if self.fire_counter == 5 and enemy3.present == True:           #Recognizes that a new Enemy3 has been initiated and resets the
                                                                        #appropriate attributes
            self.fire = False
            self.fire_counter = 0
            enemy3.movex = True

        if powerUp.freeze == True or ring_of_fire.present == True:          #Stops the missile if the freeze powerup or ring of fire has been activated
            self.speed = 0

        if powerUp.freeze == False and ring_of_fire.present == False:       #Sets the speed back to the appropriate non zero value once the freeze
            if enemy3.x < display_width/2:                                  #powerup or ring of fire is no longer active
                self.speed = 5

            elif enemy3.x > display_width/2:
                self.speed = -5

        if self.fire == True and enemy3.movex == False:

            self.x += self.speed                                    #Adjusts the position of the missile according to its speed
            gameDisplay.blit(self.image, (self.x, self.y))          #Blits the missile to the screen

    def position_selector(self):

        if self.fire == False and enemy3.present == True and enemy3.movex == False:

            y_position_list = [enemy3.y + 0.5 * enemy3.height, enemy3.y + 0.7 * enemy3.height]

            y_number = random.randrange(0,2)

            self.y = y_position_list[y_number]          #Sets a random vertical position so that the missile may fire from one of the two cannons

            if enemy3.x < display_width / 2:            #Sets the speed and orientation of the missile according to the horizontal position of Enemy3

                self.x = enemy3.x

                if self.direction == "up":
                    self.image = pygame.transform.rotate(enemy_missile_img, 270)

                elif self.direction == "down":
                    self.image = pygame.transform.rotate(enemy_missile_img, 90)

                elif self.direction == "right":
                    self.image = enemy_missile_img

                elif self.direction == "left":
                    self.image = pygame.transform.rotate(enemy_missile_img, 180)

                self.speed = 5

            elif enemy3.x > display_width / 2:

                self.x = enemy3.x + enemy3.width

                if self.direction == "up":
                    self.image = pygame.transform.rotate(enemy_missile_img, 90)

                elif self.direction == "down":
                    self.image = pygame.transform.rotate(enemy_missile_img, 270)

                elif self.direction == "right":
                    self.image = pygame.transform.rotate(enemy_missile_img, 180)

                elif self.direction == "left":
                    self.image = enemy_missile_img

                self.speed = -5

            self.fire = True

    def position_check(self):           #Checks to see if the missile has left the screen and notifies Enemy3 that it may fire again if this is the case

        if enemy3.x == 0 or enemy3.x == display_width - enemy3.width:

            if self.fire == True:

                if self.x < -10 or self.x > display_width + 10:
                    self.fire = False
                    self.fire_counter += 1

    def player_check(self):             #Checks to see if the missile has collided with the player plane and responds accordingly

        if enemy3.x == 0 or enemy3.x == display_width - enemy3.width:

            if self.fire == True:

                if player.x < self.x < player.x + player.width and player.y < self.y < player.y + player.height:

                    if player.shield == False:
                        player.health -= 20
                    elif player.shield == True:
                        player.shield_health -= 20

                    self.fire = False
                    self.fire_counter += 1

class Mine:

    def __init__(self):

        self.x = 0
        self.y = 0
        self.width = mine_width
        self.height = mine_height
        self.speedx = 0
        self.present = False
        self.image = mine_img
        self.hit = False
        self.explosion = False
        self.e_counter = 0
        self.player_hit = False

    def render(self):

        if self.hit == True:                            #Triggers an explosion if the player collides with the mine

            pygame.mixer.Sound.play(hit_sound2)

            self.image = explosion_e2_img
            self.explosion = True
            self.hit = False
            self.x -= 20
            self.y -= 20

        if self.explosion == True:                      #Sets a timer to determine when to enlarge the explosion and when to stop it
                                                        #Then deducts from the player's health accordingly
            self.e_counter += 1

            if self.e_counter == 15:

                self.image = explosion2_e2_img
                self.x = self.x + explosion_e2_width / 2 - explosion2_e2_width / 2
                self.y = self.y + explosion_e2_height / 2 - explosion2_e2_height / 2

            elif self.e_counter == 30:

                self.present = False
                self.explosion = False
                self.e_counter = 0

                if self.player_hit == True:

                    player.health -= 30
                    self.player_hit = False

        self.position_selector()                #Calls the defined methods
        self.position_check()
        self.player_check()

        if powerUp.freeze == True:              #Stops the mine if the freeze powerup has been activated
            self.speedx = 0

        elif powerUp.freeze == False and self.speedx == 0 and self.explosion == False:      #Sets the speed back to the appropriate non zero value if the
            if self.x < 0.5 * display_width:                                                #freeze powerup is no longer active
                self.speedx = 1
            if self.x > 0.5 * display_width:
                self.speedx = -1

        if self.present == True:

            self.x += self.speedx                                   #Adjusts the position of the mine according to its speed
            gameDisplay.blit(self.image, (self.x, self.y))          #Blits the mine to the screen


    def position_selector(self):

        if self.present == False:

            special_number = random.randrange(0,300)            #Selects a random number from 0 to 300

            if special_number == 5:                             #Initiates a new mine if that number is 5

                self.present = True
                self.x = random.randrange(0.1 * display_width, 0.9 * display_width)         #Selects a random horizontal position
                self.y = random.randrange(0.3 * display_height, 0.9 * display_height)       #Selects a random vertical position

                if self.x < 0.5 * display_width:            #Sets the speed of the mine accordingly
                    self.speedx = 1
                if self.x > 0.5 * display_width:
                    self.speedx = -1

                self.image = mine_img

    def position_check(self):           #Checks to see if the mine is no longer on the screen and responds accordingly

        if self.x + self.width < 0 or self.x > display_width:
            self.present = False

    def player_check(self):             #Checks to see if the player has collided with the mine and responds accordingly

        if player.x < self.x < player.x + player.width and player.y < self.y < player.y + player.height:
            if self.present == True and self.image == mine_img:
                if player.shield == True:
                    player.shield_health = 0
                else:
                    self.player_hit = True
                self.hit = True

        elif player.x < self.x + self.width < player.x + player.width and player.y < self.y < player.y + player.height:
            if self.present == True and self.image == mine_img:
                if player.shield == True:
                    player.shield_health = 0
                else:
                    self.player_hit = True
                self.hit = True

        elif player.x < self.x < player.x + player.width and player.y < self.y + self.height < player.y + player.height:
            if self.present == True and self.image == mine_img:
                if player.shield == True:
                    player.shield_health = 0
                else:
                    self.player_hit = True
                self.hit = True

        elif player.x < self.x + self.width < player.x + player.width and player.y < self.y + self.height < player.y + player.height:
            if self.present == True and self.image == mine_img:
                if player.shield == True:
                    player.shield_health = 0
                else:
                    self.player_hit = True
                self.hit = True

class Tutorial:

    def __init__(self):

        self.tutorial_1 = False
        self.counter_1 = False
        self.tutorial_2 = False
        self.counter_2 = False
        self.tutorial_3 = False
        self.counter_3 = False
        self.tutorial_4 = False
        self.counter_4 = False
        self.tutorial_5 = False
        self.counter_5 = False
        self.tutorial_6 = False
        self.counter_6 = False
        self.tutorial_7 = False
        self.counter_7 = False
        self.tutorial_8 = False
        self.counter_8 = False
        self.run = True

# INSTANCES #

main_menu = Main_Menu()
settings = Settings()
game_over = Game_Over()
player = Plane()
bullet = Bullet()
enemyH = EnemyH()
enemyV = EnemyV()
enemy2 = Enemy2()
enemy3 = Enemy3()
enemyBulletH = EnemyBulletH()
enemyBulletV = EnemyBulletV()
enemyBullet2 = EnemyBullet2()
enemyBullet3 = EnemyBullet3()
powerUp = PowerUp()
mine = Mine()
ring_of_fire = ROF()
tutorial = Tutorial()

# LOOPS #

def gameLoop():

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:        #Arrow key event handling that adjusts the direction of the player plane based on the keys that are pressed

                if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
                    player.directionx = "left"
                    player.stopx = False
                    player.stopy = True

                if pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
                    player.directionx = "right"
                    player.stopx = False
                    player.stopy = True

                if pygame.key.get_pressed()[pygame.K_UP] != 0:
                    player.directiony = "up"
                    player.stopy = False
                    player.stopx = True

                if pygame.key.get_pressed()[pygame.K_DOWN] != 0:
                    player.directiony = "down"
                    player.stopy = False
                    player.stopx = True

                if event.key == pygame.K_SPACE:     #Pressing the space bar allows the player to shoot

                    if bullet.fire == False:

                        bullet.x = player.x + player.width/2 - bullet.width/2
                        bullet.y = player.y
                        bullet.fire = True

                if event.key == pygame.K_a:         #Pressing the A key allows the player to activate their ring of fire

                    if ring_of_fire.counter > 0:

                        ring_of_fire.present = True
                        ring_of_fire.counter -= 1

                if pygame.key.get_pressed()[pygame.K_LEFT] == 0 and pygame.key.get_pressed()[pygame.K_RIGHT] == 0:      #Allows for smoother plane motion
                    player.stopx = True

                if pygame.key.get_pressed()[pygame.K_UP] == 0 and pygame.key.get_pressed()[pygame.K_DOWN] == 0:
                    player.stopy = True

        gameDisplay.blit(game_background, (0,0))

        if player.health <= 0:      #Pauses the game for 3 seconds before going to the game over screen after the player has lost their health

            pygame.time.delay(3000)

            game_over.run = True

            while game_over.run == True:

                game_over.render()

                if game_over.menu == True:

                    gameExit = True
                    game_over.menu = False

        else:

            if tutorial.run == False:           #Ensures that the tutorial images will not appear during the game if Tutorial is unchecked in settings

                tutorial.tutorial_1 = True
                tutorial.tutorial_2 = True
                tutorial.tutorial_3 = True
                tutorial.tutorial_4 = True
                tutorial.tutorial_5 = True
                tutorial.tutorial_6 = True
                tutorial.tutorial_7 = True
                tutorial.tutorial_8 = True

            if tutorial.tutorial_1 == True:     #Player may move and shoot and activate their ring of fire once the game begins

                player.render()
                bullet.render()
                ring_of_fire.render()

            if tutorial.tutorial_2 == True and player.time_counter >= 200:      #EnemyH is initiated 200 ms after the game begins

                enemyH.render()
                enemyBulletH.render()

                if player.time_counter >= 300:      #EnemyV is initiated 300 ms after the game begins

                    enemyV.render()
                    enemyBulletV.render()

            if tutorial.tutorial_8 == True and player.time_counter >= 200:      #Powerups are initiated 200 ms after the game begins

                powerUp.update()

            if tutorial.tutorial_3 == True and player.time_counter >= 600:      #Enemy2 is initiated 600 ms after the game begins

                enemy2.render()
                enemyBullet2.render()

            if tutorial.tutorial_4 == True and player.time_counter >= 800:      #Enemy3 is initiated 800 ms after the game begins

                enemy3.render()
                enemyBullet3.render()

            if tutorial.tutorial_7 == True and player.time_counter >= 650:      #Mines are initiated 650ms after the game begins

                mine.render()

        if tutorial.tutorial_1 == False:        #Shows the tutorial images in the appropriate sequence as time progresses

            gameDisplay.blit(tutorial_1_img, (0.5 * display_width - 203.5, 0.5 * display_height - 105.5))
            tutorial.counter_1 = True
            tutorial.tutorial_1 = True

        elif tutorial.tutorial_6 == False and player.time_counter >= 300:

            gameDisplay.blit(tutorial_6_img, (0.5 * display_width - 203.5, 0.5 * display_height - 100))
            tutorial.counter_6 = True
            tutorial.tutorial_6 = True

        elif tutorial.tutorial_2 == False and player.time_counter >= 700:

            gameDisplay.blit(tutorial_2_img, (0.5 * display_width - 203.5, 0.5 * display_height - 141.5))
            tutorial.counter_2 = True
            tutorial.tutorial_2 = True

        elif tutorial.tutorial_8 == False and player.time_counter >= 1400:

            gameDisplay.blit(tutorial_8_img, (0.5 * display_width - 203.5, 0.5 * display_height - 112.5))
            tutorial.counter_8 = True
            tutorial.tutorial_8 = True

        elif tutorial.tutorial_3 == False and player.time_counter >= 2200:

            gameDisplay.blit(tutorial_3_img, (0.5 * display_width - 203.5, 0.5 * display_height - 123))
            tutorial.counter_3 = True
            tutorial.tutorial_3 = True

        elif tutorial.tutorial_5 == False and player.time_counter >= 3000:

            gameDisplay.blit(tutorial_5_img, (0.5 * display_width - 203.5, 0.5 * display_height - 123))
            tutorial.counter_5 = True
            tutorial.tutorial_5 = True

        elif tutorial.tutorial_4 == False and player.time_counter >= 3500:

            gameDisplay.blit(tutorial_4_img, (0.5 * display_width - 203.5, 0.5 * display_height - 141.5))
            tutorial.counter_4 = True
            tutorial.tutorial_4 = True

        elif tutorial.tutorial_7 == False and player.time_counter >= 4000:

            gameDisplay.blit(tutorial_7_img, (0.5 * display_width - 203.5, 0.5 * display_height - 100))
            tutorial.counter_7 = True
            tutorial.tutorial_7 = True

        pygame.display.update()

        if tutorial.run == True:        #Pauses the game for 5000 ms everytime a tutorial image is shown

            if tutorial.counter_1 == True:

                pygame.time.delay(5000)
                tutorial.counter_1 = False

            elif tutorial.counter_2 == True:

                pygame.time.delay(5000)
                tutorial.counter_2 = False

            elif tutorial.counter_3 == True:

                pygame.time.delay(5000)
                tutorial.counter_3 = False

            elif tutorial.counter_4 == True:

                pygame.time.delay(5000)
                tutorial.counter_4 = False

            elif tutorial.counter_5 == True:

                pygame.time.delay(5000)
                tutorial.counter_5 = False

            elif tutorial.counter_6 == True:

                pygame.time.delay(5000)
                tutorial.counter_6 = False

            elif tutorial.counter_7 == True:

                pygame.time.delay(5000)
                tutorial.counter_7 = False

            elif tutorial.counter_8 == True:

                pygame.time.delay(5000)
                tutorial.counter_8 = False

        clock.tick(60)

def appLoop():

    appExit = False
    gameExit = False

    while not appExit:

        while main_menu.run == True:

            main_menu.render()

        while settings.run == True:

            settings.render()

        if gameExit == True:

            gameExit = False

        gameLoop()

pygame.mixer.music.load("Audio/Airstrike_Music.wav")      #Plays music during the game
pygame.mixer.music.play(-1)                         #Allows song file to loop to the beginning everytime it finishes

appLoop()
