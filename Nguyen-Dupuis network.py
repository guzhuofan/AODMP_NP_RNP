import bisect
from typing import List, Set, Tuple
from AODMP.AODMP import *
from NP.NP import compute_np  # 导入NP算法函数
from RNP.RNP import RNP
# 测试用例实现
graph = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
od = [[1, 2], [1, 3], [4, 2], [4, 3]]
m = 2
result = aodmp(graph, od, m)
print("Path:", result)
print("path number:",len(result))
# 对每条路径计算NP值
np_results = [compute_np(path, od) for path in result]
print("NP Values:", np_results)
# 选择几条路径计算RNP值
n = 1
path = [1, 5, 6, 7, 8, 2]
rnp_result = RNP(n, path, od)
# 将一组没有公共链路的子路径元组(子路径元组中每个小元组代表一条弧)
# 构成一个列表,将列表添加到valid_combos列表中
# 一个列表代表一种子路径组合
print("path's RNP Value:", rnp_result)





