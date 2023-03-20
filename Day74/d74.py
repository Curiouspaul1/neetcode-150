from itertools import combinations


def combinationSum(candidates, target):
    # res = []
    # sample_list = candidatess
    # list_combinations = list()
    # for n in range(len(sample_list) + 1):
    #     list_combinations += list(combinations(sample_list, n))

    # for i in list_combinations:
    #     newI = sorted(i)
    #     # check if newI is present in res
    #     if sum(newI) == target and newI not in res:
    #         res.append(list(newI))
    # return res

    def dfs(remain, combo, index):
        if remain == 0:
            res.append(combo)
            return
        for i in range(index, len(candidates)):
            if candidates[i] > remain: break
            dfs(remain - candidates[i], combo + [candidates[i]], i)
    candidates.sort()
    res = []
    dfs(target, [], 0)
    return res


candidatess = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(combinationSum(candidatess, target))
