from ipynb.fs.defs.aoc.day_06 import (
    edges, digraph, dfs, part_1,
    bigraph, planet, bfs, part_2)

edges0 = """a)b
b)c
b)d
d)e"""

edges1 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""

edges2 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""


def test_edges():
    assert list(edges(edges0)) == \
        [('a', 'b'), ('b', 'c'), ('b', 'd'), ('d', 'e')]


def test_digraph():
    assert digraph(edges(edges0)) == \
        {'a': {'b'}, 'b': {'c', 'd'}, 'd': {'e'}}


def test_dfs():
    assert dfs(digraph(edges(edges0)), 'a') == \
        {'a': 0, 'b': 1, 'c': 2, 'd': 2, 'e': 3}
    g = digraph(edges(edges1))
    assert sum(dfs(g, 'COM').values()) == 42


def test_part_1():
    assert part_1(edges0, 'a') == 8
    assert part_1(edges1) == 42


def test_bigraph():
    g = digraph(edges(edges0))
    assert bigraph(g) == \
        {'a': {'b'}, 'b': {'a', 'c', 'd'}, 'c': {'b'},
         'd': {'b', 'e'}, 'e': {'d'}}


def test_planet():
    g = bigraph(digraph(edges(edges2)))
    assert planet(g, 'YOU') == 'K'
    assert planet(g, 'SAN') == 'I'


def test_bfs():
    g = bigraph(digraph(edges(edges2)))
    assert bfs(g, 'YOU', 'SAN') == \
        ['YOU', 'K', 'J', 'E', 'D', 'I', 'SAN']


def test_part_2():
    assert part_2(edges0, 'a', 'e') == 1
    assert part_2(edges2, 'YOU', 'SAN') == 4
