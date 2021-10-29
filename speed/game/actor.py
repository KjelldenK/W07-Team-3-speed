

class Actor:

    def __init__(self):

        self._text = ""
        self._position = point(0,0)
        self._velocity = Point(0,0)
    
    def get_position(self):
        return self._position

    def get_text(self):
        return self._text

    def get_velocity(self):
        return self._velocity
    
    