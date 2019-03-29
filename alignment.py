'''
This .py is about alignment
Use of classes to align
References: Tópicos em Bioinformática - UFPI
Use Smith-Waterman algorithm
'''


class Arrow:
    def __init__(self):
        self.direction = None


class Cell:
    def __init__(self):
        self.main_value = None
        self.left_value = None
        self.under_value = None
        self.diagonal_value = None
        # receive a list of arrows
        self.arrows = None

    def choose_main_value(self):
        self.main_value = max(self.diagonal_value, self.left_value, self.under_value)

    def set_arrows(self, arrows):
        self.arrows = arrows


class DNA:
    '''
    Both horizontal and vertical are list of DNA
    '''

    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical


def init(DNA):
    begin = (-2) * len(DNA.vertical)
    arr = []
    for i in range(len(DNA.vertical)):
        cell = Cell()
        cell.main_value = begin
        arr2 = [cell]
        # 0 indicates was initialized
        for j in range(1, len(DNA.vertical)):
            cell.main_value = 0
            arr2.append(cell)
        arr.append(arr2)
        begin += 2

    begin = 0
    arr2 = []
    for i in range(len(DNA.horizontal) + 1):
        cell.main_value = begin
        arr2.append(cell)
        begin -= 2

    arr.append(arr2)

    return arr


def get_matrix(array):
    for i in array:
        print(i)


if __name__ == "__main__":
    h = ['T', 'C', 'G']
    v = ['G', 'C', 'T', 'A']

    '''
    Values for scores
    '''
    match = 1
    mismatch = -1
    gap = -2

    DNA = DNA(h, v)
    matrix = init(DNA)
    get_matrix(matrix)

    #Begin Global Alignment
    control = len(v) - 1
    limit = len(h)
    for i in range(control, 0, -1):
        for j in range(1, limit):
            matrix[i][j]

    '''
    ISSUES
    Change get_matrix
    '''