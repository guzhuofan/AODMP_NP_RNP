# 算法展示
# 输入例子Brasse network
from AODMP.AODMP import aodmp
from NP.NP import compute_np
from RNP.RNP import RNP

Graph = [
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 0, 0]
]
OD = [[1, 3], [2, 4], [3, 2], [1, 4]]
M = 1
result = aodmp(Graph, OD, M)
print(result)
# 对每条路径计算NP值
np_results = [compute_np(path, OD) for path in result]
print("NP Values:", np_results)
# 选择几条路径计算RNP值
n = 2
path = [1,3,2,4]
print(RNP(n,path,OD))
