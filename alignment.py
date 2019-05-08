import numpy as np

gap = -10
match = 5
mismatch = -3

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

def alignment(t, v, h, table):
    
    tam_v = len(v)
    tam_h = len(h)

    

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
