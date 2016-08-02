from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    import pdb; pdb.set_trace()
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    with open('somefile.txt') as f:
        results = search(f, 'python', 5)
        import pdb; pdb.set_trace()
        for line, prevlines in results:
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)
