% Edge Colouring CSP solver

% usiamo una lista di Archi per rappresentare il Grafo, dove ogni Arco è una coppia di Nodi
% prendiamo la lista in input dal file ListaEdge.dzn
include "ListaEdge.dzn";

%output ["n = " ++ show(n) ++"\n"];
%output ["Edge_" ++ show(i) ++ " = " ++ show(Edge[i, 1]) ++ "-" ++ show(Edge[i, 2]) ++ "\n" | i in 1..n];

% ora creiamo la lista di variabili di assegnare, che rappresentano i colori degli Archi
array[1..n] of var 1..3: EdgeColor;

% vincoli
constraint forall(x in 1..n) (
    forall(y in 1..n) (
        forall(z in 1..n) (
            if x!=y /\ y!=z /\ z!=x then 
                if (Edge[x,1]==Edge[y,1]/\Edge[y,2]==Edge[z,1]/\Edge[z,2]==Edge[x,2]) \/  
                   (Edge[x,1]==Edge[y,1]/\Edge[y,2]==Edge[z,2]/\Edge[z,1]==Edge[x,2]) \/
                   (Edge[x,1]==Edge[y,2]/\Edge[y,1]==Edge[z,1]/\Edge[z,2]==Edge[x,2]) \/
                   (Edge[x,1]==Edge[y,2]/\Edge[y,1]==Edge[z,2]/\Edge[z,1]==Edge[x,2]) \/
                   (Edge[x,2]==Edge[y,1]/\Edge[y,2]==Edge[z,1]/\Edge[z,2]==Edge[x,1]) \/
                   (Edge[x,2]==Edge[y,1]/\Edge[y,2]==Edge[z,2]/\Edge[z,1]==Edge[x,1]) \/ 
                   (Edge[x,2]==Edge[y,2]/\Edge[y,1]==Edge[z,1]/\Edge[z,2]==Edge[x,1]) \/
                   (Edge[x,2]==Edge[y,2]/\Edge[y,1]==Edge[z,2]/\Edge[z,1]==Edge[x,1]) then % i tre archi formano un triangolo  
                   if EdgeColor[x] == EdgeColor[y] then 
                      EdgeColor[y] != EdgeColor[z]
                   else
                      if EdgeColor[y] == EdgeColor[z] then
                         EdgeColor[x] != EdgeColor[y]
                      endif
                   endif
                endif
            endif
        )
    )
);
solve satisfy;

output["\nColor of Edge:\n"];
output ["Edge_" ++ show(i) ++ " = " ++ show(EdgeColor[i]) ++"\n" | i in 1..n];
