def index_of_nearest(lst: list, x: int):
    if not len(lst):
        return -1
    else:
        minimum = abs(x - lst[0])
        index_min_number = 0
        for index, value in enumerate(lst):
            if abs(x - value) < minimum:
                minimum = abs(x - value)
                index_min_number = index
        return index_min_number

print(index_of_nearest([7, 13, 3, 5, 18], 0))
