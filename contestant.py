import random


class Contestant:
    def __init__(self, contestant_id: int, contestant_name: str, star_power=0,
                 whatnottosing=0, sympathy=0, comedy=0, stats_values=None, prep=0, rigor_range=30):
        self.__contestant_id = contestant_id
        self.__contestant_name = contestant_name
        self.__star_power = star_power
        self.__whatnottosing_score = whatnottosing
        self.__sympathy = sympathy
        self.__comedy = comedy
        self.__wins = 0
        self.__highs = 0
        self.__lows = 0
        self.__safes = 0
        self.__btms = 0
        self.__score = 0.0
        self.__ep_count = 0
        self.__score_average = 0.0
        self.__eliminated_flag = False
        self.__placement = 0
        self.__overly_safe_flag = False
        self.__score_floor = 1
        self.__score_ceiling = 100
        self.__ceiling_steam_change = False
        self.__stats = {'Strength': 0, 'Speed': 0, 'Luck': 0, 'Fashion': 0, 'Love': 0, 'Beauty': 0, 'Leadership': 0,
                        'Composure': 0, 'Teamwork': 0, 'Theatrics': 0,
                        'Devotion': 0, 'Political Drive': 0, 'Humor': 0, 'Craftsmanship': 0, 'Intelligence': 0}
        self.__seasonal_preparation = prep
        self.__rigor_morris = 0
        if prep != 0:
            self.__score_floor = prep
            self.__rigor_morris = random.Random(prep * len(self.__contestant_name) + int(contestant_id)).randint(-abs(rigor_range), rigor_range)
            if self.__rigor_morris < 0:
                self.__rigor_morris = 0
        if isinstance(stats_values, dict):
            self.__stats = stats_values

    @property
    def placement(self):
        return self.__placement

    @property
    def rigor_morris(self):
        return self.__rigor_morris

    @property
    def seasonal_preparation(self):
        return self.__seasonal_preparation

    @property
    def contestant_id(self):
        return self.__contestant_id

    @property
    def contestant_name(self):
        return self.__contestant_name

    @property
    def star_power(self):
        return self.__star_power

    @star_power.setter
    def star_power(self, value: int):
        self.__star_power = value

    @property
    def stats(self):
        return self.__stats

    @stats.setter
    def stats(self, value: dict):
        self.__stats = value

    @property
    def ceiling_steam_change(self):
        return self.__ceiling_steam_change

    @ceiling_steam_change.setter
    def ceiling_steam_change(self, value: bool):
        self.__ceiling_steam_change = value

    @property
    def score_floor(self):
        return self.__score_floor

    @score_floor.setter
    def score_floor(self, value: int):
        self.__score_floor = value

    @property
    def score_ceiling(self):
        return self.__score_ceiling

    @score_ceiling.setter
    def score_ceiling(self, value: int):
        self.__score_ceiling = value

    @property
    def overly_safe_flag(self):
        return self.__overly_safe_flag

    @overly_safe_flag.setter
    def overly_safe_flag(self, value: bool):
        self.__overly_safe_flag = value

    @property
    def whatnottosing_score(self):
        return self.__whatnottosing_score

    @whatnottosing_score.setter
    def whatnottosing_score(self, value: int):
        self.__whatnottosing_score = value

    @property
    def sympathy(self):
        return self.__sympathy

    @sympathy.setter
    def sympathy(self, value: int):
        self.__sympathy = value

    @property
    def comedy(self):
        return self.__comedy

    @comedy.setter
    def comedy(self, value: int):
        self.__comedy = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value: float):
        self.__score = value
        self.__score_average = self.__score / self.__ep_count

    @property
    def ep_count(self):
        return self.__ep_count

    @ep_count.setter
    def ep_count(self, value: int):
        self.__ep_count = value

    @property
    def wins(self):
        return self.__wins

    @wins.setter
    def wins(self, value: int):
        self.__wins = value

    @property
    def highs(self):
        return self.__highs

    @highs.setter
    def highs(self, value: int):
        self.__highs = value

    @property
    def lows(self):
        return self.__lows

    @lows.setter
    def lows(self, value: int):
        self.__lows = value

    @property
    def btms(self):
        return self.__btms

    @btms.setter
    def btms(self, value: int):
        self.__btms = value

    @property
    def safes(self):
        return self.__safes

    @safes.setter
    def safes(self, value: int):
        self.__safes = value

    @property
    def score_average(self):
        return self.__score_average

    @score_average.setter
    def score_average(self, value: float):
        self.__score_average = value

    @property
    def eliminated_flag(self):
        return self.__eliminated_flag

    @eliminated_flag.setter
    def eliminated_flag(self, value: bool):
        self.__eliminated_flag = value

    def __repr__(self):
        output = "<Name: " + self.__contestant_name + ">"
        return output
