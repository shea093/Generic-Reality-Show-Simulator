from contestant import Contestant
from episode import Episode
from simulator2 import Simulator
import random
import copy

contestants = []
glob_seed = 255

def make_contestants():
    contestant_name_and_stat_list = []
    with open ("Config/contestant_stats",'r') as f:
        for line in f.readlines():
            if len(line) < 5:
                pass
            else:
                num_for_seed = 0
                line_edit = line.strip()
                line_split = line_edit.split("\t")
                for i, obj in enumerate(line_split):
                    if i == 0:
                        pass
                    else:
                        line_split[i] = int(line_split[i])
                        num_for_seed += int(line_split[i])
                line_split.append(random.Random(glob_seed+num_for_seed).randint(1, 9999999))
                contestant_name_and_stat_list.append(line_split)

    test = ""
    for n, contestant_info in enumerate(contestant_name_and_stat_list):
        contestant_name_val = contestant_info[0]

        #RNG on contestant stats
        stat_rngize = (glob_seed * 24 * len(contestant_info[0])) - 200
        for ind, stat in enumerate(contestant_info[1:],1):
            rng_percent = 0.15
            stat_percent = (100 - rng_percent) / 100
            rng_ratio = rng_percent * random.Random(stat_rngize).randint(1,100)
            stat_ratio = stat_percent * stat
            contestant_info[ind] = round(rng_ratio + stat_ratio)

        contestant_stats = {'Strength': contestant_info[1], 'Speed': contestant_info[2], 'Luck': contestant_info[3],
                            'Fashion': contestant_info[4], 'Love': contestant_info[5], 'Beauty': contestant_info[6],
                            'Leadership': contestant_info[7], 'Composure': contestant_info[8], 'Teamwork': contestant_info[9],
                            'Theatrics': contestant_info[10], 'Devotion': contestant_info[11], 'Political Drive': contestant_info[12],
                            'Humor': contestant_info[13], 'Craftsmanship': contestant_info[14], 'Intelligence': contestant_info[15]}
        #RNG Values
        prep_range = 10
        rigor_range = 5
        prep_val = random.Random(contestant_info[16]).randint(-abs(prep_range), prep_range)
        contestants.append(Contestant(contestant_id=n,contestant_name=contestant_name_val,star_power=50,whatnottosing=50,sympathy=50,
                                      comedy=50,stats_values=contestant_stats,prep=prep_val,rigor_range=rigor_range))


make_contestants()
sim_season = Simulator(seed=glob_seed, contestant_list=contestants, pause_bool=False)
sim_season.simulate_season()
sim_season.elim_ending()
