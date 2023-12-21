#!/usr/bin/env python3


# Created by: Senai
# Created on: December 2023
# This program is the "Space Aliens" program on the PyBadge


import ugame
import stage
import constants

def game_scene():
    # this function is the main game game_scene

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # set the background to image 0 in the image bank
    #   and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8)

    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

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
            print("pass")
        if keys & ugame.K_O:
            print("pass")
        if keys & ugame.K_START:
            print("pass")
        if keys & ugame.K_SELECT:
            print("pass")
        if keys & ugame.K_RIGHT:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
        else:
            ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)


        if keys & ugame.K_LEFT:
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 1)
        if keys & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 1)




        # update game logic


        # redraw Sprites
        game.render_sprites({ship})
        game.tick()


if __name__ == "__main__":
    game_scene()
