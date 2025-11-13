from dataclasses import dataclass
from enum import Enum
from typing import Optional

from .framerate import Framerate
from .timecode import Timecode, subtract, timecode


# NOTE: These should be part of the CueTrack app, not this library.
# class CueType(Enum):
#     SCORE = "Score"
#     SONG = "Song"
#     SOURCE = "Source"


# NOTE: These should be part of the CueTrack app, not this library.
# class CueStatus(Enum):
#     TO_DO = "To Do"
#     IN_PROGRESS = "In Progress"
#     NEEDS_REVISIONS = "Needs Revisions"
#     CANCELLED = "Cancelled"
#     MERGED = "Merged" # merged with?
#     APPROVED = "Approved"


class Cue:
    """
    Defines a single piece of music in a Project.
    Required: framerate, and start and/or end time.
    If duration is supplied, and either start or end aren't, then the missing value is automatically calculated.
    """
    def __init__(self, framerate: Framerate|None, start: Optional[str|Timecode],
                 end: Optional[str|Timecode], duration: Optional[str|Timecode],
                 name: str|None=None, number: str|None=None):
        self.number: str = number
        self._name: Optional[str]
        self._framerate: Framerate
        self._start: Timecode
        self._end: Timecode
        self._duration: Timecode

        # Defaults
        if name is not None:
            self.name = name
        if framerate is not None:
            self.framerate = framerate
        if start is not None:
            self.start = start
        if end is not None:
            self.end = end

    @property
    def name(self) -> str:
        if self._name is not None:
            return self._name
        else:
            return ""

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def framerate(self) -> Framerate:
        return self._framerate

    @framerate.setter
    def framerate(self, value: Framerate) -> None:
        self._framerate = value

    @property
    def start(self) -> Timecode:
        return self._start

    @start.setter
    def start(self, value: str|Timecode) -> None:
        if isinstance(value, Timecode):
            self._start = value
        else:
            self._start = timecode(framerate=self.framerate, timecode=value)

    @property
    def end(self) -> Timecode:
        return self._end

    @end.setter
    def end(self, value: str|Timecode) -> None:
        if isinstance(value, Timecode):
            self._end = value
        else:
            self._end = timecode(framerate=self.framerate, timecode=value)

    @property
    def duration(self) -> Timecode:
        if self._duration is None:
            self._duration = subtract(self.end, self.start)
        return self._duration

    @duration.setter
    def duration(self, value: Timecode, adjust_start: bool=False) -> None:
        """ Sets the new duration of the Cue by adjusting either its start or end time (default: start). """

    def override_framerate(self):
        """ Sets a framerate different from the parent Project's framerate. """