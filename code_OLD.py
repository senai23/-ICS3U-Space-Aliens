#!/usr/bin/env python3


# Created by: Senai
# Created on: December 2023
# This program is the "Space Aliens" program on the PyBadge


# Pybadge screen size is 160x128 and sprites are 16x16
import ugame
import stage
import time
import random

import constants


def splash_scene():
    # this function is splash scene

    # get sound ready
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

    # an image bank for CircuitPython
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # set the background to image 0 in bank
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X
                            constants.SCREEN_Y)

    # create a statge fro the backgrounf to show up on
    # and set the frame rate to 60fps
    # sets the background to image 0 in the image bank
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X,
                             constants.SCREEN_Y)

    # used this program to split the image into tile:
     #   https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png

    background.tile(2, 2, 0)  # blank white

    background.tile(3, 2, 1)

    background.tile(4, 2, 2)

    background.tile(5, 2, 3)

    background.tile(6, 2, 4)

    background.tile(7, 2, 0)  # blank white



    background.tile(2, 3, 0)  # blank white

    background.tile(3, 3, 5)

    background.tile(4, 3, 6)

    background.tile(5, 3, 7)

    background.tile(6, 3, 8)

    background.tile(7, 3, 0)  # blank white



    background.tile(2, 4, 0)  # blank white

    background.tile(3, 4, 9)

    background.tile(4, 4, 10)

    background.tile(5, 4, 11)

    background.tile(6, 4, 12)

    background.tile(7, 4, 0)  # blank white



    background.tile(2, 5, 0)  # blank white

    background.tile(3, 5, 0)

    background.tile(4, 5, 13)

    background.tile(5, 5, 14)

    background.tile(6, 5, 0)

    background.tile(7, 5, 0)  # blank white

    # create a stage for the background to show up on 
    #  and set the frame rate to 60fps 
    game= stage.Stage(ugame.display, constants.FPS)
    # set the layer, items show up in order
    game =layers = {background}
    # render the background and initial location of sprite list 
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # Wait for 2 seconds
        time.sleep(2.0)
        menu_scene()

 
def menu_scene():
    # this function is the main game game_scene


    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
   
    # add text objects
    text=[]
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALLETTE, buffer=None)
    text1.move(20, 10)
    text1. text("MT Game Studios")
    text.append(text1)


    text2 = stage.Text(width=29, height=12, font=None, palette= constants.RED_PALLETTE, buffer=None)
    text2.move(40, 110)
    text2. text("PRESS START")
    text.append(text2)


    # set the background to image 0 in the image bank
    #   and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white




    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game= stage.Stage(ugame.display, constants.FPS)
    # set the layers, items show up in order
    game.layers = [background]
    # render the background and the initial location of sprite list
    # most likey you will only render the background once per game scene
    game.render_block()
   
    # repeat forever, game loop
    while True:
        # Wait for 2 seconds
        time sleep(2.0)
        menu_scene()


def game_scene():
    # this function is the main game game_scene

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # buttons that you want to keep state information on 
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # get sound ready
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    
    # set the background to image 0 in the image bank
    #   and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_X,
                            constants.SCREEN_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEn_GRID_Y):
            tile_picked = random.randint(1, 3)
            background.tile(x_location, y_location, tile_picked)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y) 
 
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

    alien = stage.Sprite(image_bank_sprites, 9,
                      int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
                      16)
    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game= stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = [ship] + [background]
    # render the background and the initial location of sprite list
    # most likey you will only render the background once per game scene
    game.render_block()
   
    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X:
            pass
        # A button to fire
        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        
            
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
           pass
        if keys & ugame.K_RIGHT:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            else: 
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_LEFT:
            if ship.x >=0:
                ship.move(ship.x - 1, ship.y)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass

        # update game logic
        # play sound if A was just button_just_pressed
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)
            pass 
        # redraw Sprites
        game.render_sprites([ship] + [alien])
        game.tick()



def menu_scene():
    # this function is the main game game_scene

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    
    # add text objects
    text=[]
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALLETTE, buffer=None)
    text1.move(20, 10)
    text1. text("MT Game Studios")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, palette= constants.RED_PALLETTE, buffer=None)
    text2.move(40, 110)
    text2. text("PRESS START")
    text.append(text2)

    # set the background to image 0 in the image bank
    #   and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y) 
 
    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game= stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and the initial location of sprite list
    # most likey you will only render the background once per game scene
    game.render_block()
   
    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:
            game_scene()
    
        # redraw Sprites
        game.tick()


if __name__ == "__main__":
    splash_scene()
