grades = (1, 2, 3, 4, 5, 6, 7, 8, 9)

def drop_first_n_last(grades):
    first, *middle, last = grades
    return sum(middle) / len(middle)

result = drop_first_n_last(grades)
print(result)

