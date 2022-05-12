from contestant import Contestant
from episode import Episode
from simulator2 import Simulator
import random
import copy

contestants = []

def make_contestants():
    contestants.append(Contestant(contestant_id=1, contestant_name="Ameliance Leveilleur",
                                  star_power=75, whatnottosing=62, sympathy=86, comedy=66))
    contestants.append(Contestant(contestant_id=2, contestant_name="Fourchenalt Leveilleur",
                                  star_power=62, whatnottosing=86, sympathy=2, comedy=2))
    contestants.append(Contestant(contestant_id=3, contestant_name="Dulia Chai",
                                  star_power=77, whatnottosing=52, sympathy=66, comedy=88))
    contestants.append(Contestant(contestant_id=4, contestant_name="Chai-Nuzz",
                                  star_power=66, whatnottosing=79, sympathy=6, comedy=21))
    contestants.append(Contestant(contestant_id=5, contestant_name="Runar",
                                  star_power=41, whatnottosing=34, sympathy=44, comedy=34))
    contestants.append(Contestant(contestant_id=6, contestant_name="Emet Selch",
                                  star_power=66, whatnottosing=97, sympathy=55, comedy=35))
    contestants.append(Contestant(contestant_id=7, contestant_name="Venat",
                                  star_power=98, whatnottosing=81, sympathy=85, comedy=62))
    contestants.append(Contestant(contestant_id=8, contestant_name="Hythlodeus",
                                  star_power=87, whatnottosing=86, sympathy=88, comedy=72))
    contestants.append(Contestant(contestant_id=9, contestant_name="Erenville",
                                  star_power=60, whatnottosing=78, sympathy=15, comedy=32))
    contestants.append(Contestant(contestant_id=10, contestant_name="Raubahn",
                                  star_power=66, whatnottosing=37, sympathy=20, comedy=27))
    contestants.append(Contestant(contestant_id=11, contestant_name="Merlwyb",
                                  star_power=62, whatnottosing=50, sympathy=25, comedy=22))
    contestants.append(Contestant(contestant_id=12, contestant_name="Kan-E-Senna",
                                  star_power=72, whatnottosing=53, sympathy=91, comedy=8))
    # contestants.append(Contestant(contestant_id=13, contestant_name="Alaina Whitaker",
    #                               star_power=38, whatnottosing=53, sympathy=55, comedy=36))
    # contestants.append(Contestant(contestant_id=14, contestant_name="Danny Gokey",
    #                               star_power=27, whatnottosing=49, sympathy=75, comedy=33))
    # contestants.append(Contestant(contestant_id=14, contestant_name="Tatiana Del Toro",
    #                               star_power=49, whatnottosing=48, sympathy=55, comedy=99))

make_contestants()
sim_season = Simulator(seed=907214076503, contestant_list=contestants, pause_bool=False)
sim_season.simulate_season()
test = ""
sim_season.elim_ending()
