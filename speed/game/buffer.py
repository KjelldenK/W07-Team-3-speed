from game.point import Point
from game.actor import Actor
class Buffer(Actor):
    """A visible, moveable thing that participates in the game. The responsibility of Actor is to keep track of its appearance, position 
    and velocity in 2d space.

    Stereotype:
        Information Holder

    Attributes:
        _text (string): The textual representation of the actor.
        _position (Point): The actor's position in 2d space.
        _velocity (Point): The actor's speed and direction.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Actor): an instance of Actor.
        """
        self._buffer_letters = ''
        self._word = str
        position = Point(1, 20)
        self.set_position(position)

        


    def add_letter(self, letter):
        """Adds a litter to buffer

        Args:
            self (Actor): an instance of Actor
        """
        self._buffer_letters += letter
        self.set_text(f"Buffer: {self._buffer_letters}")


    def get_buffer(self):
        """Sends what is in buffer. 

        Args:
            self (Actor): an instance of Acror
        """

        return self._buffer_letters

    def clear_buffer(self):
        """ clears buffer
        """
        self._buffer_letters = ""

    def set_word(self):
        """ Takes whats in buffer and saves it as a usable word for checking.
        """
        self._word = self._buffer_letters
        self.clear_buffer()

    def get_set_word(self):
        """Gets and sends the saved word to check if the word is in play.
        """
        return self._word