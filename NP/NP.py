import bisect

def compute_np(path, od_pairs):
    """
    修正版NP算法实现（时间复杂度O(n² + m log m)）
    关键修正点：贪心算法区间判断条件
    """
    node_indices = {node: i for i, node in enumerate(path)}
    valid_od = set()
    od_positions = []

    # 预处理有效OD对 [^1]
    for (o, d) in od_pairs:
        if o in node_indices and d in node_indices:
            s, t = node_indices[o], node_indices[d]
            if s < t:
                valid_od.add((path[s], path[t]))  # 修正点1：存储原始节点对
                od_positions.append((s, t))

    # 按起点排序OD对 [^2]
    od_positions.sort(key=lambda x: (x[0], x[1]))
    start_positions = [x[0] for x in od_positions]

    candidate_subpaths = []
    n = len(path)

    # 生成候选子路径
    for i in range(n):
        for j in range(i+1, n):
            # 快速有效性检查 [^3]
            origin, dest = path[i], path[j]
            if (origin, dest) not in valid_od:
                continue

            # 二分查找优化 [^4]
            left = bisect.bisect_left(start_positions, i)
            right = bisect.bisect_right(start_positions, j-1)

            has_internal = False
            for k in range(left, right):
                s, t = od_positions[k]
                if t <= j and s > i:  # 严格内部判断
                    has_internal = True
                    break

            if not has_internal:
                candidate_subpaths.append( (i, j) )

    # 贪心算法修正 [^5]
    if not candidate_subpaths:
        return 0

    sorted_subpaths = sorted(candidate_subpaths, key=lambda x: x[1])
    last_end = -1
    count = 0

    for start, end in sorted_subpaths:
        if start >= last_end:  # 关键修正：允许端点相接
            count += 1
            last_end = end

    return count


if __name__ == '__main__':
    path = [1, 3, 2, 4]
    od_set = [[1, 3], [3, 2], [2, 4],[1, 4]]
    print(compute_np(path, od_set))  # 输出3
