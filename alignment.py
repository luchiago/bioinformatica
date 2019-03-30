'''
This .py is about alignment
Use of classes to align
References: Tópicos em Bioinformática - UFPI
Use Smith-Waterman algorithm
'''


class Arrow:
    def __init__(self):
        self.direction = None
        self.cell = None


class Cell:
    def __init__(self):
        self.main_value = None
        # receive a list of arrows
        self.arrows = None


class DNA:
    '''
    Both horizontal and vertical are list of DNA
    '''

    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical


def init(DNA):
    begin = (-2) * (len(DNA.vertical) - 1)
    arr = []
    for i in range(len(DNA.vertical) - 1):
        cell = Cell()
        cell.main_value = begin
        arr2 = [cell]
        # 0 indicates was initialized
        for j in range(1, len(DNA.vertical) - 1):
            cell = Cell()
            cell.main_value = 0
            arr2.append(cell)
        arr.append(arr2)
        begin += 2

    begin = 0
    arr2 = []
    for i in range(len(DNA.horizontal) + 1):
        cell = Cell()
        cell.main_value = begin
        arr2.append(cell)
        begin -= 2

    arr.append(arr2)

    return arr


def get_matrix(array, h, v):
    for i in range(0, len(v)):
        for j in range(0, len(h)):
            print(array[i][j].main_value, end=' ')
        print('')
    print('\n')


if __name__ == "__main__":

    # Tip: 'Z' represents the special symbol
    h = ['T', 'C', 'G']
    v = ['A', 'T', 'C', 'G']
    v.insert(0, 'Z')
    h.insert(0, 'Z')
    v = v[::-1]
    print('Vertical: ')
    for letter in v: print(letter, end='\n')
    print('Horizontal: ')
    for letter in h: print(letter, end=' ')
    print('\n')

    '''
    Values for scores
    '''
    match = 1
    mismatch = -1
    gap = -2

    DNA = DNA(h, v)
    matrix = init(DNA)
    get_matrix(matrix, h, v)

    # Begin Global Alignment
    control = len(h)
    limit = len(v) - 2

    for i in range(limit, -1, -1):
        for j in range(1, control):
            left = matrix[i][j - 1].main_value - 2
            under = matrix[i + 1][j].main_value - 2
            if v[i] == h[j]:
                # Match
                diagonal = matrix[i + 1][j - 1].main_value + match
            else:
                # Mismatch
                diagonal = matrix[i + 1][j - 1].main_value + mismatch
            options = {left : 'left', under : 'under', diagonal: 'diagonal'}
            major = max(left, under, diagonal)
            arrows = []
            for op in options.keys():
                a = Arrow()
                if op == major:
                    if options[op] == 'left':
                        a.cell = matrix[i][j - 1]
                        a.direction = 'left'
                        arrows.append(a)
                    elif options[op] == 'under':
                        a.cell = matrix[i + 1][j]
                        a.direction = 'under'
                        arrows.append(a)
                    elif options[op] == 'diagonal':
                        a.direction = 'diagonal'
                        arrows.append(a)
            matrix[i][j].main_value = major
            matrix[i][j].arrows = arrows

    get_matrix(matrix, h, v)
