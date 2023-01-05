import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Player(Actor):
    """A cycle player.
    The responsibility of the Player us to move itself and record the information about its position.

    """
    def __init__(self):
        self.started = False
        super().__init__()
        self._segments = []
        self._last_segment = Actor()

    def get_segments(self):
        """Returns an array with the segments behind the Player"""
        return self._segments

    def add_segment(self, segment):
        """Adds a segment behind the player. 
        
        Arg:
            segment(Actor)"""
        self._segments.append(segment)

    def move_next(self):
        """I move every segment of the Player.
            """
        self._last_segment = self._segments[-1]  #where the tail ended before moving
        for segment in self._segments:
          #  segment.move_next() # move each segment (They are Actor objects) 
            x = (segment.get_position().get_x() + segment.get_velocity().get_x()) % constants.MAX_X
            y = (segment.get_position().get_y() + segment.get_velocity().get_y()) % constants.MAX_Y
            segment.set_position(Point(x, y))
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
             # decreasing from the last one to the first one
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)  
            # all of the segments will move
        self.grow_tail()
        # to start drawing a tail behind them but it stops working

    def get_head(self):
        """Returns the first element of the segments array, the head of the Player."""
        return self._segments[0]

    def grow_tail(self):
        #finish this idea
        position_start = self._last_segment.get_position()  #where the tail started
        number_of_segments = len(self._segments)
        for i in range(number_of_segments):  #maybe the error is in this for
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            self._segments[i].set_position(position)
            # segment.set_position(position)
            # segment.set_velocity(velocity) 
            # segment.set_text("#")
            # segment.set_color(tail.get_color())
            # self._segments.append(segment)
            
        
        last_segment = Actor()
        last_segment.set_position(position_start)
        last_segment.set_velocity(self._last_segment.get_velocity())
        last_segment.set_text("#")
        last_segment.set_color(self._last_segment.get_color())
        self._segments.append(last_segment)

    def turn_head(self, velocity): #receive a point
        """changes the velocity of the Player.
        
        Arg:
            velocity(Point)"""
        self._segments[0].set_velocity(velocity)  # the head is in the 0 index
    
