from collections import defaultdict

def tricks(domains, lower, upper):
    graph = [{0: set()}]
    for i, dom in enumerate(domains):
        graph.append({})
        for pred in graph[i]:
            for v in dom:
                graph[i][pred].add((v, pred + v))
                graph[i + 1][pred + v] = set()

    for v in set(graph[-1]):
        if v < lower or v > upper:
            del graph[-1][v]

    for i in reversed(range(len(graph) - 1)):
        for parent, arcs in graph[i].items():
            for v, dest in set(arcs):
                if dest not in set(graph[i + 1]):
                    graph[i][parent].remove((v, dest))

    filtered_domains = [
            {v for _, arcs in graph[i].items() for v, _ in arcs}
            for i in range(len(graph) - 1)
            ]
    return filtered_domains


print(tricks([(0, 2), (0, 3), (0, 4), (0, 5)], 10, 12))

