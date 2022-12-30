import random

nums = [
    "Bashorun",
    "Blanked",
    "C",
    "Donald",
    "Engr-TStark",
    "Enutrof",
    "Richie",
    "Sodiq",
    "Ven",
    "iamkelv",
    "curiouspaul",
    "mraction",
    "prosper",
    "toyosi"
]
cmap = {}
pairings = []


def gen_pair(arr):
    res = []
    set_ = set()
    for i in range(2):
        print(set_)
        x = random.choice(arr)
        if x not in set_:
            set_.add(x)
        else:
            while x in set_:
                x = random.choice(arr)
        res.append(nums.index(x))
    return res


def gen_pairings(pair, c1=False, c2=False):
    if len(pairings) == len(nums) // 2:
        return
    if c1 is False and c2 is False:
        if pair[0] != pair[1]:
            print(pair)
            cmap[nums[pair[0]]] = nums[pair[1]]
            pairings.append(pair)
    npair = gen_pair(nums)
    cond1 = nums[npair[0]] in cmap.keys() or nums[npair[0]] in cmap.values()
    cond2 = nums[npair[1]] in cmap.keys() or nums[npair[1]] in cmap.values()
    gen_pairings(npair, cond1, cond2)

def show_pairings():
    gen_pairings(gen_pair(nums))
    for x,y in pairings:
        print(f"{nums[x]} <--> {nums[y]}")


show_pairings()
