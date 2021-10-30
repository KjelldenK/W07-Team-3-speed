from time import sleep
from game import constants
from game.typeword import TypeWord
from game.score import Score
from game.buffer import Buffer

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        food (buffer): The word that the player is typeing.
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
        typeword (typeword): typeword the word that needs to be typed to gain points.
    """
    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._typeword = TypeWord()
        self._input_service = input_service
        self._output_service = output_service
        self._score = Score()
        self._buffer = Buffer()
        self._keep_playing = True

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """

        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)


    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the key event to place a letter into buffer or let the game know to check for the word in play.

        Args:
            self (Director): An instance of Director.
        """
        letter = self._input_service.get_letter()
        
        if letter == "*":
            self._buffer.set_word()
        else:
            self._buffer.add_letter(letter)

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for if a word is in play and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        if self._buffer.get_set_word() != (""):
            self._handle_word_check()



    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actor(self._buffer)
        self._output_service.draw_actors(self._typeword.get_words())
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()
        pass


    def _handle_word_check(self):
        """Handles if the word that they player put in is in the game 
        and if it is removes that word and makes a new word

        Args:
            self (Director): An instance of Director.
        """
        words = self._typeword.get_words()
        for i in range(0,5):
            if self._buffer.get_set_word() == words[i].get_text():
                points = words[i].get_points()
                self._score.add_points(points)
                self._typeword.remove_word(i)