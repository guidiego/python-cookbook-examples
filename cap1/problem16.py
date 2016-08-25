import time

rows = [1, 4, -5, 10, -7, 2, 3, -1]

def list_comprehesion():
    rows_filtered_positive = [r for r in rows if r >= 0]
    rows_filtered_negative = [r for r in rows if r < 0]

    print(rows_filtered_positive)
    print(rows_filtered_negative)

def generator():
    rows_filtered_positive = (r for r in rows if r >= 0)
    rows_filtered_negative = (r for r in rows if r < 0)

    for row in rows_filtered_positive:
        print(row)

    for row in rows_filtered_negative:
        print(row)

def filter_try_except():
    values = '1 2 -3 - 4 N/A'.split()
    def is_int(n):
        try:
            x = int(n)
            return True
        except:
            return False

    vals = list(filter(is_int, values))
    print(vals)


if __name__ == '__main__':
    print('List Comprehesion')
    t1 = time.time()
    list_comprehesion()
    print('spent: %.6f' % (time.time() - t1))

    print('Generator')
    t1 = time.time()
    generator()
    print('spent: %.6f' % (time.time() - t1))

    print('Filter try/except')
    t1 = time.time()
    filter_try_except()
    print('spent: %.6f' % (time.time() - t1))
