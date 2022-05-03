import enum


class GameStatus(enum.Enum):
    NOT_STARTED = 1
    ACTIVE = 2
    PAUSED = 3
    ENDED = 4
    EXITED = 5
