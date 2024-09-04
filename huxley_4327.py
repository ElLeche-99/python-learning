condition = True
conditions_cases = []

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
    





