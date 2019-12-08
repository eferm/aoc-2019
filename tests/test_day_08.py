from ipynb.fs.defs.aoc.day_08 import to_layers, to_img

def test_to_layers():
    assert to_layers('123456789012', 3, 2) == ['123456', '789012']
    assert to_layers('0222112222120000', 2, 2) == ['0222', '1122', '2212', '0000']


def test_to_img():
    assert to_img(to_layers('0222112222120000', 2, 2)) == '0110'
