def serialize(line1, line2):
    count, ideal_w, time = list(map(int, line1.split()))
    weights = list(map(int, line2.split()))

    return count, ideal_w, time, weights


def main():
    c, i, t = list(map(int, input().split()))
    w = list(map(int, input().split()))
    res_n, res = solve(c, i, t, w)
    print(res_n)
    if res_n == 0:
        return
    else:
        print(*res)

def test():
    test_data = [
        ["3 5 2", "5 10 6", 2, [1, 3]],
        ["5 19 32", "36 10 72 4 50", 2, [2, 4]],
        ["4 25 10", "1 10 42 9", 0, []],
        ["2 12 10", "10 14", 2, [1, 2]]
    ]
    print('test starts')
    for data in test_data:
        res = data.pop(-1)
        res_n = data.pop(-1)
        c, i, t, w = serialize(*data)
        assert solve(c, i, t, w) == (res_n, res)
    print('test ends')


def count_ideal_fig(count_n, ideal_w, time, weights, args_sorted):
    if count_n == 0:
        return 0, []

    if count_n == 1:
        if ideal_w - time <= weights[0] <= ideal_w + time:
            return 1, weights
        else:
            return 0, []

    # find nearest to ideal wight figure
    remain_time = time

    nearest_left_i = None
    nearest_right_i = None
    for i in range(count_n):
        item_indx = args_sorted[i]
        item_w = weights[item_indx]

        if ideal_w < item_w:
            nearest_right_i = i
            break
        nearest_left_i = i

    # count maximum ideals figures:
    count_figures = 0
    figures = []
    while True:
        # check borders:
        if nearest_left_i is not None and nearest_left_i < 0:
            nearest_left_i = None
        if nearest_right_i is not None and nearest_right_i >= count_n:
            nearest_right_i = None

        # count step to left
        if nearest_left_i is None:
            step_to_left = float('inf')
        else:
            nearest_left = weights[args_sorted[nearest_left_i]]
            step_to_left = ideal_w - nearest_left

        # count step to right
        if nearest_right_i is None:
            step_to_right = float('inf')
        else:
            nearest_right = weights[args_sorted[nearest_right_i]]
            step_to_right = nearest_right - ideal_w

        # if all borders passed
        if nearest_right_i is None and nearest_left_i is None:
            break

        # choice best one

        # if left is best
        if step_to_left <= step_to_right:
            # check
            if remain_time - step_to_left < 0:
                nearest_left_i = None  # not look at left anymore
            else:
                remain_time -= step_to_left
                figures.append(args_sorted[nearest_left_i] + 1)
                # figures += str(args_sorted[nearest_left_i] + 1)
                count_figures += 1
                nearest_left_i -= 1
        # if right is best
        else:
            if remain_time - step_to_right < 0:
                nearest_right_i = None  # not look at right anymore
            else:
                remain_time -= step_to_right
                figures.append(args_sorted[nearest_right_i] + 1)
                count_figures += 1
                nearest_right_i += 1
    # figures.sort()
    return count_figures, figures


def get_args_of_array(seq):
    args = sorted(range(len(seq)), key=seq.__getitem__)
    return args  # indexes but sorted


def solve(count_n, ideal_w, time, weights):
    args_sorted = get_args_of_array(weights)
    n_fig, figures = count_ideal_fig(count_n, ideal_w, time, weights, args_sorted)
    return n_fig, figures


if __name__ == '__main__':
    # main()
    test()
