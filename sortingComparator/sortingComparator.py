#!/bin/python3

from functools import cmp_to_key

#
# Complete the 'Player' class below.
#
# The comparator class function is expected to return an integer.
# The class accepts following parameters:
#  1.  String name
#  2.  Integer score
#

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def comparator(a, b):      
        if (a.score < b.score):
            return 1
        if (a.score > b.score):
            return -1
        if (a.name.lower() < b.name.lower()):
            return -1
        if (a.name.lower() > b.name.lower()):
            return 1
        return 0

#
# Expected input sample:
#  
# 3
# Smith 20
# Jones 15
# Jones 20
#

n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)