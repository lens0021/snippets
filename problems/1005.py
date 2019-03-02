# https://www.acmicpc.net/problem/1005

number_of_test_cases = int(input())

for _ in range(number_of_test_cases):
    # Read variables
    number_of_buildings, number_of_rules = map(int, input().split(' '))
    build_times = list(map(int, input().split(' ')))

    paths = []
    for _ in range(number_of_rules):
        paths.append(tuple(map(lambda x: int(x)-1, input().split(' '))))

    final_building = int(input())-1

    # Get rid of the useless paths.
    visited = [final_building]
    useful_paths = []
    for vertex in visited:
        for path in paths:
            if path[1] == vertex:
                visited.append(path[0])
                useful_paths.append(path)

    # Calculate
    total_time = build_times[0]

    built = [0]
    buildings = []
    while final_building not in built:
        if len(buildings):
            has_built = min(buildings, key=lambda t: t[1])

            built.append(has_built[0])
            buildings.remove(has_built)
            total_time += has_built[1]
            for building in buildings:
                building[1] -= has_built[1]
        else:
            buildables = []
            for path in useful_paths:
                for building in built:
                    if (building == path[0]) and (path[1] not in built):
                        buildables.append(path[1])

            for buildable in buildables:
                buildings.append([buildable, build_times[buildable]])

    print(total_time)
