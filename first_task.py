#Dupla: Juliana Carla e Lucas Hiago

#DNA de entrada
DNA = "GCC.GCC.GGT.TAA.TGC.CGA.TAA.TGC.ATG"
DNA = DNA.split(".")
#Duplicação do DNA

#RNAm
RNAm = ""
for trinca in DNA:
    auxiliar = ""
    for letter in range(0, len(trinca)):
        if trinca[letter] == 'C':
            auxiliar += 'G'
        elif trinca[letter] == 'G':
            auxiliar += 'C'
        elif trinca[letter] == 'T':
            auxiliar += 'A'
        elif trinca[letter] == 'A':
            auxiliar += 'U'
    RNAm += (auxiliar + ".")

print(RNAm)

'''
DNA ORIGINAL  = GCC.GCC.GGT.TAA.TGC.CGA.TAA.TGC.ATG
         RNAm = CGG CGG CCA AUU ACG GCU AUU ACG UAC
'''
