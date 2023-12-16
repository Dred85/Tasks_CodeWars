def gps(s, x):
    ''' Высчитываем среднюю скорость'''
    dist_list = []
    for i in range(len(x)-1):
        # находим расстояние между 2-мя соседними точками и  добавляем к новому списку dist_list
        distance_steps = x[i + 1] - x[i]
        dist_list.append(distance_steps)

    # находим пройденную дистанцию
    delta_distance = sum(dist_list)
    if delta_distance <= 1:
        return 0


    average_speed_list = []
    for i in range(len(dist_list)):
        # Высчитываем среднюю скорость на дистанции и добавляем в список average_speed_list
        average_speed_list.append((3600 * dist_list[i]) / s)
        # возврат максимального и округленного значения средней скорости
    return  round(max(average_speed_list))

# В одну строчку
# def gps(s, x):
#     return max(((x[i] - x[i - 1]) * 3600 / s for i in range(len(x))), default=0)


x = [0.0, 0.11, 0.22, 0.33, 0.44, 0.65, 1.08, 1.26, 1.68, 1.89, 2.1, 2.31, 2.52, 3.25]
s = 12
print(gps(s, x))

