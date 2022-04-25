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

        star_power_bias = 0.05
        score_bias = 0.16
        whatnottosing_bias = 0.22
        sympathy_bias = 0.03
        comedy_bias = 0.03
        random_bias = 0.51

        if self.__week_number <= 2:
            star_power_bias = 0.14
            score_bias = 0.13
            whatnottosing_bias = 0.28
            sympathy_bias = 0.03
            comedy_bias = 0.03
            random_bias = 0.39

        if self.__week_number >= 8:
            star_power_bias = 0.04
            score_bias = 0.46
            whatnottosing_bias = 0.03
            sympathy_bias = 0.03
            comedy_bias = 0.01
            random_bias = 0.45

        if self.__contestant_number <= 5:
            star_power_bias = 0.04
            score_bias = 0.56
            whatnottosing_bias = 0.03
            sympathy_bias = 0.03
            comedy_bias = 0.01
            random_bias = 0.35

        if self.__contestant_number == 3:
            star_power_bias = 0.02
            score_bias = 0.8
            whatnottosing_bias = 0.03
            sympathy_bias = 0.02
            comedy_bias = 0.02
            random_bias = 0.11


        random.Random(rng_seed).shuffle(contestants)
        seed_increment = 1000

        for contestant in contestants:
            seed_increment = seed_increment + 1000
            contestant_weekly_score = []    #Index 0 = Contestant Object; Index 1 = Contestant Score
            star_power_share = contestant.star_power * star_power_bias
            whatnottosing_share = contestant.whatnottosing_score * whatnottosing_bias
            sympathy_share = contestant.sympathy * sympathy_bias
            comedy_share = contestant.comedy * comedy_bias
            rng_score = random.Random(rng_seed+seed_increment).randint(1,100)
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
            contestant_score = contestant_score
            seed_increment = seed_increment + 1000
            chance_of_showstopper = ((random.Random(rng_seed+seed_increment).randint(1,100) * 0.75) + (contestant.star_power*0.15) + (contestant_score * 0.1)) /5
            if chance_of_showstopper > 14:
                contestant_score = contestant_score + 20
            if contestant_score > 100:
                contestant_score = 100
            if contestant.btms >= 2:
                contestant_score = contestant_score * 0.7
            if contestant.btms >= 3:
                contestant_score = contestant_score - 20
            if (contestant.highs + contestant.wins) <= 3 and self.__week_number > 7:
                contestant_score = contestant_score - 10
            if (contestant.highs + contestant.wins) <= 3 and self.__week_number > 8:
                contestant_score = contestant_score - 10
            if (contestant.wins) >= 3 and self.__week_number >= 9:
                contestant_score = contestant_score * 0.7
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
            seed_increment = seed_increment + 100
            losing_steam_chance = random.Random(rng_seed + seed_increment).randint(1, 100)
            seed_increment = seed_increment + 100
            if week_number == 1:
                if contestant.contestant_name == self.__winner:
                    contestant.score = contestant.score + 24
            if contestant.wins >= 2 and contestant.contestant_name == self.__winner and self.__contestant_number >2:
                seed_increment = seed_increment + 250
                chance = random.Random(rng_seed+seed_increment).randint(1,100)
                seed_increment = seed_increment + 250
                if chance > 30:
                    if self.__contestant_weekly_scores[1][0].wins >=2  and self.__contestant_number >4:
                        self.__contestant_weekly_scores[0][0], self.__contestant_weekly_scores[2][0] = self.__contestant_weekly_scores[2][0], self.__contestant_weekly_scores[0][0]
                    else:
                        self.__contestant_weekly_scores[0][0], self.__contestant_weekly_scores[1][0] = self.__contestant_weekly_scores[1][0], self.__contestant_weekly_scores[0][0]
                        self.__winner = self.__contestant_weekly_scores[0][0].contestant_name
                        test = self.__winner
                        test = ""
            if contestant.wins >= 3 and contestant.contestant_name == self.__winner and self.__contestant_number > 2:
                seed_increment = seed_increment + 250
                chance = random.Random(rng_seed + seed_increment).randint(1, 100)
                seed_increment = seed_increment + 250
                if chance > 20:
                    if self.__contestant_weekly_scores[1][0].wins >=3  and self.__contestant_number >4:
                        self.__contestant_weekly_scores[0][0], self.__contestant_weekly_scores[2][0] = self.__contestant_weekly_scores[2][0], self.__contestant_weekly_scores[0][0]
                    else:
                        self.__contestant_weekly_scores[0][0], self.__contestant_weekly_scores[1][0] = self.__contestant_weekly_scores[1][0], self.__contestant_weekly_scores[0][0]
                        self.__winner = self.__contestant_weekly_scores[0][0].contestant_name
                        test = self.__winner
                        test = ""
            if (contestant.wins) >= 3 and self.__week_number >= 8 and losing_steam_chance > 35:
                contestant.score = contestant.score - 35
            seed_increment = seed_increment + 100
            losing_steam_chance = random.Random(rng_seed + seed_increment).randint(1, 100)
            seed_increment = seed_increment + 100
            if (contestant.wins + contestant.highs) > 6 and self.__week_number >= 7 and losing_steam_chance > 35:
                contestant.score = contestant.score / 0.80
            if (contestant.wins + contestant.highs) >= 4 and self.__week_number < 7 and losing_steam_chance > 25:
                contestant.score = contestant.score / 0.85
            if contestant.safes > 3 and week_number <= 7 and contestant.overly_safe_flag == False:
                contestant.overly_safe_flag = True
                seed_increment = seed_increment + 350
                safe_change = random.Random(rng_seed + seed_increment).randint(-30, 15)
                contestant.score = contestant.score + safe_change
                if safe_change > 5:
                    contestant.score = contestant.score * 1.25
                if safe_change < -20:
                    contestant.score = contestant.score * 0.8




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
                contestant.score = contestant.score + 25
                self.__next_week_contestants.append(contestant)
            elif contestant.contestant_name in self.__highs:
                self.__non_safe_contestants.append(contestant.contestant_name)
                contestant.highs = contestant.highs + 1
                contestant.score = contestant.score + 16
                if self.__week_number <=3:
                    contestant.score = contestant.score + 13
                self.__next_week_contestants.append(contestant)
            elif contestant.contestant_name in self.__lows:
                self.__non_safe_contestants.append(contestant.contestant_name)
                contestant.lows = contestant.lows + 1
                contestant.score = contestant.score -7
                if self.__week_number <=3:
                    contestant.score = contestant.score + -7
                self.__next_week_contestants.append(contestant)
            elif contestant.contestant_name in self.__btm:
                self.__non_safe_contestants.append(contestant.contestant_name)
                contestant.btms = contestant.btms + 1
                contestant.score = contestant.score - 15
                if self.__week_number <=3:
                    contestant.score = contestant.score + -9
                if contestant.contestant_name != self.__eliminated.contestant_name:
                    self.__next_week_contestants.append(contestant)
                else:
                    contestant.eliminated_flag = True
            #safe
            else:
                self.__safes.append(contestant.contestant_name)
                contestant.safes = contestant.safes + 1
                contestant.score = contestant.score - 3
                if self.__week_number <= 4:
                    contestant.score = contestant.score - 5
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





