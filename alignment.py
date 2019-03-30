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
        self.letters = None


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
        cell.letters = [DNA.vertical[i], DNA.horizontal[0]]
        arr2 = [cell]
        # 0 indicates was initialized
        for j in range(1, len(DNA.vertical) - 1):
            cell = Cell()
            cell.letters = [DNA.vertical[i], DNA.horizontal[j]]
            cell.main_value = 0
            arr2.append(cell)
        arr.append(arr2)
        begin += 2

    begin = 0
    arr2 = []
    for i in range(len(DNA.horizontal)):
        cell = Cell()
        cell.main_value = begin
        #a = Arrow()
        cell.letters = [DNA.vertical[len(DNA.vertical) - 1], DNA.horizontal[i]]
        #cell.arrows = a
        arr2.append(cell)
        begin -= 2

    arr.append(arr2)

    return arr


def get_matrix(array, h, v):
    for i in range(0, len(v)):
        for j in range(0, len(h)):
            #print(array[i][j].main_value, end=" " + str(array[i][j].letters) + " ")
            print(array[i][j].main_value, end=" ")
        print('')
    print('\n')


def choice_start_value(matrix, h, v):
    #Options is a dict of main values of cells
    options = {}
    for cell in matrix[0]:
        options[cell.main_value] = cell
    for i in range(0, len(v)):
        cell = matrix[i][len(h) - 1]
        options[cell.main_value] = cell

    major = max(options.keys())
    return options[major]


if __name__ == "__main__":

    # Tip: 'Z' represents the special symbol
    h = ['T', 'G', 'T']
    v = ['G', 'T', 'G', 'T']
    #WITH THIS GLOBAL AND LOCAL ARE RIGHT, TEST WITH SLIDE ONE
    # if is local
    LOCAL = False
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

    # Begin Alignment
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
                a.letters = [v[i], h[j]]
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
                        a.cell = matrix[i + 1][j - 1]
                        a.direction = 'diagonal'
                        arrows.append(a)
            if LOCAL is True and major < 0:
                major = 0
            matrix[i][j].main_value = major
            matrix[i][j].arrows = arrows

    get_matrix(matrix, h, v)

    #Traceback
    start_cell = choice_start_value(matrix, h, v)
    score = 0
    upper_alignment = down_alignment = ""
    limit = max((len(v) - 1), (len(h) - 1))
    for i in range(limit):
        if LOCAL is True and start_cell.main_value < 0:
            start_cell.main_value = 0
        score += start_cell.main_value
        arrows = start_cell.arrows
        if start_cell.letters[0] == 'Z':
            upper_alignment += '-'
        else:
            upper_alignment += start_cell.letters[0]
        if start_cell.letters[1] == 'Z':
            down_alignment += '-'
        else:
            down_alignment += start_cell.letters[0]
        if start_cell.arrows is None:
            break
        major = []
        for a in arrows:
            major.append(a.cell.main_value)
        major = max(major)
        for a in arrows:
            if major == a.cell.main_value:
                start_cell = a.cell

    print(upper_alignment[::-1])
    print(down_alignment[::-1])
    print(score)