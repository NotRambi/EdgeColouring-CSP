### CONVERSIONE DA MATRICE DI ADIACENZA A LISTA DI ARCHI ###

# Matrice da modificare

M = [
        [' ','S','A','B','C','D','E','G1','G2','H','I','J'],
        ['S', 0 , 1 , 1 , 1 , 1 , 0 ,  0 ,  0 , 0 , 0 , 0 ],
        ['A', 1 , 0 , 0 , 0 , 0 , 1 ,  0 ,  0 , 1 , 1 , 0 ],
        ['B', 1 , 0 , 0 , 1 , 0 , 0 ,  0 ,  1 , 0 , 1 , 1 ],
        ['C', 1 , 0 , 1 , 0 , 1 , 0 ,  0 ,  1 , 0 , 0 , 0 ],
        ['D', 1 , 0 , 0 , 1 , 0 , 1 ,  0 ,  0 , 0 , 0 , 0 ],
        ['E', 0 , 1 , 0 , 0 , 1 , 0 ,  1 ,  0 , 1 , 0 , 0 ],
        ['G1',0 , 0 , 0 , 0 , 0 , 1 ,  0 ,  0 , 1 , 0 , 0 ],
        ['G2',0 , 0 , 1 , 1 , 0 , 0 ,  0 ,  0 , 0 , 0 , 1 ],
        ['H', 0 , 1 , 0 , 0 , 0 , 1 ,  1 ,  0 , 0 , 1 , 0 ],
        ['I', 0 , 1 , 1 , 0 , 0 , 0 ,  0 ,  0 , 1 , 0 , 0 ],
        ['J', 0 , 0 , 1 , 0 , 0 , 0 ,  0 ,  1 , 0 , 0 , 0 ],
    ]

numNodi = len(M) -1 
numArchi = 0
for i in range(1, numNodi+1):
    for j in range(1, i):
        if M[i][j] == 1:
            numArchi += 1
            
f = open("ListaEdge.dzn", "w", encoding="utf-8")
f.write("int: n="+str(numArchi)+";\n")
f.write("array[1..n,1..2] of string: Edge = [|")

for i in range(1, numNodi+1):
    for j in range(1, i):
        if M[i][j] == 1:
            f.write("\""+M[i][0]+"\",\""+M[0][j]+"\"|")

f.write("];")
f.close()