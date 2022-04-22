from contestant import Contestant
from episode import Episode
import random

global_rng_seed = 399576543
simulator_seed_increment = 0
contestants = []

def make_contestants():
    contestants.append(Contestant(contestant_id=1,contestant_name="Jennifer Hudson",
                                  star_power=85,whatnottosing=63,sympathy=5,comedy=60))
    contestants.append(Contestant(contestant_id=2, contestant_name="Katharine McPhee",
                                  star_power=65, whatnottosing=55, sympathy=2, comedy=4))
    contestants.append(Contestant(contestant_id=3, contestant_name="Paris Bennett",
                                  star_power=41, whatnottosing=58, sympathy=20, comedy=6))
    contestants.append(Contestant(contestant_id=4, contestant_name="Melinda Doolittle",
                                  star_power=56, whatnottosing=77, sympathy=44, comedy=21))
    contestants.append(Contestant(contestant_id=5, contestant_name="Kimberley Locke",
                                  star_power=36, whatnottosing=64, sympathy=15, comedy=51))
    contestants.append(Contestant(contestant_id=6, contestant_name="Christina Christian",
                                  star_power=37, whatnottosing=55, sympathy=22, comedy=5))
    contestants.append(Contestant(contestant_id=7, contestant_name="David Archuleta",
                                  star_power=64, whatnottosing=57, sympathy=45, comedy=6))
    contestants.append(Contestant(contestant_id=8, contestant_name="Sanjaya Malakar",
                                  star_power=15, whatnottosing=19, sympathy=50, comedy=50))
    contestants.append(Contestant(contestant_id=9, contestant_name="George Huff",
                                  star_power=32, whatnottosing=58, sympathy=33, comedy=58))
    contestants.append(Contestant(contestant_id=10, contestant_name="Jon Peter Lewis",
                                  star_power=35, whatnottosing=34, sympathy=37, comedy=56))
    contestants.append(Contestant(contestant_id=11, contestant_name="Bo Bice",
                                  star_power=44, whatnottosing=71, sympathy=4, comedy=11))
    contestants.append(Contestant(contestant_id=12, contestant_name="Constantine Maroulis",
                                  star_power=37, whatnottosing=52, sympathy=4, comedy=11))
    contestants.append(Contestant(contestant_id=13, contestant_name="Siobhan Magnus",
                                  star_power=36, whatnottosing=62, sympathy=11, comedy=36))
    contestants.append(Contestant(contestant_id=14, contestant_name="Rickey Smith",
                                  star_power=12, whatnottosing=39.8, sympathy=33, comedy=45))

def get_highs(ep: Episode):
    output = ""
    for high in ep.highs:
        output = output + high + ", "
    return output

def get_btm(ep: Episode):
    output = ""
    for btm in ep.btm:
        output = output + btm + ", "
    return output

def get_safes(ep: Episode):
    output = ""
    for safe in ep.safes:
        output = output + safe + ", "
    return output

make_contestants()
elimination_order = []


def simulate_a_week(week_number: int, this_weeks_contestants: list[Contestant]):
    if len(this_weeks_contestants) == 2:
        print("----------------------------")
        print(this_weeks_contestants[0].contestant_name+" score: "+str(this_weeks_contestants[0].score_average))
        print(this_weeks_contestants[1].contestant_name + " score: " + str(this_weeks_contestants[1].score_average))
        if this_weeks_contestants[0].score_average > this_weeks_contestants[1].score_average:
            elim_person = [this_weeks_contestants[1].contestant_name, this_weeks_contestants[1].wins, this_weeks_contestants[1].highs]
            elimination_order.append(elim_person)
            elim_person = [this_weeks_contestants[0].contestant_name, this_weeks_contestants[0].wins, this_weeks_contestants[0].highs]
            elimination_order.append(elim_person)
        else:
            elim_person = [this_weeks_contestants[0].contestant_name, this_weeks_contestants[0].wins, this_weeks_contestants[0].highs]
            elimination_order.append(elim_person)
            elim_person = [this_weeks_contestants[1].contestant_name, this_weeks_contestants[1].wins, this_weeks_contestants[1].highs]
            elimination_order.append(elim_person)
        print("----------------------------")
        return "Finale"
    this_episode = Episode(week_number=week_number, contestants=this_weeks_contestants, rng_seed=global_rng_seed+week_number)
    print(getattr(this_episode, 'contestant_weekly_scores'))
    print("----------------------------")
    print("Episode" + str(week_number))
    print("Winner: " + this_episode.winner)
    if len(this_episode.highs) >= 1:
        print("Highs: " + get_highs(this_episode)[0:len(get_highs(this_episode)) - 2])
    if len(this_episode.safes) >= 1:
        print("Safes: " + get_safes(this_episode)[0:len(get_safes(this_episode)) - 2])
    if len(this_episode.lows) >= 1:
        print("Low: " + this_episode.lows[0])
    if len(this_episode.btm) >= 1:
        print("Btm: " + get_btm(this_episode)[0:len(get_btm(this_episode)) - 2])
    print("Eliminated: " + this_episode.eliminated.contestant_name)
    elim_person = [this_episode.eliminated.contestant_name,this_episode.eliminated.wins,this_episode.eliminated.highs]
    elimination_order.append(elim_person)
    next_week_pool = this_episode.next_week_contestants
    return next_week_pool

weekly_contestant_pool = contestants.copy()

for i in range (1,14):
    if weekly_contestant_pool == "Finale":
        pass
    else:
        next_week = simulate_a_week(i,weekly_contestant_pool)
        weekly_contestant_pool = next_week

elimination_order.reverse()
for index, elim in enumerate(elimination_order):
    print(elim)
test = ""
