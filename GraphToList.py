### CONVERSIONE DA MATRICE DI ADIACENZA A LISTA DI ARCHI ###

# Matrice da modificare
X = 0
M = [
        [' ','S','A','B','C','D','E','G1','G2','H','I','J'],
        ['S', X , X , X , X , X , X ,  X ,  X , X , X , X ],
        ['A', 1 , X , X , X , X , X ,  X ,  X , X , X , X ],
        ['B', 1 , 0 , X , X , X , X ,  X ,  X , X , X , X ],
        ['C', 1 , 0 , 1 , X , X , X ,  X ,  X , X , X , X ],
        ['D', 1 , 0 , 0 , 1 , X , X ,  X ,  X , X , X , X ],
        ['E', 0 , 1 , 0 , 0 , 1 , X ,  X ,  X , X , X , X ],
        ['G1',0 , 0 , 0 , 0 , 0 , 1 ,  X ,  X , X , X , X ],
        ['G2',0 , 0 , 1 , 1 , 0 , 0 ,  0 ,  X , X , X , X ],
        ['H', 0 , 1 , 0 , 0 , 0 , 1 ,  1 ,  0 , X , X , X ],
        ['I', 0 , 1 , 1 , 0 , 0 , 0 ,  0 ,  0 , 1 , X , X ],
        ['J', 0 , 0 , 1 , 0 , 0 , 0 ,  0 ,  1 , 0 , 0 , X ],
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
            f.write("\""+M[0][j]+"\",\""+M[i][0]+"\"|")

f.write("];")
f.close()
print("\nCONVERSIONE COMPLETATA\n")

import sys
import argparse
flagG = False

argparser = argparse.ArgumentParser()
argparser.add_argument('-g', '-G', action='store_true')
args = argparser.parse_args()
if args.g:
    flagG = True

# stampa del grafo a partire dalla matrice di adiacenza usando una libreria esterna
        
if flagG == False:
    print("Per generare il grafo aggiungere il parametro -G\n")
    sys.exit()

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(M[0][1:])
for i in range(1, numNodi+1):
    for j in range(1, i):
        if M[i][j] == 1:
            G.add_edge(M[0][j], M[i][0])

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=5000, node_color='skyblue', font_size=8, font_weight='bold', font_color='black', edge_color='black', width=1, edge_cmap=plt.cm.Blues)
plt.show()
