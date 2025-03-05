# AODMP算法展示
# 输入例子Brasse网络
# Graph=[0 1 1 0;0 0 0 1;0 1 0 1;0 0 0 0];
# OD=[1 3;2 4;3 2;1 4];
# M=1;
# ALLOD3path=AODMP(Graph,OD,M);
from AODMP.AODMP import aodmp

Graph = [
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 0, 0]
]
OD = [[0, 3], [1, 3], [2, 1], [0, 2]]
M = 1
ALLOD3path = aodmp(Graph, OD, M)
print(ALLOD3path)
