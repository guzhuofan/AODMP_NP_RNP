import bisect

def compute_np(path, od_pairs):
    """
    NP算法实现（时间复杂度O(n² + m log m)）
    """
    node_indices = {node: i for i, node in enumerate(path)}
    valid_od = set()
    od_positions = []

    # 预处理有效OD对,即起点终点均在路径上的,这时OD对的路径才有可能是path的子路径
    for (o, d) in od_pairs:
        if o in node_indices and d in node_indices:
            s, t = node_indices[o], node_indices[d]
            if s < t:
                # 有效OD对集合中是起点终点在path中,且起点终点方向和path方向相同的OD对
                valid_od.add((path[s], path[t]))
                od_positions.append((s, t))

    # 按起点排序OD对
    od_positions.sort(key=lambda x: (x[0], x[1]))
    start_positions = [x[0] for x in od_positions]

    candidate_subpaths = []
    n = len(path)

    # 筛选出所有不包含其他有效 OD 对的子路径
    for i in range(n):
        for j in range(i+1, n):
            # 每次循环会生成一个子路径,循环完会生成所有情况的子路径
            # 生成的子路径,令子路径起点为origin,终点为dest
            origin, dest = path[i], path[j]
            # 子路径起点和终点构成的 OD 对必须有效,不然直接排除
            if (origin, dest) not in valid_od:
                continue

            # 现保证子路径内部不能包含其他有效 OD 对

            # 在start_positions找到第一个大于等于i的元素的索引,
            left = bisect.bisect_left(start_positions, i)
            # 在start_positions找到第一个严格大于j-1的元素的索引,这个索引左边的元素就都是小于等于j-1的,就是重合的OD对
            right = bisect.bisect_right(start_positions, j-1)

            has_internal = False
            for k in range(left, right):
                # [left,right)代表的索引,对应所有起点在这个子路径内的OD对
                s, t = od_positions[k]
                if (s > i and t <= j) or (s == i and t < j):
                    # 候选子路径需满足：除自身OD对外，子路径范围内不存在其他有效OD对
                    # 严格内部判断
                    has_internal = True
                    break

            if not has_internal:
                candidate_subpaths.append( (i, j) )

    # 贪心算法
    if not candidate_subpaths:
        return 0

    sorted_subpaths = sorted(candidate_subpaths, key=lambda x: x[1])
    last_end = -1
    count = 0

    for start, end in sorted_subpaths:
        if start >= last_end:
            count += 1
            last_end = end

    return count


if __name__ == '__main__':
    path = [1, 3, 2, 4]
    od_set = [[1, 3], [3, 2], [2, 4],[1, 4]]
    print(compute_np(path, od_set))  # 输出3
