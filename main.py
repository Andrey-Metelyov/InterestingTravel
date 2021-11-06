def dist(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

def find_path(graph, start, end):
    # print(f"find_path({start}, {end})")
    wave = dict()
    current_distance = 0
    wave = {start}
    visited = {start}
    while wave:
        new_wave = set()
        for city_from in wave:
            # print("before:", wave)
            visited.add(city_from)
            for city_to in graph[city_from]:
                if city_to == end:
                    return current_distance + 1
                if city_to not in visited:
                    new_wave.add(city_to)
        current_distance += 1
        wave = new_wave
        # print("after:", wave)
    return -1

n = int(input())

cities = []
for _ in range(n):
    cities.append([int(x) for x in input().split()])

max_distance = int(input())

start, end = (int(x) for x in input().split())

# print(n)
# for i, city in enumerate(cities, start=1):
#     print(i, ": x =", city[0], ", y =", city[1])
# print(max_distance)
# print(start, end)

graph = dict()
for i, city_from in enumerate(cities, start=1):
    graph[i] = set()
    current = graph[i]
    for j, city_to in enumerate(cities, start=1):
        if i != j and dist(city_from[0], city_from[1], city_to[0], city_to[1]) <= max_distance:
            current.add(j)

# print(graph)

print(find_path(graph, start, end))
