def serialize(inp_1, inp_2, inp_3, inp_4, inp_5):
    size_n = int(inp_1)  # count_jumps of
    kb_keys = list(map(int, inp_2.split()))
    kb_line = list(map(int, inp_3.split()))

    size_k = int(inp_4)
    text = list(map(int, inp_5.split()))

    return size_n, kb_keys, kb_line, size_k, text


def main():
    size_n = int(input())  # count_jumps of
    kb_keys = list(map(int, input().split()))
    kb_line = list(map(int, input().split()))

    size_k = int(input())
    text = list(map(int, input().split()))

    jumps = solve(size_n, kb_keys, kb_line, size_k, text)
    print(jumps)


def solve(size_n, kb_keys, kb_line, size_k, text):
    mapped_keys = keys_to_line(size_n, kb_keys, kb_line)
    jumps = count_jumps(mapped_keys, size_k, text)
    return jumps


def keys_to_line(size_n, kb_keys, kb_line):
    """ Return map with key_value : line_num """
    m = {}
    for i in range(size_n):
        m[kb_keys[i]] = kb_line[i]
    return m


def count_jumps(mapped_keys, size_k, text):
    """ count_jumps jumps between line """
    jumps = 0
    if size_k == 0 or size_k == 1:
        return jumps

    symb = text[0]
    l = mapped_keys[symb]
    prev_l = l
    for symb in text[1:]:
        l = mapped_keys[symb]  # current symb line number
        if l != prev_l:
            jumps += 1
            prev_l = l

    return jumps


def test():
    tests = [
        [4, [1, 2, 3, 4], [1, 2, 1, 2], 5, [1, 2, 3, 1, 4], 3],
        [3, [42, 3, 14], [1, 3, 3], 4, [3, 14, 14, 3], 0],
    ]

    test_with_serialize = [
        (
            """ 4 
            1 2 3 4
            1 2 1 2
            5
            1 2 3 1 4 """,
            3
        ),
        (
            """ 3
            42 3 14
            1 3 3
            4
            3 14 14 3 """,
            0
        ),
        (""" 0
        
        
        0 
        """,
        0
         )

    ]
    print("test starts")
    assert keys_to_line(3, [1, 2, 3], [1, 1, 1]) == {1: 1, 2: 1, 3: 1}
    assert keys_to_line(3, [1, 2, 3], [1, 2, 2]) == {1: 1, 2: 2, 3: 2}
    assert keys_to_line(0, [], []) == {}

    for test in tests:
        size_n, kb_keys, kb_line, size_k, text, jumps = test
        assert solve(size_n, kb_keys, kb_line, size_k, text) == jumps

    for test in test_with_serialize:
        text, res = test
        vals = serialize(*text.split('\n'))
        assert solve(*vals) == res



    print("test ends")


if __name__ == "__main__":
    main()
    # test()
