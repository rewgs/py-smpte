from abc import ABC, abstractmethod

from .framerate import Framerate


class Timecode(ABC):
    """ Abstract base class for the two timecode subtypes: drop and non-drop. """

    def __init__(self, timecode: str):
        self._split: list[str] = self._split_timecode(timecode)
        self.hours: int = int(self._split[0])
        self.minutes: int = int(self._split[1])
        self.seconds: int = int(self._split[2])

    @staticmethod
    @abstractmethod
    def _split_timecode(timecode: str) -> list[str]:
        """ Splits a given timecode string into a list of strings (HH, MM, SS, FF). """


class Drop(Timecode):
    """ Defines drop timecodes: 29.97d, etc. """

    def __init__(self, framerate: Framerate, timecode: str):
        # TODO: Valid framerates
        self.valid: list[Framerate] = []
        if framerate not in self.valid:
            raise Exception(f"{framerate} is not a valid drop framerate!")
        super().__init__(timecode)

    # TODO: Similar to nondrop._split_timecode(), but deal with `;` for last field.
    @staticmethod
    def _split_timecode(timecode: str) -> list[str]:
        ...


class Nondrop(Timecode):
    """ Defines non-drop timecodes: 24, etc. """

    def __init__(self, framerate: Framerate, timecode: str):
        self.valid: list[Framerate] = [
            Framerate.FILM,
            Framerate.VIDEO,
        ]
        if framerate not in self.valid:
            raise Exception(f"{framerate} is not a valid non-drop framerate!")
        super().__init__(timecode)

    @staticmethod
    def _split_timecode(timecode: str) -> list[str]:
        # TODO: Deal with strings with more than 3 colons, etc.
        try:
            split: list[str] = timecode.split(":", 4)
        # TODO: Actually handle this error, specify what to do with different Exceptions, etc.
        except Exception as error:
            raise error
        else:
            return split


def timecode(framerate: Framerate, timecode: str) -> Timecode:
    drop = Drop(framerate, timecode)
    nondrop = Nondrop(framerate, timecode)
    if framerate in drop.valid:
        return drop
    elif framerate in nondrop.valid:
        return nondrop
    else:
        raise Exception(f"{framerate} is not a valid framerate!")


def add(augend: Timecode, addend: Timecode) -> Timecode:
    """ Adds the addend to the augend. Returns the sum. """


def subtract(minuend: Timecode, subtrahend: Timecode) -> Timecode:
    """ Subtracts the subtrahend from the minuend. Returns the difference. """
