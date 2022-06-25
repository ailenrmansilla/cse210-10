# Players can move up, down, left and right...
# Player one moves using the W, S, A and D keys.
# Player two moves using the I, K, J and L keys.
# Each player's trail grows as they move.
# Players try to maneuver so the opponent collides with their trail.
# If a player collides with their opponent's trail...
# A "game over" message is displayed in the middle of the screen.
# The cycles turn white.
# Players keep moving and turning but don't run into each other.

import constants
import random
from game.casting.cast import Cast
from game.casting.actor import Actor
from game.casting.player import Player
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    # create the cast
    cast = Cast()
    player1 = Player()
    x = int((constants.MAX_X / 2) + 20)
    y = int(constants.MAX_Y / 2)
    position = Point(x,y)
    velocity = Point(0,0) # it starts static
    text = "0-0"
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = Color(r,g,b)
    player1.set_position(position)
    player1.set_velocity(velocity)
    player1.set_text(text)
    player1.set_color(color)
    first_segment = player1
    player1.add_segment(first_segment)  #check if this is right

    player2 = Player()
    x = int((constants.MAX_X / 2) - 20)
    y = int(constants.MAX_Y / 2)
    position = Point(x,y)
    velocity = Point(0,0) 
    text = "0-0"
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = Color(r,g,b)
    player2.set_position(position)
    player2.set_velocity(velocity)
    player2.set_text(text)
    player2.set_color(color)
    first_segment = player2
    player2.add_segment(first_segment) 

    cast.add_actor("player1", player1) 
    cast.add_actor("player2", player2)
    # cast.add_actor("scores", Score())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script() # it stores the next actions in those groups
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script) # it sends all the necessary actiosn to start the game


if __name__ == "__main__":
    main()