condition = True
conditions_cases = []
results = []

#dict_structure = {'max_dist': '', 'min_dist': '', 'distences': 'lista[]'}

while(condition):
    distances = True
    distances_cases = []
    conditions = input()

    if(conditions == ''):
        condition = False
        break

    while(distances):
        distance = int(input())
        distances_cases.append(int(distance))

        if(distance == 0):
            distances = False
            
    dict_structure = {'max_distance': int(conditions.split(' ')[0]), 'min_distance': int(conditions.split(' ')[1]), 'distances': distances_cases}
    conditions_cases.append(dict_structure)


for test_case in conditions_cases:
    min_dist = []
    max_dist = [0]

    for distance in test_case['distances']:
        if distance >= test_case['min_distance']:
            if len(min_dist) == 0:
                min_dist.append(test_case['distances'].index(distance)+1)
            
            if(distance <= test_case['max_distance']):
                max_dist[0] = test_case['distances'].index(distance)+1
    results.append([min_dist[0], max_dist[0]])


for result in results:
    print("{} {}\n".format(result[0], result[1]), end='')

                