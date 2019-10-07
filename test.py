arr = [1, 2, 2, 3, 1]


def degree_finder(arr, search_key=None):
    count_dict = {x: arr.count(x) for x in arr}
    for key, val in count_dict.items():
        if search_key is not None:
            if val == max(count_dict.values()):
                return count_dict[key]


def degreeOfArray(arr):
    count_dict = {x: arr.count(x) for x in arr}
    degree = degree_finder(arr)

    elements = []
    for key, val in count_dict.items():
        if val == degree:
            elements.append(key)

    lengths = []
    for key in elements:
        start = 0
        for i, item in enumerate(arr):
            if item == key:
                start = i
                break
        sub_arr = arr[start: ]
        for i, item in enumerate(sub_arr):
            sub_degree = degree_finder(sub_arr[: i])
            if sub_degree == degree:
                lengths.append(i)
                break

        return min(lengths)




