
import random

# f_cnt, t_cnt = 3, 10  # number of functions and terminals
# t_perc = 0.7


def dfs(t_perc):
    # if random.random() < t_cnt / (f_cnt + t_cnt):
    if random.random() < t_perc:
        return 1, 1
    L_depth, L_nodes = dfs(t_perc)
    R_depth, R_nodes = dfs(t_perc)
    return max(L_depth , R_depth) + 1, L_nodes + R_nodes + 1

if __name__ == '__main__':
    # for t_perc in [0.7, 0.8, 0.9]:
    for t_perc in [0.9999, 0.999, 0.99, 0.95, 0.9, 0.8, 0.7, 0.65, 0.6, 0.55, 0.54, 0.53, 0.52, 0.51, 0.505]:
        results = []
        for test_id in range(0, 100000):
            # print(dfs(t_perc))
            results.append(dfs(t_perc))
        print('terminal percentage = {:.2f}% : average depth = {:.4f} , average nodes = {:.4f}'.format(
            t_perc * 100,
            sum([r[0] for r in results]) / len(results),
            sum([r[1] for r in results]) / len(results),
        ))

