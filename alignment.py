'''
This .py is about alignment
Use of classes to align
References: Tópicos em Bioinformática - UFPI
'''


class Cell:
    def __init__(self):
        self.main_value = None
        self.left_value = None
        self.under_value = None
        self.diagonal_value = None

    def choose_main_value(self):
        self.main_value = max(self.diagonal_value, self.left_value, self.under_value)


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
        arr2 = [begin]
        #0 indicates was initialized
        for j in range(1, len(DNA.vertical)):
            arr2.append(0)
        arr.append(arr2)
        begin += 2

    begin = 0
    arr2 = []
    for i in range(len(DNA.horizontal) + 1):
        arr2.append(begin)
        begin -= 2

    arr.append(arr2)

    return arr

if __name__ == "__main__":
    h = ['T', 'C', 'G']
    v = ['G', 'C', 'T', 'A']

    DNA = DNA(h, v)
    matrix = init(DNA)
    for i in matrix:
        print(i)