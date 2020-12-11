import json

END_CHARACTER = "\0"
MOVE_PATTERN = "{username}> город: {city}"
GAME_BEGIN = "GAME BEGIN! Начальный город: Самара"
GAME_CONTINUE = "GAME CONTINUE! Последний названный город: {city}"
YOUR_MOVE = "Твой ход"
MOVE_AGAIN = "Некорректный ход! Город должен начинаться на букву {letter} и существовать в реальности"
NICHYA = "Ничья!"
FAIL_PATTERN = "{username} проиграл!"
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
