from ipynb.fs.defs.aoc.day_03 import manhattan, trace, intersections, part_1, part_2

example_0 = [['R1', 'U1', 'L1', 'D1'], ['D1']]
example_1 = [['R2', 'U1', 'L1', 'D2'], ['D1']]  # self-cross at (1, 0)
example_2 = [
    ['R8', 'U5', 'L5', 'D3'],
    ['U7', 'R6', 'D4', 'L4']]
example_3 = [
    ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
    ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']]
example_4 = [
    ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
    ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15' ,'U6', 'R7']]


def test_manhattan():
    assert manhattan((1, 1), (0, 0)) == 2
    assert manhattan((1, 1)) == 2
    assert manhattan((0, 0)) == 0
    assert manhattan((2, 2), (1, 1)) == 2
    assert manhattan((1, 1), (1, 1)) == 0
    assert manhattan((-1, -1)) == 2
    assert manhattan((-1, 1)) == 2
    assert manhattan((1, -1)) == 2


def test_trace():
    assert trace(example_0[0]) == [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]
    assert trace(example_1[0]) == [(0, 0), (1, 0), (2, 0), (2, 1), (1, 1), (1, 0), (1, -1)]
    assert trace(example_2[0]) == [
        (0, 0),
        (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0),  # R8
        (8, 1), (8, 2), (8, 3), (8, 4), (8, 5),  # U5
        (7, 5), (6, 5), (5, 5), (4, 5), (3, 5),  # L5
        (3, 4), (3, 3), (3, 2), # D5
    ]
    assert trace(example_2[1]) == [
        (0, 0),
        (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),  # U7
        (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7),  # R6
        (6, 6), (6, 5), (6, 4), (6, 3),  # D4
        (5, 3), (4, 3), (3, 3), (2, 3),  # L4
    ]


def test_intersections():
    assert set(intersections(map(trace, example_0))) == {(0, 0)}
    assert set(intersections(map(trace, example_1))) == {(0, 0)}
    assert set(intersections(map(trace, example_2))) == {(0, 0), (3, 3), (6, 5)}


def test_part_1():
    assert part_1(example_0) == []
    assert part_1(example_1) == []
    assert part_1(example_2)[0] == 6
    assert part_1(example_3)[0] == 159
    assert part_1(example_4)[0] == 135


def test_part_2():
    assert part_2(example_0) == []
    assert part_2(example_1) == []
    assert part_2(example_2)[0] == 30
    assert part_2(example_3)[0] == 610
    assert part_2(example_4)[0] == 410
    