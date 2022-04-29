from contestant import Contestant
from episode import Episode
import random

#4636
global_rng_seed = 665345643543564324453425325553534645243434343554355435543554355435432453535567656575435432443245435543565467547745763546543564554554554355456664363465345345453543543554355345634666666666666666666876546743654353446546


simulator_seed_increment = 0
contestants = []

def make_contestants():
    contestants.append(Contestant(contestant_id=1,contestant_name="Melinda Doolittle",
                                  star_power=87,whatnottosing=77,sympathy=86,comedy=64))
    contestants.append(Contestant(contestant_id=2, contestant_name="George Huff",
                                  star_power=63, whatnottosing=72, sympathy=62, comedy=82))
    contestants.append(Contestant(contestant_id=3, contestant_name="Kelly Clarkson",
                                  star_power=91, whatnottosing=76, sympathy=68, comedy=95))
    contestants.append(Contestant(contestant_id=4, contestant_name="Jordin Sparks",
                                  star_power=78, whatnottosing=58, sympathy=66, comedy=26))
    contestants.append(Contestant(contestant_id=5, contestant_name="Danny Noriega",
                                  star_power=69, whatnottosing=34, sympathy=50, comedy=93))
    contestants.append(Contestant(contestant_id=6, contestant_name="Phil Stacey",
                                  star_power=57, whatnottosing=52, sympathy=76, comedy=35))
    contestants.append(Contestant(contestant_id=7, contestant_name="Nadia Turner",
                                  star_power=86, whatnottosing=65, sympathy=65, comedy=42))
    contestants.append(Contestant(contestant_id=8, contestant_name="Trenyce",
                                  star_power=60, whatnottosing=65, sympathy=55, comedy=44))
    contestants.append(Contestant(contestant_id=9, contestant_name="LaKisha Jones",
                                  star_power=66, whatnottosing=56, sympathy=76, comedy=12))
    contestants.append(Contestant(contestant_id=10, contestant_name="Kellie Pickler",
                                  star_power=64, whatnottosing=34, sympathy=63, comedy=90))
    contestants.append(Contestant(contestant_id=11, contestant_name="Anthony Federov",
                                  star_power=70, whatnottosing=40, sympathy=75, comedy=12))
    contestants.append(Contestant(contestant_id=12, contestant_name="Alaina Whittaker",
                                  star_power=58, whatnottosing=53, sympathy=61, comedy=7))
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
                           round(this_weeks_contestants[1].score_average,2), this_weeks_contestants[1]]
            elimination_order.append(elim_person)
            elim_person = [this_weeks_contestants[0].contestant_name, this_weeks_contestants[0].wins, this_weeks_contestants[0].highs,
                           round(this_weeks_contestants[0].score_average,2),this_weeks_contestants[0]]
            elimination_order.append(elim_person)
        else:
            elim_person = [this_weeks_contestants[0].contestant_name, this_weeks_contestants[0].wins, this_weeks_contestants[0].highs,
                           round(this_weeks_contestants[0].score_average,2), this_weeks_contestants[0]]
            elimination_order.append(elim_person)
            elim_person = [this_weeks_contestants[1].contestant_name, this_weeks_contestants[1].wins, this_weeks_contestants[1].highs,
                           round(this_weeks_contestants[1].score_average,2), this_weeks_contestants[1]]
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
                   round(this_episode.eliminated.score_average,2),this_episode.eliminated]
        elimination_order.append(elim_person)
    next_week_pool = this_episode.next_week_contestants
    if pause == True:
        input("...")
    return next_week_pool

def simulate_season():
    weekly_contestant_pool = contestants.copy()

    for i in range (1,16):
        if weekly_contestant_pool == "Finale":
            pass
        else:
            next_week = simulate_a_week(i,weekly_contestant_pool,pause=False,non_elims=3)
            weekly_contestant_pool = next_week

    elimination_order.reverse()
    for index, elim in enumerate(elimination_order):
        print(elim[0],"\t",elim[3],"\t","WINS: ",elim[4].wins,"\t","HIGHS: ",elim[4].highs,"\t","BTMS: ",elim[4].btms,"LOWS: ",elim[4].lows)
    test = ""

simulate_season()