import json

END_CHARACTER = "\0"
MOVE_PATTERN = "{username}> city: {city}"
GAME_BEGIN = "GAME BEGIN! Starting city: Samara"
GAME_CONTINUE = "GAME CONTINUE! Last city: {city}"
YOUR_MOVE = "You move"
MOVE_AGAIN = "INCORRECT MOVE! The city must start with a letter: {letter}"
NICHYA = "Nichya!"
FAIL_PATTERN = "{username} fail!"
TARGET_ENCODING = "utf-8"


class Message(object):
    def __init__(self, **kwargs):
        self.username = None
        self.city = None
        self.cities = None
        self.letter = None
        self.game_begin = False
        self.game_continue = False
        self.can_move = False
        self.incorrect_move = False
        self.quit = False
        self.nichya = False
        self.fail = False
        self.__dict__.update(kwargs)

    def __str__(self):
        if self.game_begin:
            return GAME_BEGIN.format(**self.__dict__)
        if self.game_continue:
            return GAME_CONTINUE.format(**self.__dict__)
        if self.can_move:
            return YOUR_MOVE
        if self.nichya:
            return NICHYA
        if self.fail:
            return FAIL_PATTERN.format(**self.__dict__)
        if self.incorrect_move:
            return MOVE_AGAIN.format(**self.__dict__)
        return MOVE_PATTERN.format(**self.__dict__)

    def marshal(self):
        return (json.dumps(self.__dict__) + END_CHARACTER).encode(TARGET_ENCODING)
