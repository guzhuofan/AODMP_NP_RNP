from typing import List, Union
from dijkstra_shortest_path import dijkstra_shortest_path
from find_all_valid_paths import find_all_valid_paths,get_valid_neighbors


def aodmp(graph: List[List[int]], od_pairs: List[List[int]], max_extra_steps: int) -> List[List[int]]:
    """高效生成所有OD对的有效路径集合

    Args:
        graph: 邻接矩阵表示的图结构，graph[i][j]=1表示存在i->j的边
        od_pairs: OD对列表，每个元素为[origin, destination]格式
        max_extra_steps: 允许相比最短路径增加的最大路段数

    Returns:
        所有满足长度约束的有效路径集合，按OD对顺序排列
    """
    all_valid_paths = []

    for origin, destination in od_pairs:
        # 获取最短路径长度
        shortest_length = dijkstra_shortest_path(graph, origin, destination)

        # 处理不可达情况
        if shortest_length == -1:
            continue

        # 获取当前OD对的所有有效路径
        od_paths = find_all_valid_paths(
            graph=graph,
            start=origin,
            end=destination,
            shortest_length=shortest_length,
            max_extra_steps=max_extra_steps
        )

        # 按节点数升序合并结果
        all_valid_paths.extend(sorted(od_paths, key=len))

    return all_valid_paths

if __name__ == '__main__':
    # 测试Brasse网络案例
    graph = [
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 1],
        [0, 0, 0, 0]
    ]
    od_pairs = [[0, 3], [1, 3], [2, 1], [0, 2]]
    print(aodmp(graph, od_pairs, 1))
    # [[0, 1, 3], [0, 2, 3], [0, 2, 1, 3], [1, 3], [2, 1], [0, 2]] 的路径组合
