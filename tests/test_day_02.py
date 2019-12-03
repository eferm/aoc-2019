from ipynb.fs.defs.aoc.day_02 import process_program, process_tape


def test_process_program():
    assert process_program([1,0,0,0,99]) == [2,0,0,0,99]
    assert process_program([2,3,0,3,99]) == [2,3,0,6,99]
    assert process_program([2,4,4,5,99,0]) == [2,4,4,5,99,9801]


def test_process_tape():
    assert process_tape([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]
