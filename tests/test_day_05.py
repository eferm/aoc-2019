import io
import re
from functools import partial
from contextlib import redirect_stdout

from ipynb.fs.defs.aoc.day_05 import part_1, part_2


def capture(func, *args, **kwargs):
    f = io.StringIO()
    with redirect_stdout(f):
        func(*args, **kwargs)
    s = f.getvalue()
    print(s)
    return int(re.match("^out: ([0-9]+)", s)[1])    


def test_part_1():
    assert part_1([1002,4,3,4,33], _input=1) == [1002, 4, 3, 4, 99]

    assert capture(part_1, [3,0,4,0,99], _input=1) == 1
    assert capture(part_1, [3,0,4,0,99], _input=1000) == 1000


def test_part_2_bool():
    # eq 8
    assert capture(part_2, [3,9,8,9,10,9,4,9,99,-1,8], _input=8) == 1
    assert capture(part_2, [3,9,8,9,10,9,4,9,99,-1,8], _input=7) == 0
    assert capture(part_2, [3,9,8,9,10,9,4,9,99,-1,8], _input=9) == 0
    
    assert capture(part_2, [3,3,1108,-1,8,3,4,3,99], _input=8) == 1
    assert capture(part_2, [3,3,1108,-1,8,3,4,3,99], _input=7) == 0
    assert capture(part_2, [3,3,1108,-1,8,3,4,3,99], _input=9) == 0
    
    # lt 8
    assert capture(part_2, [3,9,7,9,10,9,4,9,99,-1,8], _input=7) == 1
    assert capture(part_2, [3,9,7,9,10,9,4,9,99,-1,8], _input=8) == 0
    assert capture(part_2, [3,9,7,9,10,9,4,9,99,-1,8], _input=9) == 0
    
    assert capture(part_2, [3,3,1107,-1,8,3,4,3,99], _input=7) == 1
    assert capture(part_2, [3,3,1107,-1,8,3,4,3,99], _input=8) == 0
    assert capture(part_2, [3,3,1107,-1,8,3,4,3,99], _input=9) == 0


def test_part_2_jump():
    # jump
    assert capture(part_2, [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], _input=0) == 0
    assert capture(part_2, [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], _input=1) == 1
    assert capture(part_2, [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], _input=10) == 1
    assert capture(part_2, [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], _input=-1) == 1
    
    assert capture(part_2, [3,3,1105,-1,9,1101,0,0,12,4,12,99,1], _input=0) == 0
    assert capture(part_2, [3,3,1105,-1,9,1101,0,0,12,4,12,99,1], _input=1) == 1
    assert capture(part_2, [3,3,1105,-1,9,1101,0,0,12,4,12,99,1], _input=10) == 1
    assert capture(part_2, [3,3,1105,-1,9,1101,0,0,12,4,12,99,1], _input=-1) == 1


def test_part_2():
    program = [
        3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
        1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
        999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
    assert capture(part_2, program, _input=7) == 999
    assert capture(part_2, program, _input=9) == 1001
    