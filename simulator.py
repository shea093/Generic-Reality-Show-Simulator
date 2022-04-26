from contestant import Contestant
from episode import Episode
import random

#4636
global_rng_seed = 337531144

simulator_seed_increment = 0
contestants = []

def make_contestants():
    contestants.append(Contestant(contestant_id=1,contestant_name="G'raha Tia",
                                  star_power=65,whatnottosing=78,sympathy=80,comedy=74))
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

def get_highs(ep: Episode):
    output = ""
    for high in ep.highs:
        output = output + high + ", "
    return output

def get_highs_random(ep: Episode, str_get = True):
    output_list = []
    for high in ep.highs:
        output_list.append(high)
    output_list.append(ep.winner)
    global simulator_seed_increment
    simulator_seed_increment = simulator_seed_increment + 1
    random.Random(global_rng_seed+simulator_seed_increment).shuffle(output_list)

    output = ""
    for high in output_list:
        output = output + high + ", "

    if str_get == True:
        return output
    else:
        return output_list


def get_lows_random(ep: Episode, str_get = True):
    output_list = []
    for low in ep.btm:
        output_list.append(low)
    if len(ep.lows) >= 1:
        for low in ep.lows:
            output_list.append(low)
    global simulator_seed_increment
    simulator_seed_increment = simulator_seed_increment + 1
    random.Random(global_rng_seed+simulator_seed_increment).shuffle(output_list)

    output = ""
    for low in output_list:
        output = output + low + ", "

    if str_get == True:
        return output
    else:
        return output_list

def get_tops_bottoms(top_list: list, btm_list: list):
    global simulator_seed_increment
    simulator_seed_increment = simulator_seed_increment + 1
    tb_list = top_list + btm_list
    random.Random(global_rng_seed+simulator_seed_increment).shuffle(tb_list)
    output_str = ""
    for n in tb_list:
        output_str = output_str + n + ", "
    return output_str




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
for contestant in contestants:
    print(contestant.contestant_name)
elimination_order = []


def simulate_a_week(week_number: int, this_weeks_contestants: list[Contestant], pause = False, non_elims = 0):
    if len(this_weeks_contestants) == 2:
        print("----------------------------")
        print(this_weeks_contestants[0].contestant_name+" score: "+str(this_weeks_contestants[0].score))
        print(this_weeks_contestants[1].contestant_name + " score: " + str(this_weeks_contestants[1].score))
        if this_weeks_contestants[0].score_average > this_weeks_contestants[1].score_average:
            elim_person = [this_weeks_contestants[1].contestant_name, this_weeks_contestants[1].wins, this_weeks_contestants[1].highs,
                           round(this_weeks_contestants[1].score_average,2)]
            elimination_order.append(elim_person)
            elim_person = [this_weeks_contestants[0].contestant_name, this_weeks_contestants[0].wins, this_weeks_contestants[0].highs,
                           round(this_weeks_contestants[0].score_average,2)]
            elimination_order.append(elim_person)
        else:
            elim_person = [this_weeks_contestants[0].contestant_name, this_weeks_contestants[0].wins, this_weeks_contestants[0].highs,
                           round(this_weeks_contestants[0].score_average,2)]
            elimination_order.append(elim_person)
            elim_person = [this_weeks_contestants[1].contestant_name, this_weeks_contestants[1].wins, this_weeks_contestants[1].highs,
                           round(this_weeks_contestants[1].score_average,2)]
            elimination_order.append(elim_person)
        print("----------------------------")
        return "Finale"
    this_episode = Episode(week_number=week_number, contestants=this_weeks_contestants, rng_seed=global_rng_seed+week_number)
    #print(getattr(this_episode, 'contestant_weekly_scores'))
    print("----------------------------")
    print("Episode" + str(week_number))

    if len(this_episode.safes) >= 1:
        print("Safes: " + get_safes(this_episode)[0:len(get_safes(this_episode)) - 2])
    if pause == True:
        input("...")

    topbtm_string = get_tops_bottoms(get_highs_random(this_episode, str_get=False), get_lows_random(this_episode, str_get=False))
    topbtm_string = topbtm_string[0:len(topbtm_string)-2] + "."

    print("The tops and bottoms are " + topbtm_string)
    print("")
    if pause == True:
        input("...")

    high_string = get_highs_random(this_episode)
    high_string = high_string[0:len(high_string)-2] + "."
    low_string = get_lows_random(this_episode)
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
        print("Btm: " + get_btm(this_episode)[0:len(get_btm(this_episode)) - 2])
    if pause == True:
        input("...")

    if week_number <= non_elims:
        pass
    else:
        print("Eliminated: " + this_episode.eliminated.contestant_name)
        elim_person = [this_episode.eliminated.contestant_name,this_episode.eliminated.wins,this_episode.eliminated.highs,
                   round(this_episode.eliminated.score_average,2)]
        elimination_order.append(elim_person)
    next_week_pool = this_episode.next_week_contestants
    if pause == True:
        input("...")
    return next_week_pool

weekly_contestant_pool = contestants.copy()

for i in range (1,16):
    if weekly_contestant_pool == "Finale":
        pass
    else:
        next_week = simulate_a_week(i,weekly_contestant_pool,pause=True,non_elims=3)
        weekly_contestant_pool = next_week

elimination_order.reverse()
for index, elim in enumerate(elimination_order):
    print(elim,elim[2])
test = ""
