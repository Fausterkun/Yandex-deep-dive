def main():
    len_c = int(input())
    c_inc = list(map(int, input().split()))
    c_edu = list(map(int, input().split()))
    c_parents = list(map(bool, map(int, input().split())))

    len_p = int(input())
    p_inc = list(map(int, input().split()))
    p_edu = list(map(int, input().split()))
    # p_parents = list(map(lambda x: x if x != 0 else None, map(int, input().split())))
    p_parents = list(map(int, input().split()))

    res = solve(len_c, c_inc, c_edu, c_parents, len_p, p_inc, p_edu, p_parents)
    print(*res)


def solve(len_c, c_inc, c_edu, c_parents, len_p, p_inc, p_edu, p_parents):
    countries = []
    for i in range(len_p):
        country_num = by_coolest = None

        # check best by parents
        by_parents = p_parents[i]
        if by_parents == 0:
            by_parents = None
        # there by_parents is None or val >= 1

        if by_parents is not None:
            if not c_parents[by_parents - 1]:  # if access by parents forbidden by country:
                by_parents = None

        # check best by coolest for each country
        inc = p_inc[i]
        edu = p_edu[i]

        if by_parents is None:
            for k in range(len_c):
                if edu >= c_edu[k] and inc >= c_inc[k]:
                    by_coolest = k + 1
                    break
        else:
            for k in range(by_parents):
                if inc >= c_inc[k] and edu >= c_edu[k]:
                    by_coolest = k + 1
                    break

        # choice which country is add
        if by_coolest is not None and by_parents is not None:
            country_num = min(by_coolest, by_parents)
        elif by_coolest is None and by_parents is None:
            country_num = None
        elif by_coolest is None:
            country_num = by_parents
        elif by_parents is None:
            country_num = by_coolest

        if country_num is None:
            country_num = 0
        countries.append(country_num)

    return countries


if __name__ == "__main__":
    main()
