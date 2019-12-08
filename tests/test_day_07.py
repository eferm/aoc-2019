from ipynb.fs.defs.aoc.day_07 import IntCode, part_1, part_2


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
    program = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    assert part_1(program) == (43210, '43210')

    program = [3,23,3,24,1002,24,10,24,1002,23,-1,23,
               101,5,23,23,1,24,23,23,4,23,99,0,0]
    assert part_1(program) == (54321, '01234')
    
    program = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
               1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
    assert part_1(program) == (65210, '10432')


def test_part_2():
    program = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
               27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    assert part_2(program) == (139629729, '98765')

    program = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
               -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
               53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
    assert part_2(program) == (18216, '97856')
