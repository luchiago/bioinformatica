def ler_fasta(arquivo):
    sequencia = ''
    dna = []
    with open(arquivo, 'r') as fasta:
            sequencia = ''
            for linha in fasta:
                if not linha.startswith('>'):
                    sequencia += linha
                else:
                    kd = linha
            dna.append(sequencia)

    return dna, kd

def replace_kd(kd):
    k = d = ""
    ind_k = kd.find('k')
    ind_d = kd.find('d')
    len_kd = len(kd)

    for i in range(ind_k + 1, ind_d):
        if kd[i] != "=":
            k += kd[i]
    
    for i in range(ind_d + 1, len_kd):
        if kd[i] != "=":
            d += kd[i]
    
    return int(k), int(d)

def gerar_arquivo(k, d, sequence):

    kdmers = []
    ind_k1 = 0
    ind_k2 = k
    ind_d1 = ind_k2 + 1
    ind_d2 = ind_d1 + k

    while ind_d2 != (len(sequence) + 1):

        kdmer1 = sequence[ind_k1: ind_k2]
        kdmer2 = sequence[ind_d1: ind_d2]

        tupla = (kdmer1, kdmer2)
        kdmers.append(tupla)
        kdmers.sort()

        ind_k1 += 1
        ind_k2 += 1

        ind_d1 = ind_k2 + 1
        ind_d2 = ind_d1 + k
    
    kdmer = "["
    for i in range(len(kdmers)):
        kdmer += kdmers[i][0]
        kdmer += "|"
        kdmer += kdmers[i][1]
        if i != len(kdmers) - 1:
            kdmer += ","
    kdmer += "]"
    
    file_name = "k" + str(k) + "d" + str(d) + "mer.txt"
    file = open(file_name, 'w')
    file.write(kdmer)
    file.close()
    

dna, kd = ler_fasta("sequence.fasta")
k, d = replace_kd(kd)

sequence = ""
for i in dna:
    sequence += i

gerar_arquivo(k, d, sequence)
