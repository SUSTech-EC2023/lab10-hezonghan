

# import matplotlib.pyplot as plt


def solve_depth(t_perc, max_d):

    # prob = [0, t_perc]
    # prob_sum = [0, t_perc]

    prob = [None] * (max_d + 1)
    prob_sum = [None] * (max_d + 1)

    prob[0] = 0
    prob_sum[0] = 0

    prob[1] = t_perc
    prob_sum[1] = t_perc

    for d in range(2, max_d + 1):
        prob[d] = (1-t_perc) * (
            prob[d-1] * prob[d-1] +
            2 * prob[d-1] * prob_sum[d-2]
        )
        prob_sum[d] = prob_sum[d-1] + prob[d]

    avg = sum([d * prob[d] for d in range(1, max_d + 1)])

    return prob, prob_sum, avg


def solve_nodes_cnt(t_perc, max_n):

    # prob = [0, t_perc]
    # prob_sum = [0, t_perc]

    prob = [None] * (max_n + 1)
    prob_sum = [None] * (max_n + 1)

    prob[0] = 0
    prob_sum[0] = 0

    prob[1] = t_perc
    prob_sum[1] = t_perc

    for n in range(2, max_n + 1):
        s = 0
        for l in range(1, n-2+1):
            s += prob[l] * prob[n-1-l]
        
        prob[n] = (1 - t_perc) * s
        prob_sum[n] = prob_sum[n-1] + prob[n]

    avg = sum([n * prob[n] for n in range(1, max_n + 1)])

    return prob, prob_sum, avg



# prob, prob_sum, avg = solve_depth(t_perc=0.6, max_d=50)
# print(prob)
# print(prob_sum)
# print(avg)


if __name__ == '__main__':

    x, y = [], []
    
    for t_perc in [0.9999, 0.999, 0.99, 0.95, 0.9, 0.8, 0.7, 0.65, 0.6, 0.55, 0.54, 0.53, 0.52, 0.51, 0.505,   0.5, 0.49, 0.48, 0.47, 0.46, 0.45, 0.4]:
        _, depth_prob_sum, depth_avg = solve_depth(t_perc=t_perc, max_d=10000)
        # _, depth_prob_sum, depth_avg = solve_depth(t_perc=t_perc, max_d=1000)   # 10000
        
        _, nodes_prob_sum, nodes_avg = solve_nodes_cnt(t_perc=t_perc, max_n=5000)
        # _, nodes_prob_sum, nodes_avg = [], [0], 0
        
        print('terminal percentage = {:.2f}% : average depth = {:.8f} (final {:.4f}%) , average nodes = {:.4f} (final {:.4f}%)'.format(
            t_perc * 100,
            depth_avg,
            depth_prob_sum[-1] * 100,
            nodes_avg,
            nodes_prob_sum[-1] * 100,
        ))

        x.append(t_perc)
        y.append(depth_avg)

    # plt.figure()
    # plt.plot(x, y)
    # plt.imsave('./depth.svg')
    # plt.show()
