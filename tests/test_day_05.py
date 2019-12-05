import io
import re
from functools import partial
from contextlib import redirect_stdout

from ipynb.fs.defs.aoc.day_05 import pad, process_pt1, process_pt2


def _output(func, *args):
    f = io.StringIO()
    with redirect_stdout(f):
        func(*args)
    s = f.getvalue()
    return int(re.match("^output: ([0-9]+)", s)[1])    


def test_pad():
    assert pad(1) == '00001'
    assert pad(1001) == '01001'


def test_process_pt1():
    assert process_pt1([1002,4,3,4,33], 1) == [1002, 4, 3, 4, 99]

    assert _output(process_pt1, [3,0,4,0,99], 1) == 1
    assert _output(process_pt1, [3,0,4,0,99], 1000) == 1000


def test_process_pt2_bool():
    # eq 8
    assert _output(process_pt2, [3,9,8,9,10,9,4,9,99,-1,8], 8) == 1
    assert _output(process_pt2, [3,9,8,9,10,9,4,9,99,-1,8], 7) == 0
    assert _output(process_pt2, [3,9,8,9,10,9,4,9,99,-1,8], 9) == 0
    
    assert _output(process_pt2, [3,3,1108,-1,8,3,4,3,99], 8) == 1
    assert _output(process_pt2, [3,3,1108,-1,8,3,4,3,99], 7) == 0
    assert _output(process_pt2, [3,3,1108,-1,8,3,4,3,99], 9) == 0
    
    # lt 8
    assert _output(process_pt2, [3,9,7,9,10,9,4,9,99,-1,8], 7) == 1
    assert _output(process_pt2, [3,9,7,9,10,9,4,9,99,-1,8], 8) == 0
    assert _output(process_pt2, [3,9,7,9,10,9,4,9,99,-1,8], 9) == 0
    
    assert _output(process_pt2, [3,3,1107,-1,8,3,4,3,99], 7) == 1
    assert _output(process_pt2, [3,3,1107,-1,8,3,4,3,99], 8) == 0
    assert _output(process_pt2, [3,3,1107,-1,8,3,4,3,99], 9) == 0


def test_process_pt2_jump():
    # jump
    assert _output(process_pt2, [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 0) == 0
    assert _output(process_pt2, [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 1) == 1
    assert _output(process_pt2, [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 10) == 1
    assert _output(process_pt2, [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], -1) == 1
    
    assert _output(process_pt2, [3,3,1105,-1,9,1101,0,0,12,4,12,99,1], 0) == 0
    assert _output(process_pt2, [3,3,1105,-1,9,1101,0,0,12,4,12,99,1], 1) == 1
    assert _output(process_pt2, [3,3,1105,-1,9,1101,0,0,12,4,12,99,1], 10) == 1
    assert _output(process_pt2, [3,3,1105,-1,9,1101,0,0,12,4,12,99,1], -1) == 1


def test_process_pt2():
    program = [
        3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
        1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
        999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
    assert _output(process_pt2, program, 7) == 999
    assert _output(process_pt2, program, 9) == 1001
    