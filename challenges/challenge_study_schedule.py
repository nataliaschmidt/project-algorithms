def study_schedule(permanence_period, target_time):
    count_students = 0

    try:
        for tupla in permanence_period:
            start_time, end_time = tupla
            if start_time <= target_time <= end_time:
                count_students += 1
    except TypeError:
        return None

    return count_students
    raise NotImplementedError


# print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 2))
