from contestant import Contestant
from episode import Episode
from simulator2 import Simulator
import random
import copy

contestants = []

def make_contestants():
    contestants.append(Contestant(contestant_id=1, contestant_name="G'raha Tia",
                                  star_power=65, whatnottosing=78, sympathy=80, comedy=74))
    contestants.append(Contestant(contestant_id=2, contestant_name="Krile Baldesion",
                                  star_power=51, whatnottosing=72, sympathy=69, comedy=82))
    contestants.append(Contestant(contestant_id=3, contestant_name="Alphinaud Leveilleur",
                                  star_power=45, whatnottosing=85, sympathy=51, comedy=35))
    contestants.append(Contestant(contestant_id=4, contestant_name="Alisaie Leveilleur",
                                  star_power=67, whatnottosing=62, sympathy=11, comedy=78))
    contestants.append(Contestant(contestant_id=5, contestant_name="Y'shtola Rhul",
                                  star_power=62, whatnottosing=72, sympathy=44, comedy=68))
    contestants.append(Contestant(contestant_id=6, contestant_name="Urianger Augurelt",
                                  star_power=41, whatnottosing=82, sympathy=76, comedy=46))
    contestants.append(Contestant(contestant_id=7, contestant_name="Tataru Taru",
                                  star_power=89, whatnottosing=41, sympathy=85, comedy=52))
    contestants.append(Contestant(contestant_id=8, contestant_name="Estinien Wyrmblood",
                                  star_power=38, whatnottosing=39, sympathy=12, comedy=54))
    contestants.append(Contestant(contestant_id=9, contestant_name="Lyse Hext",
                                  star_power=52, whatnottosing=27, sympathy=35, comedy=12))
    contestants.append(Contestant(contestant_id=10, contestant_name="Thancred Waters",
                                  star_power=57, whatnottosing=41, sympathy=40, comedy=27))
    contestants.append(Contestant(contestant_id=11, contestant_name="The Warrior of Light",
                                  star_power=80, whatnottosing=70, sympathy=55, comedy=22))
    contestants.append(Contestant(contestant_id=12, contestant_name="Ryne",
                                  star_power=69, whatnottosing=28, sympathy=91, comedy=12))
    # contestants.append(Contestant(contestant_id=13, contestant_name="Alaina Whitaker",
    #                               star_power=38, whatnottosing=53, sympathy=55, comedy=36))
    # contestants.append(Contestant(contestant_id=14, contestant_name="Danny Gokey",
    #                               star_power=27, whatnottosing=49, sympathy=75, comedy=33))
    # contestants.append(Contestant(contestant_id=14, contestant_name="Tatiana Del Toro",
    #                               star_power=49, whatnottosing=48, sympathy=55, comedy=99))

make_contestants()

simmed_seasons = []

sim_start = random.randint(1,9999999999)

for i in range(sim_start,sim_start+5000):
    sim_season = Simulator(seed=i,contestant_list=contestants)
    sim_season_this = copy.deepcopy(sim_season)
    sim_season_this.simulate_season()
    simmed_seasons.append(sim_season_this)

winner_dict = {}
cumulative_wins = {}

for i in simmed_seasons[0].elimination_order:
    winner_dict[i[4].contestant_name] = 0
    cumulative_wins[i[4].contestant_name] = 0

for i in simmed_seasons:
    current_contestant = i.elimination_order[0][4]
    winner_dict[current_contestant.contestant_name] = winner_dict[current_contestant.contestant_name] + 1
    cumulative_wins[current_contestant.contestant_name] = cumulative_wins[current_contestant.contestant_name] + current_contestant.wins
    print(current_contestant.contestant_name + ", WINS: " + str(current_contestant.wins))

print(winner_dict)
print(cumulative_wins)

print("------------")
print("WINNER COUNT")
for key, value in winner_dict.items():
    print(key + ": \t" + str(value))

print("------------")
print("CUMULATIVE WINS")
for key,value in cumulative_wins.items():
    print(key + ": \t" + str(value))