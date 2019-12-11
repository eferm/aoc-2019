from ipynb.fs.defs.aoc.day_09 import IntCode, part_1, part_2


def test_IntCode():
    # day 2
    assert next(IntCode([1,0,0,0,99]).run()).mem == [2,0,0,0,99]
    assert next(IntCode([2,3,0,3,99]).run()).mem == [2,3,0,6,99]
    assert next(IntCode([2,4,4,5,99,0]).run()).mem == [2,4,4,5,99,9801]
    assert next(IntCode([1,1,1,4,99,5,6,0,99]).run()).mem == [30,1,1,4,2,5,6,0,99]
    assert next(IntCode([1002,4,3,4,33]).run()).mem == [1002, 4, 3, 4, 99]
    
    # input / output
    assert next(IntCode([3,0,4,0,99]).run([1])).output == 1
    assert next(IntCode([3,0,4,0,99]).run([1000])).output == 1000

    # eq
    assert next(IntCode([3,9,8,9,10,9,4,9,99,-1,8]).run([8])).output == 1
    assert next(IntCode([3,9,8,9,10,9,4,9,99,-1,8]).run([7])).output == 0
    assert next(IntCode([3,9,8,9,10,9,4,9,99,-1,8]).run([9])).output == 0
    
    assert next(IntCode([3,3,1108,-1,8,3,4,3,99]).run([8])).output == 1
    assert next(IntCode([3,3,1108,-1,8,3,4,3,99]).run([7])).output == 0
    assert next(IntCode([3,3,1108,-1,8,3,4,3,99]).run([9])).output == 0
    
    # lt 8
    assert next(IntCode([3,9,7,9,10,9,4,9,99,-1,8]).run([7])).output == 1
    assert next(IntCode([3,9,7,9,10,9,4,9,99,-1,8]).run([8])).output == 0
    assert next(IntCode([3,9,7,9,10,9,4,9,99,-1,8]).run([9])).output == 0
    
    assert next(IntCode([3,3,1107,-1,8,3,4,3,99]).run([7])).output == 1
    assert next(IntCode([3,3,1107,-1,8,3,4,3,99]).run([8])).output == 0
    assert next(IntCode([3,3,1107,-1,8,3,4,3,99]).run([9])).output == 0

    # jump
    assert next(IntCode([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]).run([0])).output == 0
    assert next(IntCode([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]).run([1])).output == 1
    assert next(IntCode([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]).run([10])).output == 1
    assert next(IntCode([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]).run([-1])).output == 1
    
    assert next(IntCode([3,3,1105,-1,9,1101,0,0,12,4,12,99,1]).run([0])).output == 0
    assert next(IntCode([3,3,1105,-1,9,1101,0,0,12,4,12,99,1]).run([1])).output == 1
    assert next(IntCode([3,3,1105,-1,9,1101,0,0,12,4,12,99,1]).run([10])).output == 1
    assert next(IntCode([3,3,1105,-1,9,1101,0,0,12,4,12,99,1]).run([-1])).output == 1

    # day 5
    program = [
        3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
        1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
        999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
    assert next(IntCode(program).run([7])).output == 999
    assert next(IntCode(program).run([9])).output == 1001


def test_part_1():
    program = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    assert next(IntCode(program).run()).mem == program
    
    program = [1102,34915192,34915192,7,4,7,99,0]
    assert len(str(next(IntCode(program).run()).output)) == 16

    program = [104,1125899906842624,99]
    assert next(IntCode(program).run()).output == program[1]
