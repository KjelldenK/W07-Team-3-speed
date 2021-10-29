from time import sleep
from game import constants
from game.buffer import Buffer 
from game.score import Score
from game.typeword import Word

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    """
       
    def __init__(self, input_service, output_service):
          """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
          self.Buffer = Buffer()
          self.input_service = input_service
          self.keep_playing = True
          self.output_service = output_service
          self.score = Score()
          self._word = Word()
          
        
    def start_game(self):
         """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
         while self.keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)
    
    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction.

        Args:
            self (Director): An instance of Director.
        """
        direct = self._input_service.get_direction()
        self._word.move_word(direct)

    def _do_updates(self):
        """Updates the important game information for each round of play. 

        Args:
            self (Director): An instance of Director.
        """
        self._spells_correctly()
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_word(self._buffer)
        self._output_service.draw_words(self._word.get_word())
        self._output_service.draw_word(self._score)
        self._output_service.flush_buffer()

    def _spells_correctly():
        pass

    
    




    