# 그래프 생성
graph = {}
graph["start"] = {}
graph["start"]["A"] = 6
graph["start"]["C"] = 1
graph["A"] = {}
graph["A"]["B"] = 16
graph["A"]["D"] = 20
graph["C"] = {}
graph["C"]["B"] = 30
graph["C"]["D"] = 35
graph["B"] = {}
graph["B"]["final"] = 21
graph["D"] = {}
graph["D"]["final"] = 10
graph["final"] = {}


# 각 정점의 가격표 생성
costs = {}
inf = float("inf") # 무한대수 생성
costs["A"] = 6
costs["B"] = inf
costs["C"] = 1
costs["D"] = inf
costs["final"] = inf

# 각 정점의 부모표 생성
parents = {}
parents["A"] = "start"
parents["B"] = None
parents["C"] = "start"
parents["D"] = None
parents["final"] = None

# 체크한 정점이 중복되지 않도록 표시하는 리스트 생성
cheked = []


def find_lowest_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in cheked:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node



# 출발점과 이웃 중 가장 작은 정점 탐색
node = find_lowest_node(costs)

while node is not None:
    cost = costs[node]
    neighbors = graph[node]

    for n in neighbors.keys(): # 정점의 이웃 정점 중 더 저렴한 경로가 있는 지 탐색
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost # 가격 Uograde
            parents[n] = node # 부모 Upgrade
    cheked.append(node) # 정점 중복 방지

    node = find_lowest_node(costs)

print(costs)
print(parents)


