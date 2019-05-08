#k = 3
#DNA = "GCGTAATGCAATAGCCCGC"

#slide de remotando genomas parte 1

k = int(input())
DNA = input()

k_mers = []
size = len(DNA) - 2

st = 0
end = k

for i in range(0, size):
    k_mers.append(DNA[st:end])
    st = st + 1
    end = end + 1

k_mers.sort() #para ordem lexiografica

print(k_mers)