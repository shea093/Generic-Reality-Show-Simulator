import random


class EpisodeType:
    def __init__(self, ep_type_val: str, ep_bias_list: list):
        self.ep_type = ep_type_val
        self.__ep_biases = {'Strength': ep_bias_list[0], 'Speed': ep_bias_list[1], 'Luck': ep_bias_list[2],
                            'Fashion': ep_bias_list[3], 'Love': ep_bias_list[4], 'Beauty': ep_bias_list[5],
                            'Leadership': ep_bias_list[6], 'Composure': ep_bias_list[7],
                            'Teamwork': ep_bias_list[8], 'Theatrics': ep_bias_list[9],
                            'Devotion': ep_bias_list[10], 'Political Drive': ep_bias_list[11],
                            'Humor': ep_bias_list[12], 'Craftsmanship': ep_bias_list[13],
                            'Intelligence': ep_bias_list[14]}

    @property
    def ep_biases(self):
        return self.__ep_biases

    @ep_biases.setter
    def ep_biases(self, value: dict[float]):
        self.__ep_biases = value

    def __repr__(self):
        return "<" + self.ep_type + ">"


def return_ratios(val_list: list[int]) -> list[float]:
    if len(val_list) != 15:
        raise ValueError
    ratio_list = []
    ep_sum = sum(val_list)
    for val in val_list:
        ratio = float(val / ep_sum)
        ratio_list.append(ratio)
    return ratio_list


def return_ep_types(rng_seed: int) -> list[EpisodeType]:
    """

    :rtype: list[EpisodeType]
    """
    # STR SPD LCK FSH LUV BEU LDR CMP TMW THT DEV POL HUM CRF INT
    # 1    2   3   4   5   6   7   8   9  10  11  12  13  14  15

    ep_type_return_list = []

    # Sewing
    sewing_ep_bias = return_ratios([0, 30, 30, 75, 5, 37, 5,
                                    35, 5, 5, 0, 5, 10, 90, 38])
    sewing_ep = EpisodeType(ep_type_val="sewing", ep_bias_list=sewing_ep_bias)
    ep_type_return_list.append(sewing_ep)

    # Dueling
    dueling_ep_bias = return_ratios([80, 70, 35, 5, -15, 10, 15, 50, 5, 45, 35, 5, 10, 3, 16])
    dueling_ep = EpisodeType(ep_type_val="dueling", ep_bias_list=dueling_ep_bias)
    ep_type_return_list.append(dueling_ep)

    # Musical
    musical_ep_bias = return_ratios([5, 20, 30, 35, 25, 40, 38, 38, 65, 90, 10, 5, 40, 20, 6])
    musical_ep = EpisodeType(ep_type_val="musical", ep_bias_list=musical_ep_bias)
    ep_type_return_list.append(musical_ep)

    # Stand-up
    standup_ep_bias = return_ratios([5, 0, 20, 15, 5, 5, 10, 35, 3, 38, 3, 20, 90, 3, 20])
    standup_ep = EpisodeType(ep_type_val="standup", ep_bias_list=standup_ep_bias)
    ep_type_return_list.append(standup_ep)

    # Cooking
    cooking_ep_bias = return_ratios([8, 15, 35, 3, 60, 8, 10, 35, 18, 15, 10, 0, 2, 75, 23])
    cooking_ep = EpisodeType(ep_type_val="cooking", ep_bias_list=cooking_ep_bias)
    ep_type_return_list.append(cooking_ep)

    # Sprint
    sprint_ep_bias = return_ratios([25, 90, 40, 3, 3, 3, 8, 30, 15, 5, 3, 3, 3, 3, 3])
    sprint_ep = EpisodeType(ep_type_val="sprint", ep_bias_list=sprint_ep_bias)
    ep_type_return_list.append(sprint_ep)

    # Political Debate
    debate_ep_bias = return_ratios([2, 0, 25, 35, 35, 35, 65, 60, 40, 32, 25, 99, 30, 3, 40])
    debate_ep = EpisodeType(ep_type_val="debate", ep_bias_list=debate_ep_bias)
    ep_type_return_list.append(debate_ep)

    # Modeling
    model_ep_bias = return_ratios([8, 8, 20, 68, 5, 80, 10, 39, 25, 34, 3, 10, 10, 19, 2])
    model_ep = EpisodeType(ep_type_val="model", ep_bias_list=model_ep_bias)
    ep_type_return_list.append(model_ep)

    # Healing
    heal_ep_bias = return_ratios([1, 6, 40, 20, 75, 30, 30, 39, 48, 3, 90, 3, 3, 1, 25])
    heal_ep = EpisodeType(ep_type_val="heal", ep_bias_list=heal_ep_bias)
    ep_type_return_list.append(heal_ep)

    # Escape Room
    escape_ep_bias = return_ratios([8, 18, 40, 4, 10, 3, 60, 60, 90, 2, 18, 2, 11, 15, 80])
    escape_ep = EpisodeType(ep_type_val="escape", ep_bias_list=escape_ep_bias)
    ep_type_return_list.append(escape_ep)

    # Random
    r_list = []
    for n in range(0, 15):
        r = random.Random(rng_seed + n).randint(1, 100)
        r_list.append(r)
    random1_ep_bias = return_ratios(r_list)
    random1_ep = EpisodeType(ep_type_val="random1", ep_bias_list=random1_ep_bias)
    ep_type_return_list.append(random1_ep)

    # Random 2
    r_list = []
    for n in range(15, 30):
        r = random.Random(rng_seed + n).randint(1, 100)
        r_list.append(r)
    random2_ep_bias = return_ratios(r_list)
    random2_ep = EpisodeType(ep_type_val="random2", ep_bias_list=random2_ep_bias)
    ep_type_return_list.append(random2_ep)

    # Brawling
    brawl_ep_bias = return_ratios([90, 25, 5, 0, 0, 0, 5, 25, 5, 5, -20, 5, 11, 3, 15])
    brawl_ep = EpisodeType(ep_type_val="brawl", ep_bias_list=brawl_ep_bias)
    ep_type_return_list.append(brawl_ep)

    return ep_type_return_list

