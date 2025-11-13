from .cue import Cue
from .framerate import Framerate
from .timecode import Timecode


class Project:
    """ Defines a scoring project -- a film, TV show, etc. """
    def __init__(self, name: str, code: str, framerate: Framerate):
        self.name: str = name
        self.code: str = code
        self.framerate: Framerate = framerate
        self.cues: list[Cue]

    def _register_cue(self, cue: Cue):
        if cue not in self.cues:
            self.cues.append(cue)
            cue.framerate = self.framerate

    def new_derived_cue(self, cue: Cue):
        """ Creates a new derived cue from the given cue. """

    def get_interval(a: Cue, b: Cue) -> Timecode:
        """ Returns the time between cues a and b as a Timecode object. """

    def renumber_cues(self):
        """ Clears and re-increments cue numbers. """

    def split_cue(self):
        """ Splits a given cue into two cues. """