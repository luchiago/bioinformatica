geneticCode = {
    'UUU': 'F', 'UUF': 'F', 'UUA': 'L', 'UUG': 'L',  # UU
    'UCU': 'S', 'UCC': 'S', 'UCA': 'L', 'UCG': 'L',  # UC
    'UAU': 'T', 'UAC': 'T', 'UAA': 'ST', 'UAG': 'ST',  # UA
    'UGU': 'C', 'UGC': 'C', 'UGA': 'ST', 'UGG': 'W',  # UG
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'G', 'CAG': 'G',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'A', 'AGG': 'A',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
}

#Dupla: Juliana Carla e Lucas Hiago

RNAm = input()
'''
O programa foi testado com este input
RNAm = "GGC.CGA.UUA.AUG.CUU.AAA.UGC.GGC.CUA.AAU.UAU"
'''
RNAm = RNAm.split(".") #para separar dos pontos os codons
aminoacido = ""
start = 0
for codon in RNAm:
    if codon == "AUG":
        #significa que vai iniciar a sintese
        aminoacido += geneticCode[codon] + " "
        start = 1
    elif codon == "UAA" or codon == "UAG" or codon == "UGA":
        #siginifca que vai parar
        break
    elif start:
        aminoacido += geneticCode[codon] + " "
print("Cadeia de Aminoácido " + aminoacido)
