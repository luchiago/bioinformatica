
geneticCode = {
'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L',
'UCU':'S', 'UCC':'S', 'UCA':'L', 'UCG':'L',
'UAU':'Y', 'UAC':'Y', 'UAA':'ST', 'UAG':'ST',
'UGU':'C', 'UGC':'C', 'UGA':'ST', 'UGG':'W',
'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M',
'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'
}


#Dupla: Juliana Carla e Lucas Hiago

'''
O código foi testado com os seguintes I/O:
Input: "AUGGUCUACAUAGCUGACAAACAGCACGUAGCAUCUCGAGAGGCAUAUGGUCACAUGUUCAAAGUUUGCGCCUAG"
Output: "MVYIADKQHVASREAYGHMFKVCA"
'''

RNAm = input()
i = start = 0
j = 3
codons = []
while 1:
	if RNAm[i:j] == "UAA" or RNAm[i:j] == "UGA" or RNAm[i:j] == "UAG":
		break
	else:
		if RNAm[i:j] == "AUG":
			start = 1
		if start == 1:
			codons.append(RNAm[i:j])
		i = j
		j += 3

aminoacido = ""
for codon in codons:
	aminoacido += geneticCode[codon]
print(aminoacido)

