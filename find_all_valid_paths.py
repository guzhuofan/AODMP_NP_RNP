from collections import deque

from dijkstra_shortest_path import dijkstra_shortest_path


def find_all_valid_paths(graph, start, end, shortest_length, max_extra_steps):
    """
    高效查找所有从起点到终点且长度不超过最短路径+M步的路径

    参数：
    graph : List[List[int]] - 邻接矩阵
    start : int - 起点编号
    end : int - 终点编号
    max_extra_steps : int - 允许的最大额外步数(M)

    返回：
    List[List[int]] - 所有有效路径集合，按节点数升序排列
    """
    max_steps = shortest_length + max_extra_steps
    visited_records = {}
    path_queue = deque()
    path_queue.append((start, [start]))

    valid_paths = []

    while path_queue:
        current_node, current_path = path_queue.popleft()

        # 终止条件检测
        if current_node == end:
            valid_paths.append(current_path)
            continue

        # 剪枝条件：超出最大步数限制
        if len(current_path) > max_steps:
            continue

        for neighbor in get_valid_neighbors(graph, current_node):
            # 避免路径回环
            if neighbor in current_path:
                continue

            # 路径缓存优化
            path_key = (neighbor, tuple(current_path))
            if path_key not in visited_records:
                new_path = current_path + [neighbor]
                path_queue.append((neighbor, new_path))
                visited_records[path_key] = True

    return valid_paths

def get_valid_neighbors(graph, node):
    """获取有效邻居节点"""
    return [i for i, val in enumerate(graph[node]) if val == 1]

if __name__ == "__main__":
    # 定义4节点图的邻接矩阵
    adj_matrix = [
        [0, 1, 1, 0],  # Node 0
        [1, 0, 1, 0],  # Node 1
        [1, 1, 0, 1],  # Node 2
        [0, 0, 1, 0]  # Node 3
    ]

    # 查找从节点0到3的所有路径（已知最短步数=2，允许额外1步）
    paths = find_all_valid_paths(
        graph=adj_matrix,
        start=0,
        end=3,
        shortest_length=2,
        max_extra_steps=1
    )

    # 输出结果（每个子列表对应一条路径）
    print(paths)
    # 可能输出：[[0,2,3,0], [0,1,2,3]]
