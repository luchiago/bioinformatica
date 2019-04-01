'''
This .py is about alignment
Use of classes to align
References: Tópicos em Bioinformática - UFPI
Use Smith-Waterman algorithm
'''


# Classes
class Arrow:
    def __init__(self):
        # where came from
        self.direction = None
        # cell of origin
        self.cell = None


class Cell:
    def __init__(self):
        self.main_value = None
        # Can be a list of arrows
        self.arrows = None
        # List with the letters of DNA
        self.letters = None


def separator(word):
    separated = []
    for letter in word:
        separated.append(letter)

    return separated


def init(v, h):
    begin = (-2) * (len(v) - 1)
    array = []
    for i in range(len(v) - 1):
        cell = Cell()
        cell.main_value = begin
        cell.letters = [v[i], h[0]]
        array_aux = [cell]
        for j in range(1, len(h)):
            cell = Cell()
            cell.letters = [v[i], h[j]]
            cell.main_value = 0
            array_aux.append(cell)
        array.append(array_aux)
        begin += 2

    begin = 0
    array_aux = []
    for i in range(len(h)):
        cell = Cell()
        cell.main_value = begin
        cell.letters = [v[len(v) - 1], h[i]]
        array_aux.append(cell)
        begin -= 2

    array.append(array_aux)

    return array


def get_array(a, v, h):
    for i in range(0, len(v)):
        for j in range(0, len(h)):
            #print(a[i][j].main_value, end=" " + str(a[i][j].letters) + " ")
            print(a[i][j].main_value, end=" ")
        print('')
    print('\n')


def choice_start_cell(a, v, h):
    options = {}
    for i in range(len(h)):
        options[a[0][i].main_value] = a[0][i]
    for i in range(1, len(v)):
        options[a[i][len(h) - 1].main_value] = a[i][len(h) - 1]
    major = max(options.keys())
    for key in options.keys():
        if key == major:
            return options[key]


def fill_array(a, v, h, l):
    '''
    Values for scores
    '''
    match = 1
    mismatch = -1
    # gap = -2

    control = len(v) - 2
    for i in range(control, -1, -1):
        for j in range(1, len(h)):
            left = a[i][j - 1].main_value - 2
            under = a[i + 1][j].main_value - 2
            if v[i] == h[j]:
                # Match
                diagonal = a[i + 1][j - 1].main_value + match
            else:
                # Mismatch
                diagonal = a[i + 1][j - 1].main_value + mismatch
            options = {left: 'left', under: 'under', diagonal: 'diagonal'}
            major = max(left, under, diagonal)
            arrows = []
            for op in options.keys():
                arrow = Arrow()
                arrow.letters = [v[i], h[j]]
                if op == major:
                    if options[op] == 'left':
                        arrow.cell = a[i][j - 1]
                        arrow.direction = 'left'
                        arrows.append(arrow)
                    elif options[op] == 'under':
                        arrow.cell = a[i + 1][j]
                        arrow.direction = 'under'
                        arrows.append(arrow)
                    elif options[op] == 'diagonal':
                        arrow.cell = a[i + 1][j - 1]
                        arrow.direction = 'diagonal'
                        arrows.append(arrow)

            if l and major < 0:
                major = 0
            a[i][j].main_value = major
            a[i][j].arrows = arrows

    get_array(a, v, h)
    start = choice_start_cell(a, v, h)
    # print(type(start))
    traceback(start)


def traceback(s):
    print("Entro")
    score = 0
    upper = down = ""
    while 1:
        score += s.main_value
        #print(score)
        if s.letters[0] == "Z" and s.letters[1] == "Z":
            pass
        else:
            if s.letters[0] == 'Z':
                upper += '-'
            else:
                upper += s.letters[0]
            if s.letters[1] == 'Z':
                down += '-'
            else:
                down += s.letters[0]

        if s.arrows is None:
            break
        s = s.arrows[0].cell
        #print(s.main_value)

    print("Score: " + str(score))
    print("V: " + upper[::-1])
    print("H: " + down[::-1])


if __name__ == "__main__":

    # vertical = input()
    vertical = "TGTG"
    vertical = vertical[::-1]
    vertical += "Z"
    vertical = separator(vertical)
    # horizontal = input()
    horizontal = "TGT"
    horizontal = horizontal.replace(horizontal, "Z" + horizontal)
    horizontal = separator(horizontal)

    print("Vertical:")
    for letter in vertical:
        print(letter, end='\n')

    print("Horizontal:")
    for letter in horizontal:
        print(letter, end=' ')
    print('')

    array = init(vertical, horizontal)
    # print(len(array))
    get_array(array, vertical, horizontal)

    local = int(input('Alinhamento Global (0) ou Local(1)? '))

    fill_array(array, vertical, horizontal, local)
