from ipynb.fs.defs.aoc import day_01


def test_compute_fuel_pt1():
    assert day_01.compute_fuel_pt1(12) == 2
    assert day_01.compute_fuel_pt1(14) == 2
    assert day_01.compute_fuel_pt1(1969) == 654
    assert day_01.compute_fuel_pt1(100756) == 33583


def test_compute_fuel_pt2():
    assert day_01.compute_fuel_pt2(14) == 2
    assert day_01.compute_fuel_pt2(1969) == 966
    assert day_01.compute_fuel_pt2(100756) == 50346
    