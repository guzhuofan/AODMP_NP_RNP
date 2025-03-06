from collections import deque


def find_all_valid_paths(graph, start, end, shortest_length, max_extra_steps):
    """改进后的安全路径搜索函数"""
    """
        高效查找所有从起点到终点且长度不超过最短路径+M步的路径

        参数：
        graph : List[List[int]] - 邻接矩阵
        start : int - 起点编号（从1开始）
        end : int - 终点编号（从1开始）
        shortest_length : int - 最短路径长度（基于节点编号从1开始）
        max_extra_steps : int - 允许的最大额外步数(M)

        返回：
        List[List[int]] - 所有有效路径集合，按节点数升序排列，路径中的节点编号从1开始
    """
    start_node = start - 1
    end_node = end - 1
    max_steps = shortest_length + max_extra_steps
    visited_records = set()  # 改用集合提高查询效率
    path_queue = deque([(start_node, [start_node])])
    valid_paths = []

    while path_queue:
        current_node, current_path = path_queue.popleft()

        if current_node == end_node:
            valid_paths.append([x + 1 for x in current_path])
            continue

        if len(current_path) > max_steps:
            continue

        # 生成唯一路径特征防止重复探索[^4]
        path_signature = (current_node, frozenset(current_path))
        if path_signature in visited_records:
            continue
        visited_records.add(path_signature)

        for neighbor in get_valid_neighbors(graph, current_node):
            if neighbor not in current_path:
                new_path = current_path + [neighbor]
                path_queue.append((neighbor, new_path))

    return valid_paths


def get_valid_neighbors(graph, node):
    """添加边界检查的邻居获取"""
    if node < 0 or node >= len(graph):
        return []
    return [i for i, val in enumerate(graph[node]) if val == 1]


if __name__ == "__main__":
    # 定义4节点图的邻接矩阵
    adj_matrix = [
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

    # 查找从节点1到4的所有路径（已知最短步数=2，允许额外1步）
    paths = find_all_valid_paths(
        graph=adj_matrix,
        start=4,
        end=2,
        shortest_length=4,
        max_extra_steps=2
    )

    # 输出结果（每个子列表对应一条路径）
    print(paths)
    # 可能输出：[[1, 3, 4], [1, 2, 3, 4]]
