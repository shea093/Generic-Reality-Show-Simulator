import os
import sys

from contestant import Contestant
from episode import Episode
import random


def blockPrinting(func):
    def func_wrapper(*args, **kwargs):
        # block all printing to the console
        sys.stdout = open(os.devnull, 'w')
        # call the method in question
        value = func(*args, **kwargs)
        # enable all printing to the console
        sys.stdout = sys.__stdout__
        # pass the return value of the method back
        return value

    return func_wrapper

class Simulator:

    def __init__(self, seed: int, contestant_list: list[Contestant]):
        self.__global_rng_seed = seed
        self.__seed_increment = random.Random(self.__global_rng_seed).randint(1,100)
        self.__contestants = contestant_list
        self.__elimination_order = []


    def get_highs(self, ep: Episode):
        output = ""
        for high in ep.highs:
            output = output + high + ", "
        return output

    def get_highs_random(self, ep: Episode, str_get = True):
        output_list = []
        for high in ep.highs:
            output_list.append(high)
        output_list.append(ep.winner)
        self.__seed_increment = self.__seed_increment + 1
        random.Random(self.__global_rng_seed+self.__seed_increment).shuffle(output_list)

        output = ""
        for high in output_list:
            output = output + high + ", "

        if str_get == True:
            return output
        else:
            return output_list


    def get_lows_random(self, ep: Episode, str_get = True):
        output_list = []
        for low in ep.btm:
            output_list.append(low)
        if len(ep.lows) >= 1:
            for low in ep.lows:
                output_list.append(low)
        self.__seed_increment = self.__seed_increment + 1
        random.Random(self.__global_rng_seed+self.__seed_increment).shuffle(output_list)

        output = ""
        for low in output_list:
            output = output + low + ", "

        if str_get == True:
            return output
        else:
            return output_list

    def get_tops_bottoms(self, top_list: list, btm_list: list):
        self.__seed_increment = self.__seed_increment + 1
        tb_list = top_list + btm_list
        random.Random(self.__global_rng_seed+self.__seed_increment).shuffle(tb_list)
        output_str = ""
        for n in tb_list:
            output_str = output_str + n + ", "
        return output_str




    def get_btm(self, ep: Episode):
        output = ""
        for btm in ep.btm:
            output = output + btm + ", "
        return output

    def get_safes(self, ep: Episode):
        output = ""
        for safe in ep.safes:
            output = output + safe + ", "
        return output

    def print_contestants(self):
        for contestant in self.__contestants:
            print(contestant.contestant_name)



    @blockPrinting
    def simulate_a_week(self, week_number: int, this_weeks_contestants: list[Contestant], pause = False, non_elims = 0):
        if len(this_weeks_contestants) == 2:
            print("----------------------------")
            print(this_weeks_contestants[0].contestant_name+" score: "+str(this_weeks_contestants[0].score))
            print(this_weeks_contestants[1].contestant_name + " score: " + str(this_weeks_contestants[1].score))
            if this_weeks_contestants[0].score_average > this_weeks_contestants[1].score_average:
                elim_person = [this_weeks_contestants[1].contestant_name, this_weeks_contestants[1].wins, this_weeks_contestants[1].highs,
                               round(this_weeks_contestants[1].score_average,2), this_weeks_contestants[1]]
                self.__elimination_order.append(elim_person)
                elim_person = [this_weeks_contestants[0].contestant_name, this_weeks_contestants[0].wins, this_weeks_contestants[0].highs,
                               round(this_weeks_contestants[0].score_average,2),this_weeks_contestants[0]]
                self.__elimination_order.append(elim_person)
            else:
                elim_person = [this_weeks_contestants[0].contestant_name, this_weeks_contestants[0].wins, this_weeks_contestants[0].highs,
                               round(this_weeks_contestants[0].score_average,2), this_weeks_contestants[0]]
                self.__elimination_order.append(elim_person)
                elim_person = [this_weeks_contestants[1].contestant_name, this_weeks_contestants[1].wins, this_weeks_contestants[1].highs,
                               round(this_weeks_contestants[1].score_average,2), this_weeks_contestants[1]]
                self.__elimination_order.append(elim_person)
            print("----------------------------")
            return "Finale"
        this_episode = Episode(week_number=week_number, contestants=this_weeks_contestants, rng_seed=self.__global_rng_seed+week_number)
        #print(getattr(this_episode, 'contestant_weekly_scores'))
        print("----------------------------")
        print("Episode" + str(week_number))

        if len(this_episode.safes) >= 1:
            print("Safes: " + self.get_safes(this_episode)[0:len(self.get_safes(this_episode)) - 2])
        if pause == True:
            input("...")

        topbtm_string = self.get_tops_bottoms(self.get_highs_random(this_episode, str_get=False), self.get_lows_random(this_episode, str_get=False))
        topbtm_string = topbtm_string[0:len(topbtm_string)-2] + "."

        print("The tops and bottoms are " + topbtm_string)
        print("")
        if pause == True:
            input("...")

        high_string = self.get_highs_random(this_episode)
        high_string = high_string[0:len(high_string)-2] + "."
        low_string = self.get_lows_random(this_episode)
        low_string = low_string[0:len(low_string)-2] + "."

        print("IN THE TOP is: " + high_string)
        print("IN THE BTM is: " + low_string)

        if pause == True:
            input("...")

        print("Winner: " + this_episode.winner)
        if pause == True:
            input("...")



        if len(this_episode.lows) >= 1:
            print("Low: " + this_episode.lows[0])
        if pause == True:
            input("...")

        if len(this_episode.btm) >= 1:
            print("Btm: " + self.get_btm(this_episode)[0:len(self.get_btm(this_episode)) - 2])
        if pause == True:
            input("...")

        if week_number <= non_elims:
            pass
        else:
            print("Eliminated: " + this_episode.eliminated.contestant_name)
            elim_person = [this_episode.eliminated.contestant_name,this_episode.eliminated.wins,this_episode.eliminated.highs,
                       round(this_episode.eliminated.score_average,2),this_episode.eliminated]
            self.__elimination_order.append(elim_person)
        next_week_pool = this_episode.next_week_contestants
        if pause == True:
            input("...")
        return next_week_pool

    def simulate_season(self):
        weekly_contestant_pool = self.__contestants.copy()

        for i in range (1,16):
            if weekly_contestant_pool == "Finale":
                pass
            else:
                next_week = self.simulate_a_week(i,weekly_contestant_pool,pause=False,non_elims=3)
                weekly_contestant_pool = next_week

        self.__elimination_order.reverse()
        # for index, elim in enumerate(self.__elimination_order):
        #     print(elim[0],"\t",elim[3],"\t","WINS: ",elim[4].wins,"\t","HIGHS: ",elim[4].highs,"\t","BTMS: ",elim[4].btms,"LOWS: ",elim[4].lows)
        test = ""

    @property
    def elimination_order(self):
        return self.__elimination_order

    def __repr__(self):
        return "<" + "Seed: " + str(self.__global_rng_seed) + ", Winner: " + self.__elimination_order[0][0] + ">"
