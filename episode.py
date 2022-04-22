from contestant import Contestant
import random

class Episode:
    def __init__(self, week_number: int, contestants: list[Contestant], rng_seed: int):
        self.__week_number = week_number
        self.__contestants = contestants
        self.__contestant_number = len(contestants)
        self.__rng_seed = rng_seed
        self.__high_count = 2   #Default
        self.__btm_count = 2    #Default
        self.__low_count = 1


        if self.__contestant_number >= 11:
            self.__high_count = 3
            self.__btm_count = 3

        if self.__contestant_number <= 6:
            self.__high_count = 1

        if self.__contestant_number <= 5:
            self.__low_count = 0

        if self.__contestant_number == 3:
            self.__high_count = 0
            self.__btm_count = 1



        self.__contestant_weekly_scores = []

        star_power_bias = 0.08
        score_bias = 0.21
        whatnottosing_bias = 0.12
        sympathy_bias = 0.03
        comedy_bias = 0.03
        random_bias = 0.53

        if self.__week_number >= 8:
            star_power_bias = 0.06
            score_bias = 0.6
            whatnottosing_bias = 0.03
            sympathy_bias = 0.03
            comedy_bias = 0.03
            random_bias = 0.25

        random.Random(rng_seed).shuffle(contestants)
        seed_increment = 1000

        for contestant in contestants:
            seed_increment = seed_increment + 1000
            contestant_weekly_score = []    #Index 0 = Contestant Object; Index 1 = Contestant Score
            star_power_share = contestant.star_power * star_power_bias
            whatnottosing_share = contestant.whatnottosing_score * whatnottosing_bias
            sympathy_share = contestant.sympathy * sympathy_bias
            comedy_share = contestant.comedy * comedy_bias
            rng_score = random.Random(rng_seed+seed_increment).randint(-50,50)
            seed_increment = seed_increment + 1000
            random_share = rng_score * random_bias
            score_share = (contestant.score_average) * score_bias
            if self.__week_number <= 4:
                half1 = random.Random(rng_seed+seed_increment).randint(-25,25) * 0.5
                seed_increment = seed_increment + 1000
                half2 = (contestant.score_average * score_bias) * 0.5
                if self.__week_number == 1 or self.__week_number == 2:
                    half2 = (contestant.whatnottosing_score * score_bias) * 0.5
                score_share = (half1+half2) * score_bias
            contestant_score = (star_power_share + whatnottosing_share + sympathy_share +
                                comedy_share + random_share + score_share)
            contestant_score = round(contestant_score,2)
            contestant_score = contestant_score + 20
            contestant_weekly_score.append(contestant)
            contestant_weekly_score.append(contestant_score)
            self.__contestant_weekly_scores.append(contestant_weekly_score)
            contestant.ep_count = contestant.ep_count + 1
            contestant.score = contestant.score + contestant_score

        self.__contestant_weekly_scores.sort(reverse=True,key=lambda x: x[1])
        self.__non_safe_contestants = []




        self.__winner = self.__contestant_weekly_scores[0][0].contestant_name
        self.__winner_score = self.__contestant_weekly_scores[0][1]


        #Attempt to prevent too many wins
        for contestant in contestants:
            if week_number == 1:
                if contestant.contestant_name == self.__winner:
                    contestant.score = contestant.score + 12.5
            if contestant.wins >= 4 and contestant.contestant_name == self.__winner:
                seed_increment = seed_increment + 250
                chance = random.Random(rng_seed+seed_increment).randint(1,100)
                seed_increment = seed_increment + 250
                if chance > 15:
                    self.__contestant_weekly_scores[0][0], self.__contestant_weekly_scores[1][0] = self.__contestant_weekly_scores[1][0], self.__contestant_weekly_scores[0][0]
                    self.__winner = self.__contestant_weekly_scores[0][0].contestant_name
                    test = self.__winner
                    test = ""


        #Get more points for winning first week

        self.__highs = []
        self.__btm = []
        self.__lows = []
        self.__safes = []

        if self.__high_count == 0:
            pass
        else:
            for n in range(0,self.__high_count):
                self.__highs.append(self.__contestant_weekly_scores[n+1][0].contestant_name)
        if self.__low_count == 0:
            pass
        else:
            for n in range(0,self.__low_count):
                self.__lows.append(self.__contestant_weekly_scores[self.__contestant_number-self.__btm_count-(n+1)][0].contestant_name)
        for n in range(0,self.__btm_count):
            self.__btm.append(self.__contestant_weekly_scores[self.__contestant_number-n-1][0].contestant_name)
        self.__eliminated = self.__contestant_weekly_scores[self.__contestant_number-1][0]

        self.__next_week_contestants = []

        for contestant in contestants:
            if contestant.contestant_name == self.__winner:
                self.__non_safe_contestants.append(contestant.contestant_name)
                contestant.wins = contestant.wins + 1
                contestant.score = contestant.score + 20
                self.__next_week_contestants.append(contestant)
            elif contestant.contestant_name in self.__highs:
                self.__non_safe_contestants.append(contestant.contestant_name)
                contestant.highs = contestant.highs + 1
                contestant.score = contestant.score + 10
                self.__next_week_contestants.append(contestant)
            elif contestant.contestant_name in self.__lows:
                self.__non_safe_contestants.append(contestant.contestant_name)
                contestant.lows = contestant.lows + 1
                contestant.score = contestant.score - 10
                self.__next_week_contestants.append(contestant)
            elif contestant.contestant_name in self.__btm:
                self.__non_safe_contestants.append(contestant.contestant_name)
                contestant.btms = contestant.btms + 1
                contestant.score = contestant.score - 20
                if contestant.contestant_name != self.__eliminated.contestant_name:
                    self.__next_week_contestants.append(contestant)
                else:
                    contestant.eliminated_flag = True
            else:
                self.__safes.append(contestant.contestant_name)
                contestant.safes = contestant.safes + 1
                self.__next_week_contestants.append(contestant)




    @property
    def contestant_weekly_scores(self):
        return self.__contestant_weekly_scores

    @property
    def next_week_contestants(self):
        return self.__next_week_contestants

    @property
    def highs(self):
        return self.__highs

    @property
    def lows(self):
        return self.__lows

    @property
    def winner(self):
        return self.__winner

    @property
    def safes(self):
        return self.__safes

    @property
    def btm(self):
        return self.__btm

    @property
    def eliminated(self):
        return self.__eliminated





