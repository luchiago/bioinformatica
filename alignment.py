
gap = -2
match = 1
mismatch = -1

def build_table(v, h):
    table = []
    
    n = gap * (v - 1)
    for i in range(0, v - 1):
        row = []
        row.append(n)
        n -= gap
        for j in range(0, h - 1):
            row.append(0)
        table.append(row)

    row = []
    for j in range(0, h):
        row.append(gap * j)
    table.append(row)

    return table


def build_table_of_dir(v, h):
    table = []

    for i in range(0, v):
        row = []
        for j in range(0, h):
            row.append(None)
        table.append(row)

    return table


def traceback(v, h, table, table_of_dir):
    
    major = -10000000000000000
    tam_v = len(v)
    tam_h = len(h)

    for i in range(0, len(v)):
        if table[i][tam_h - 1] > major:
            major = table[i][tam_h - 1]
    
    for i in range(0, len(h)):
        if table[0][i] > major:
            major = table[0][i]
    
    print(major)

def alignment(t, v, h, table):
    
    tam_v = len(v)
    tam_h = len(h)

    table_of_dir = build_table_of_dir(tam_v, tam_h)

    letter_v = 3
    for i in range(tam_v - 2, -1, -1):
        letter_h = 1
        for j in range(1, tam_h):
            sup = table[i][j - 1] + gap
            low = table[i + 1][j] + gap
            mid = table[i + 1][j - 1]

            if v[letter_v] == h[letter_h]:
                mid += match
            elif v[letter_v] != h[letter_h]:
                mid += mismatch 

            choose_one = max(sup, low, mid)

            if choose_one == sup:
                #esquerda
                direction = [[i, j - 1], [v[letter_v], h[letter_h]]]
            elif choose_one == low:
                #abaixo
                direction = [[i + 1, j], [v[letter_v], h[letter_h]]]
            elif choose_one == mid:
                #diagonal
                direction = [[i + 1, j - 1], [v[letter_v], h[letter_h]]]

            if t == 1 and choose_one < 0:
                #se for local
                choose_one = 0
            table[i][j] = choose_one
            table_of_dir[i][j] = direction
            
            letter_h += 1
        letter_v -= 1
    '''
    for i in range(0, tam_v):
        for j in range(0, tam_h):
            print(table[i][j], end=' ')
        print('\n')
    
    for i in range(0, tam_v):
        for j in range(0, tam_h):
            print(table_of_dir[i][j], end=' ')
        print('\n')
    '''

    traceback(v, h, table, table_of_dir)
    

if __name__ == "__main__":

    #vertical
    v = "ATCG"
    #horizontal
    h = "TCG"
    
    v = v[::-1]
    v += "X"
    h = "X" + h

    table = build_table(len(v), len(h))
    
    #type_of_alignment = int(input("Escolha o tipo de alinhamento: Global (0) ou Local (1) > "))
    type_of_alignment = 0

    alignment(type_of_alignment, v, h, table)
