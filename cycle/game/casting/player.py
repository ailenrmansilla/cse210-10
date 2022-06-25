import constants
from game.casting.actor import Actor
from game.shared.point import Point
import random


class Player(Actor):
    """A cycle player.
    The responsibility of the Player us to move itself and record the information about its position.

    """
    def __init__(self):
        super().__init__()
        self._segments = []
        # self._prepare_cycle()
        self._last_segment = Actor()

    def get_segments(self):
        """Returns an array with the segments behind the Player"""
        return self._segments

    def add_segment(self, segment):
        self._segments.append(segment)

    def move_next(self):
        #I CAN ADD ANOTHER SEGMENT AT THE END EVERYTIME IN THE SAME PLACE SO IT WILL LOOK LIKE STATIONARY BUT IT IS NOT... MAYBE?
        self._last_segment = self._segments[-1]  #where the tail ended before moving
        if len(self._segments) > 1:
            for segment in self._segments:
                segment.move_next()   # move each segment (They are Actor objects) 
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
             # decreasing from the last one to the first one
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)  
            # all of the segments will move

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        #finish this idea
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity) 
            segment.set_text("#")
            segment.set_color(tail.get_color())
            self._segments.append(segment)
            
        position_start = self._last_segment.get_position()  #where the tail started
        last_segment = Actor()
        last_segment.set_position(position_start)
        last_segment.set_velocity(self._last_segment.get_velocity())
        segment.set_text("#")
        segment.set_color(self._last_segment.get_color())
        self._segments.append(segment)

    def turn_head(self, velocity): #receive a point
        self._segments[0].set_velocity(velocity)  # the head is in the 0 index
    
    # def _prepare_cycle(self): #the cycle has no tail at the beginning
    #     x = int((constants.MAX_X / 2) + random.randint(1,4))
    #     y = int(constants.MAX_Y / 2)
    #     position = Point(x * constants.CELL_SIZE, y)
    #     velocity = Point(0, 0)
    #     text = "O-O" #if i == 0 else "#"
    #     color = (random.randint(0,265),random.randint(0,265),random.randint(0,265)) #if i == 0 else constants.GREEN
    #     # the first segment is the head, the cycle which will move
    #     segment = Actor()
    #     segment.set_position(position)
    #     segment.set_velocity(velocity)
    #     segment.set_text(text)
    #     segment.set_color(color)
    #     self._segments.append(segment) 

        # for i in range(constants.SNAKE_LENGTH):
        #     position = Point(x - i * constants.CELL_SIZE, y)
        #     velocity = Point(1 * constants.CELL_SIZE, 0)
        #     text = "O-O" if i == 0 else "#"
        #     color = (random.randint(0,265),random.randint(0,265),random.randint(0,265)) #if i == 0 else constants.GREEN
            
        #     segment = Actor()
        #     segment.set_position(position)
        #     segment.set_velocity(velocity)
        #     segment.set_text(text)
        #     segment.set_color(color)
        #     self._segments.append(segment) 