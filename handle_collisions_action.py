import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the two cycles.
    
    The responsibility of HandleCollisionsAction is to handle the situation when a cycle collides
    with the other one or when the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    # def _handle_food_collision(self, cast):
    #     """Updates the score nd moves the food if the snake collides with the food.
        
    #     Args:
    #         cast (Cast): The cast of Actors in the game.
    #     """
    #     score = cast.get_first_actor("scores")
    #     player1 = cast.get_first_actor("player1")
    #     head1 = player1.get_head()
    #     player2 = cast.get_first_actor("player2")
    #     head2 = player2.get_head()

    #     if head1.get_position().equals(food.get_position()):
    #         points = food.get_points()
    #         snake.grow_tail(points)
    #         score.add_points(points)
    #         food.reset()
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if one cycle collides with one of its segments or with a segment from the other cycle.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        # score = cast.get_first_actor("scores")
        player1 = cast.get_first_actor("player1")
        head1 = player1.get_segments()[0]
        tail1 = player1.get_segments()[1:] 
        player2 = cast.get_first_actor("player2")
        head2 = player2.get_segments()[0]
        tail2 = player2.get_segments()[1:] 

        #to see in the cycle 2 is touching the other player's tail
        for segment in tail1:
            if head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
                #print who wins and freeze the game

        #to see in the cycle 1 is touching the other player's tail
        for segment in tail2:
            if head1.get_position().equals(segment.get_position()):
                self._is_game_over = True
                #print who wins and freeze the game
        
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            player1 = cast.get_first_actor("player1")
            segments1 = player1.get_segments()
            
            player2 = cast.get_first_actor("player2")
            segments2 = player2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            #look for another way to print the message of game over or restaure the code for printing messages
            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments1:
                segment.set_color(constants.WHITE)
            for segment in segments2:
                segment.set_color(constants.WHITE)