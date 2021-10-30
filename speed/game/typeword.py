import random
from game.actor import  Actor
from game import constants
from game.point import Point
class TypeWord(Actor):


    def __init__(self):

        super().__init__()
        self._points = 0
        self._words_list = []
        self._prepare_words()


    def add_word(self,text, position, points):
        """ Adds a new word to the game.
        """
        
        word = Actor()
        word.set_text(text)
        word.set_position(position)
        word.set_points(points)
        self._words_list.append(word)

    def new_word(self):
        """ creates the info to make a new word and have it have its own spot on the game board.
        """
        text = constants.LIBRARY[random.randint(1,10000)]
        self._points = int(len(text))
        x = random.randint(1, constants.MAX_X - 2)
        y = random.randint(1, constants.MAX_Y - 2)
        position = Point(x, y)
        self.add_word(text, position, self._points)
    
    def remove_word(self, word_position):
        """ removes a word from play.
        """
        self._words_list.pop(word_position)
        self.new_word()
        

    def get_words(self):
        """Gets the list of words in play.
        """
        return self._words_list

    def _prepare_words(self):
        """ at the start of the game will make as many words as or in start_words in the constants file.
        """
        for _ in range(0, constants.STARTING_WORDS):
            text = constants.LIBRARY[random.randint(1,10000)]
            self._points = int(len(text))
            x = random.randint(1, constants.MAX_X - 2)
            y = random.randint(1, constants.MAX_Y - 2)
            position = Point(x, y)
            self.add_word(text, position, self._points)



