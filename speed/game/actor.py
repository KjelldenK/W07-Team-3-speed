from game import constants
from game.point import Point

class Actor:
    """A visible, moveable thing that participates in the game. The responsibility of Actor is to keep track of its appearance, position 
    and velocity in 2d space.

    Stereotype:
        Information Holder

    Attributes:
        _text (string): The textual representation of the actor.
        _position (Point): The actor's position in 2d space.
        _points the acotrs points that it will give.
    """
    def __init__(self):

        self._text = ""
        self._position = Point(0,0)
        self._points = int
        
        

    def get_position(self):
        """Gets the actor's position in 2d space.
        
        Args:
            self (Actor): an instance of Actor.

        Returns:
            Point: The actor's position in 2d space.
        """   
        return self._position

    def get_text(self):
        """Gets the actor's textual representation.
        
        Args:
            self (Actor): an instance of Actor.

        Returns:
            string: The actor's textual representation.
        """
        return self._text

    def get_points(self):
        """Gets the actor's ponts representation.
        
        Args:
            self (Actor): an instance of Actor.

        Returns:
            int: The actor's points representation.
        """
        return self._points
    
    def set_position(self, position):
        """Updates the actor's position to the given one.
        
        Args:
            self (Actor): An instance of Actor.
            position (Point): The given position.
        """
        self._position = position

    def set_text(self, text):
        """Updates the actor's text to the given value.
        
        Args:
            self (Actor): An instance of Actor.
            text (string): The given value.
        """
        self._text = text
    
    def set_points(self, points):
        """Updates the actor's points to the given value.
        
        Args:
            self (Actor): An instance of Actor.
            points (string): The given value.
        """
        self._points = points

    