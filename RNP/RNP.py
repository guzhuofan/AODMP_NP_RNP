from itertools import combinations


def RNP(n, path, W):
    """
    计算路径p上无公共链路的n个子路径族集合
    :param n: 需要选取的子路径数量
    :param path: 路径节点列表，如[1,2,3,4,5]
    :param W: 所有有效OD对集合，如[(1,2), (3,4), (4,5)]
    :return: 符合条件的子路径族集合，元素为按路径顺序排列的边元组
    """
    # 生成所有合法子路径
    valid_subpaths = generate_valid_subpaths(path, W)

    # 枚举所有n个元素的组合并筛选无冲突的
    valid_combos = []
    for combo in combinations(valid_subpaths, n):
        if is_independent(combo):
            sorted_combo = sorted(combo, key=lambda x: x['start'])
            valid_combos.append([tuple(sp['edges']) for sp in sorted_combo])

    return valid_combos


def generate_valid_subpaths(path, W):
    """生成路径上所有满足OD对的有效子路径"""
    W_set = {(o, d) for o, d in W}
    subpaths = []
    for start in range(len(path)):
        for end in range(start + 1, len(path)):
            od = (path[start], path[end])
            if od in W_set:
                edges = [(path[i], path[i + 1]) for i in range(start, end)]
                subpaths.append({
                    'edges': edges,
                    'edges_set': set(edges),
                    'start': start  # 用于结果排序
                })
    return subpaths


def is_independent(combo):
    """检查组合内所有子路径边是否互不相交"""
    seen = set()
    for sp in combo:
        if seen & sp['edges_set']:
            return False
        seen.update(sp['edges_set'])
    return True

if __name__ == '__main__':
    n = 2
    path =[1, 3, 2, 4]
    W = [[1, 3], [3, 2], [2, 4],[1, 4]]
    print(RNP(n, path, W))