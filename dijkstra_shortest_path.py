import heapq


def dijkstra_shortest_path(graph, start_node, end_node):
    """
    计算无权图中起点到终点的最短路径长度（边权重默认为1）
    参数：
    graph: List[List[int]] - 邻接矩阵表示的图
    start_node: int - 起点索引（从0开始）
    end_node: int - 终点索引
    返回：
    int - 最短路径长度，不可达时返回-1
    """
    # 初始化数据结构
    num_nodes = len(graph)
    min_distances = [float('inf')] * num_nodes  # 起点到各节点的最短距离
    min_distances[start_node] = 0

    # 创建邻接表优化访问效率（预处理阶段）
    adjacency_list = [[] for _ in range(num_nodes)]
    for u in range(num_nodes):
        for v in range(num_nodes):
            if graph[u][v] == 1 and u != v:
                adjacency_list[u].append(v)
                # 行索引对应节点：adjacency_list[u]表示图中索引为 u的节点
                # 列表内容为邻接节点：每个子列表存储的是该行对应节点的直接相邻节点索引

    # 使用最小堆优化节点选取
    priority_queue = [(0, start_node)] # 优先队列，按距离从小到大排序
    visited = set() # 用于记录已处理的节点，避免重复处理

    while priority_queue:
        # 从优先队列中取出距离最小的节点
        current_distance, current_node = heapq.heappop(priority_queue)

        # 提前终止条件：找到目标节点,目标节点第一次出来一定就是最短距离
        if current_node == end_node:
            return current_distance

        # 跳过已处理的点,这时这些点已经达到最小距离的了,这些就是优先队列中要清理的
        if current_node in visited:
            continue

        # 如果不是已经处理过的点,那第一次弹出一定就是最短距离,则加入visited
        visited.add(current_node)

        # 遍历当前达到最短距离的节点所有的相邻节点
        for neighbor in adjacency_list[current_node]:
            new_distance = current_distance + 1  # 边权重默认为1
            # 发现更短路径时更新到优先队列中备选
            if new_distance < min_distances[neighbor]:
                min_distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return -1  # 不可达情况


if __name__ == '__main__':
    # 定义4节点图的邻接矩阵
    adj_matrix = [
        [0, 1, 0, 1],  # Node 0
        [1, 0, 1, 1],  # Node 1
        [0, 1, 0, 1],  # Node 2
        [1, 1, 1, 0]  # Node 3
    ]

    print(dijkstra_shortest_path(adj_matrix, 0, 3))  # 输出：3（路径0-1-2-3）


